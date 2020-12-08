print("Welcome to Word_Find")
main = {
        'Appriciate':'To make someone willing to do.',
        'Invade':'Attack.',
        'Audacity':'Daring.',
        'Merriment':'Happiness.',
        'Dof':'Stupid.',
        'August':'Respectfull,Impressive.',
        'Profiletric':'Duration.',
        'Acrimonious':'Angry,Rudly.',
        'Bling':'Decorative.',
        'Abysmal':'Extremely bad.',
        'Articulate':'Clearly express in words.',
        'Miserable':'Unhappy.',
        'Admire':'Respect.',
        'Solitary':'Alone.',
        'Vengeance':'Revenge.',
        'Awful':'Unpleasent.',
        'Blunder':'Unexpected.',
        'Hellacious':'Bad experience.',
        'Hailstorm':'Heavy rains.',
        'Mug up':'Remembring.',
        'Petrified':'Scared.',
        'Clung':'Hold tightly.',
        'Grave':'Very serious.',
        'Keen':'Abate.',
        'Abate':'Become less in amount.',
        'Empathy':"Understanding someone's feeling.",
        'Opulent':'Superior in quality.',
        'Orator':'Person delevering a speech.'       
    }
need = input("Enter the word here: ")
if need in main:
    print("Meaning of",need,"is",main[need])
else:
    print("No word found as",need)

word = input("Enter the word here: ")
meaning = input("Enter the meaning here: ")