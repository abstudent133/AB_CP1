#AB 1st Crew Shares

money = int(input("What was the amout of money earned by the pirates:"))
num_crew = int(input("How many crew members are there:"))
share = money/(num_crew + 10)
crew_share = share - 500
first_mate_share = share * 3
captain_share = share * 7
print(f"The captain gets: ${captain_share:.2f}")
print(f"The first mate gets: ${first_mate_share:.2f}")
print(f"Each member of the crew still needs: ${crew_share:.2f}")

