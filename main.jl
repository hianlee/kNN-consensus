using Random, Parameters, PyCall, LightGraphs, LinearAlgebra, DelimitedFiles, CSV, DataFrames, Statistics
# nx = pyimport("networkx")

# Parameters
max_iter = 10000
max_trials = 1
elements = 1000
n_agents = 100
n_neighbours = [10] #range(2, stop=98)
ks = n_neighbours .+ 1

error_rate = .3
evidence_rate = .01

recheck = false

@with_kw mutable struct Agent
    name::Int
    n_states::Int
    neighbours = []

    belief = zeros(n_states)
    last_update = 0
    converged = false
end

@with_kw mutable struct Environment
    n_states::Int
    state = rand([-1, 1], n_states)
end

function check_env(agent, env)    # Agent able to check environment
    global error_rate, elements, recheck
    evidence = copy(agent.belief)
    uncertainties = findall(x -> x == 0, agent.belief)  # Pick proposition to check
    if size(uncertainties) != (0,)
        check_prop = uncertainties[rand(1:end)]
        if rand() > error_rate              # Provide good data
            evidence[check_prop] = env.state[check_prop]
        else                                # Provide bad data
            evidence[check_prop] = -env.state[check_prop]
        end
        # Fuse evidence directly
        agent.belief = evidence
        agent.last_update = 0
    elseif recheck
        # Check random proposition to ensure belief is correct
        check_prop = rand(1:elements)
        if rand() > error_rate              # Provide good data
            evidence[check_prop] = env.state[check_prop]
        else                                # Provide bad data
            evidence[check_prop] = -env.state[check_prop]
        end
        if evidence == agent.belief
            agent.last_update += 1
        else
            # Fuse evidence directly
            agent.belief = evidence
            agent.last_update = 0
        end
    end
end

function fuse_belief_sets(self, new_belief_set)
    final_belief = self.belief + new_belief_set
    clamp!(final_belief, -1, 1)
    return final_belief
end

function system_check_converged(agent_list, threshold)
    # Check if agent has converged individually
    for agent in agent_list
        if agent.last_update > threshold
            agent.converged = true
        end
    end
    # Check if all agents have converged
    for agent in agent_list
        if !agent.converged
            return false
        end
    end
    return true
end

all_errors = []
all_std_dev = []
all_convergence_times = []
time_std_dev = []
all_opinions = []

for k in ks
    trial = 0
    k_error = []
    convergence_times = []
    opinions = 0
    while trial < max_trials
        # Random.seed!(5512)
        # Initialise environment
        env = Environment(n_states=elements)
        g = watts_strogatz(n_agents, k, 0)

        # Initialise agents
        sys_converged = false
        agent_list = []
        opinion_counter = []

        for i in range(1, stop=n_agents)
            agent = Agent(name=i, n_states=elements)
            push!(agent_list, agent)
            # Connect the network
            for edge in collect(edges(g))
                if src(edge) == i
                    push!(agent.neighbours, dst(edge))
                elseif dst(edge) == i
                    push!(agent.neighbours, src(edge))
                end
            end
        end

        iteration = 0

        while iteration < max_iter && !sys_converged
            trial_opinion_list = []
            for agent in agent_list
                if rand() < evidence_rate
                    check_env(agent, env)    # Get the evidence and merge
                end
            end

            # Pick two connected agents and fuse the beliefs of those two agents only
            agent1 = agent_list[rand(1:end)]
            agent2 = agent_list[agent1.neighbours[rand(1:end)]]
            consensus = fuse_belief_sets(agent1, agent2.belief)

            if agent1.belief != consensus
                agent1.belief = consensus
                agent1.last_update = 0
            else
                agent1.last_update += 1
            end

            if agent2.belief != consensus
                agent2.belief = consensus
                agent2.last_update = 0
            else
                agent2.last_update += 1
            end

            for agent in agent_list
                if agent.belief ∉ trial_opinion_list
                    push!(trial_opinion_list, agent.belief)
                end
            end
            push!(opinion_counter, length(trial_opinion_list))


            sys_converged = system_check_converged(agent_list, 100)


            iteration += 1
            # println(iteration)

            # This loop triggers immediately before the iteration loop ends and saves convergence times
            # if sys_converged
            #     # println("System Converged at iteration ", iteration-100)
            #     push!(convergence_times, iteration-100)
            # elseif iteration == max_iter
            #     push!(convergence_times, iteration)
            # end
        end
        
        # This chunk calculates system error
        error = 0
        # Calculate individual agent error first
        for agent in agent_list
            indiv_error = 0
            for i in range(1, stop=elements)
                indiv_error += (abs(agent.belief[i] - env.state[i]) / 2)
            end
            error += indiv_error
        end
        error /= (n_agents * elements)  # Sum and average

        push!(k_error, error)

        # This chunk finds the number of opinions in the system
        opinion_list = []
        for agent in agent_list
            if agent.belief ∉ opinion_list
                push!(opinion_list, agent.belief)
            end
        end
        trial += 1
        opinion_tracker_file = "data/k10_eps3_ev01_opinion_track.csv"
        CSV.write(opinion_tracker_file, DataFrame([opinion_counter]), header=false)
    end



    push!(all_opinions, opinions/max_trials)
    push!(all_errors, mean(k_error))
    push!(all_std_dev, std(k_error))
    push!(all_convergence_times, mean(convergence_times))
    push!(time_std_dev, std(convergence_times))
    println("k", k-1, " Error: ", mean(k_error), " ± ", std(k_error),
            " Average Convergence Time: ", mean(convergence_times),
            " ± ", std(convergence_times), " Average No. of Opinions: ", opinions/max_trials)
end

#   Save data files
error_file = "data/eps1_ev5_strat_error.csv"
std_dev_file = "data/eps1_ev5_strat_stddev.csv"
conv_time_file = "data/eps1_ev5_strat_convtime.csv"
conv_time_sd_file = "data/eps_ev5_strat_convtime_stddev.csv"
opinion_file = "data/eps4_ev5_ops.csv"
CSV.write(error_file, DataFrame([all_errors]), header=false)
CSV.write(std_dev_file, DataFrame([all_std_dev]), header=false)
CSV.write(conv_time_file, DataFrame([all_convergence_times]), header=false)
CSV.write(conv_time_sd_file, DataFrame([time_std_dev]), header=false)
CSV.write(opinion_file, DataFrame([all_opinions]), header=false)
println("Done")
