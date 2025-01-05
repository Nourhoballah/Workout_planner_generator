from Leg_day import Leg
from upper_body_day import UpperBodyDay
from cardio_day import Cardio
from goals import Goal
import random


class WorkoutPlanner:
    def __init__(self): #c'est le constructeur, j'initialise les sous classes
        self.leg_workout = Leg()
        self.upper_body_workout = UpperBodyDay()
        self.cardio_workout = Cardio()
        self.goal = Goal()

    def plan_preferences(self): #je demande les préférences de l'utilisateur
        leg_day = int(input("How many leg days would you like per week? "))
        upper_day = int(input("How many upper body days would you like per week? "))
        cardio_day = int(input("How many cardio days would you like per week? "))
        return leg_day, upper_day, cardio_day

    def generate_plan(self, leg_days, upper_days, cardio_days):
        plan = [] # va contenir les jours d'entraînement et leurs exercices

        # Générer les Leg Days
        for i in range(leg_days):
            used_exercises = set()  # Ensemble pour suivre les exercices déjà sélectionnés

            # Choisir 2 exercice différent  pour les hamstrings et je verifie si il n'est pas déjà utilisé
            hamstring_workout = random.sample([
                ex for ex in self.leg_workout.hamstring_exercice if ex not in used_exercises
            ],2)
            used_exercises.update(hamstring_workout)  # Ajouter l'exercice choisi aux utilisés

            # Choisir 2 exercice pour les quads et je verifie si il n'est pas déjà utilisé
            quad_workout = random.sample([
                ex for ex in self.leg_workout.quad_exercice if ex not in used_exercises
            ],2)
            used_exercises.update(quad_workout)

            # Choisir 2 exercice pour les glutes et je verifie si il n'est pas déjà utilisé
            glute_workout = random.sample([
                ex for ex in self.leg_workout.glute_exercices if ex not in used_exercises
            ],2)
            used_exercises.update(glute_workout)

            # Ajouter ce Leg Day au plan
            plan.append(f"Leg Day: Hamstrings: {hamstring_workout}, Quads: {quad_workout}, Glutes: {glute_workout}")

        # Générer les Upper Body Days (pas besoin de vérification ici car les exercices ne sont pas répété dans la liste d'exercices)
        for i in range(upper_days):
            shoulder_workout = random.sample(self.upper_body_workout.shoulder_exercise,2)
            tricep_workout = random.sample(self.upper_body_workout.tricep_exercise,2)
            bicep_workout = random.sample(self.upper_body_workout.biceps_exercise,2)
            chest_workout = random.sample(self.upper_body_workout.chest_exercise,2)
            plan.append(
                f"Upper Body Day: Shoulders: {shoulder_workout}, Triceps: {tricep_workout}, Biceps: {bicep_workout}, Chest: {chest_workout}")

        # Générer les Cardio Days
        for i in range(cardio_days):
            workout = random.choice(self.cardio_workout.cardio) #sélectionne aléatoirement l'exercice
            plan.append(f"Cardio Day: {workout} for at minimum 15 minutes")

        return plan

    def display_planner(self, plan): # cette méthode affiche le plan généré
        print("\nYour Weekly Workout Plan:")
        for day, workout in enumerate(plan, 1): # je parcour plan avec enumerate
            print(f"Day {day}: {workout}")


# Utilisation du générateur de plan
planner = WorkoutPlanner()

# Utilisation de la classe Goal pour récupérer l'objectif
goal = planner.goal.goal_display()  # Appel de la méthode de ta classe Goal


# Récupération des préférences de planification
leg_days, upper_days, cardio_days = planner.plan_preferences()
workout_plan = planner.generate_plan(leg_days, upper_days, cardio_days)

# Affichage du plan
planner.display_planner(workout_plan)
