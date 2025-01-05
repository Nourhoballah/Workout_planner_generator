class Goal:
    def __init__(self):
        pass

    def goal_display(self):
        print("1. Gain muscle mass/hypertrophy")
        print("2. Lose weight")
        print("3. Improve muscle endurance")
        print("4. Muscular power")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            print("1. Gain muscle mass/hypertrophy is your goal")
            print("""
            For each exercise:
            - Number of sets: 2-3
            - Number of repetitions: 8-10
            - Time of rest: 60-90 seconds
            - Tempo: 3-0-1
            - Protocol of overload: 8-MAX(10) or 10-MAX(12)
            """)
        elif choice == "2":
            print("2. Lose weight is your goal")
            print("""
            For each exercise:
            - Number of sets: 2
            - Number of repetitions: 10-15
            - Time of rest: 20 seconds
            - Tempo: 2-0-2
            - Protocol of overload: 10-MAX(12) or 12-MAX(15)
            """)
        elif choice == "3":
            print("3. Improve muscle endurance is your goal")
            print("""
            For each exercise:
            - Number of sets: 3
            - Number of repetitions: 15
            - Time of rest: 30-60 seconds
            - Tempo: 2-0-2
            - Protocol of overload: 15-MAX(20)
            """)
        elif choice == "4":
            print("4. Muscular power is your goal")
            print("""
            For each exercise:
            - Number of sets: 3
            - Number of repetitions: 1-6
            - Time of rest: 2 minutes
            - Tempo: 3-0-0
            - Protocol of overload: 1-MAX(6)
            """)
        else:
            print("Invalid choice. Please select between 1 and 4")


