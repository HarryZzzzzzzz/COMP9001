import random
def main():
     print("🎮 Welcome to the Life Simulation Game: 'Truths of Life' 🎮\n")
     name = input('Enter your character\'s name: ')
     gender = random.choice(["Male", "Female"])
     print(f"\n{name}'s gender is randomly assigned as: {gender}")
     
     while True:
        change = input("Would you like to change the gender? (yes/no): ").lower()
        if change in ("yes", "no"):
          break
        print("Please enter 'yes' or 'no'.")
     if change.lower() == "yes":
          print("Regardless of gender, it's the greatest gift life has given you. It's destiny. You have no right to choose your gender.")

     print("\n🌱 Early Life Stage:")
     life = 100
     strength = 10
     intelligence = 10
     talent = 0
     love = 0

     while True:
        education_mode = input("Choose your education path ('experiential' / 'exam-oriented'): ").lower()
        if education_mode in ('experiential', 'exam-oriented'):
          break
        print("Please enter 'experiential' or 'exam-oriented'.")
     life -= 20

     if education_mode == "experiential":
          talent = 1
          strength += 5
          intelligence += 3
     elif education_mode == "exam-oriented":
          strength -= 3
          intelligence += 5

     print(f"\nCurrent status -> Life: {life}, Strength: {strength}, Intelligence: {intelligence}, Talent: {talent}")

     print("\n🔬 Question 2: Do you want to explore unknown human knowledge?")
     while True:
          research = input("Do you want to try researching? (yes/no): ").lower()
          if research not in ("yes", "no"):
               print ('Please enter yes or no.')
               return
          if research == "no":
               break
          strength -= 1
          if education_mode == "experiential":
               if random.randint(1, 10) == 1:
                    print("🎉 Congratulations! You discovered unknown human knowledge!")
                    break
          if education_mode == "exam-oriented":
               if strength <= 0:
                    print("\n💀 Hard work is important, but that rare 1% of talent is what truly brings success.")
                    print("A life shaped only by exams loses the ability to feel the world, and thus, the courage and curiosity to explore it.")
                    print("May your next life be one where you roam freely in this bittersweet world.")
                    return
          elif strength <= 0:
               print("\n💀 Congratulations! You found your life's goal and pursued it with all your might.")
               print("Though the result was failure, perhaps that too is a form of success.")
               print("May your next life be full of richer experiences. Sometimes, there's nothing difficult in this world, if you're willing to give up.")
               return

     life -= 20
     
     while True:
          marry = input("\n👰 At age 30, do you want to get married? (yes/no): ").lower()
          if marry in ('yes','no'):
               break
          print('Plesae enter yes. or no.')
     if marry == "yes":
          love = 1

     child = "no"
     if marry == "yes":
          child = input("Do you want to have children? (yes/no): ").lower()
          if child not in ('yes','no'):
               print('Please enter yes or no.')
               return
          if child == "yes":
               strength -= 5

     print("\n👪 Age 50: Your parents are nearing the end of their lives.")
     life -= 20
     save_parents = input("Would you give up 20 years of your life for your parents to live 10 more years? (yes/no): ").lower()
     if save_parents not in ('yes','no'):
               print('Please enter yes or no.')
               return
     if save_parents == "yes":
          life -= 20
          if random.choice([True, False]):
               print("\n💔 Your spouse has fallen seriously ill.")
               print("Because you were willing to give up your life for your parents, it is only expected that you'd do the same for your spouse.")
               life -= 20
          if life <= 0:
               print("\n💀 Loving your parents and spouse is noble, but true love is shown while they're still alive.")
               print("Love yourself first, then love them—not by sacrificing yourself, but by cherishing every moment.")
               print("Let go when life says it's time. Love them when they live, and have no regrets when they leave.")
               print("Now you no longer have enough life left to remain in this world. As your white-haired parents and spouse hold your lifeless body and weep, whispering 'we're sorry'—how do you feel?")
               return

     if child == "yes" and save_parents == "yes":
          accept_kid_sacrifice = input("You're dying. Your child is willing to give up 20 years of their life to give you 10 more. Do you accept? (yes/no): ").lower()
          life -= 40
          print("\n👶 Your child, just like you once were, loves you deeply.")
          print("They want to keep you close even if it costs them their life.")
          print("Now your child is 80 as you, white-haired, sitting beside you.")
          print("Are you truly happy to still be here watching them grow old?")
          return
     elif child == "no" and save_parents == "yes":
          life -= 20
          regret = input("You're 80 and fall mildly ill. You could have lived 20 more years but your life has run out. Do you regret it? (yes/no): ").lower()
          if regret == "yes":
               life -= 40
               print("\n💀 Congratulations on realizing, even at 80, that you are the most important person in your life.")
               print("Sadly, you have no more time. May your next life be one where you prioritize yourself.")
          else:
               life -= 40
               print("\n💀 You dream of your long-departed parents. Their eyes are full of tears, lips moving silently.")
               print("You couldn't hear them, but you feel they were saying: 'Child, we are sorry.'")
          if life <= 0:
               print_death_message()
          return
     elif child == "yes" and save_parents == "no":
          life -= 40
          regret_kid = input("You fell mildly ill but your child didn't come to care for you. Do you regret having children? (yes/no): ").lower()
          if regret_kid == "yes":
               print("\n💬 Children are not your possessions. They come through you, but they do not belong to you.")
               print("May your next life bring clarity—that children are born from love, not obligation.")
          else:
               print("\n💬 You've truly understood the meaning of parenthood. They come through you, but they do not belong to you.")
          if life <= 0:
               print_death_message()
          return
     elif child == "no" and save_parents == "no":
          life -= 40
          regret_no_kid = input("You are in the hospital, sick but not seriously. You see other elders with kids caring for them. Do you regret not having kids? (yes/no): ").lower()
          if regret_no_kid == "yes":
               print("\n💬 Children are not your possessions. They come through you, but they do not belong to you.")
          else:
               print("\n💬 You've truly respected and accepted your choices. Whatever comes next, you'll live freely.")
          if life <= 0:
               print_death_message()
          return

def print_death_message():
    print("💀 You've reached the end of your life. Every choice you made led you here.")
    print("Whether or not you achieved greatness or happiness, you walked your own path bravely.")
    print("Rest now, knowing this life was lived with intention.")

if __name__ == "__main__":
    main()
