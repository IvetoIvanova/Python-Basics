def voting_system():
    print("💡 Welcome to the voting system!")

    candidates = []
    votes = []

    print("\nEnter candidate names one by one. Type 'end' when you're done.")

    while True:
        name = input("Enter candidate name: ")

        if name == "end":
            if len(candidates) < 2:
                print("⚠️ At least two candidates are required!")
                continue
            break

        candidates.append(name)
        votes.append(0)

    num_voters = int(input("\nEnter the number of voters: "))

    def voting_round(candidates, num_voters):
        votes = [0] * len(candidates)
        voted_ids = []
        valid_votes = 0

        print("\n📢 Voting has started! Enter the candidate's name to vote.")
        print("Each voter has a unique ID. Type 'end' to stop voting early.\n")

        for _ in range(num_voters):
            while True:
                voter_id = input("Enter your ID: ")

                if voter_id in voted_ids:
                    print("⚠ You have already voted! Try again with a different ID.")
                else:
                    voted_ids.append(voter_id)
                    break

            while True:
                vote = input("Vote for a candidate: ")

                if vote == "end":
                    return votes

                if vote in candidates:
                    index = candidates.index(vote)
                    votes[index] += 1
                    voted_ids.append(voter_id)
                    valid_votes += 1
                    break
                else:
                    print("⚠ Invalid candidate! Please try again.")

        return votes

    votes = voting_round(candidates, num_voters)
    round_number = 2

    while True:
        print("\n📊 Voting Results:")

        max_votes = max(votes)
        winners = []

        for i in range(len(candidates)):
            if votes[i] == max_votes:
                winners.append(candidates[i])

        for i in range(len(candidates)):
            total_votes = sum(votes)

            if total_votes > 0:
                percentage = (votes[i] / total_votes) * 100
            else:
                percentage = 0

            print(f"{candidates[i]}: {votes[i]} votes ({percentage:.2f}%)")

        if len(winners) == 1:
            print(f"\n🏆 The winner is: {winners[0]} with {max_votes} votes! 🎉")
            break
        else:
            print(f"\n⚠ There is a tie! Starting round {round_number} of voting.")
            print("Candidates moving to the next round:", ", ".join(winners))
            round_number += 1

            # New round of voting only between the tied candidates
            candidates = winners
            votes = voting_round(candidates, num_voters)


# Start the voting system
voting_system()
