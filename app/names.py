from random import shuffle

sample_names = '''Alyvia Rush
Annabelle Clarke
Annie Hooper
Ashlynn Winters
Aurora Tyler
Axel Sharp
Barrett Webb
Batman
Benjamin Weiss
Bo Ball
Caitlin Page
Cesar Becker
Colt Schultz
Dario Dunlap
Darnell Andersen
Dayana Ortiz
Dexter Fischer
Dominic Petersen
Donald Duck
Eden Murphy
Elena Burns
Gabriela Shannon
Gaige Parrish
Giuliana Boyle
Glenn Price
Grogu
Hailey Drake
Heisenberg
Hugh Franco
Ivy Page
Jaiden Salinas
Jaquan Solomon
Jaycee Woodward
Jaylen Murphy
Johanna Schroeder
Joselyn Riddle
Kaitlin Cabrera
Kaleigh Giles
Kayden Gillespie
Khloe Madden
Kid Dynomite
Krish Anderson
Lando
Laura Good
Layla Dawson
Luciano Young
Lukas Mclean
Maddison Walter
Maria Zhang
Marquis Cervantes
Martin Kirby
Mary Poppins
Maximo Simon
Maximus Hutchinson
Melina Sutton
Michael Maddox
Myles Noble
Nasir Randolph
Neil Maxwell
Noemi Weaver
Nolan Fitzgerald
Quinten Hardin
Ray Mccormick
Road Runner
Ryann Trujillo
Sam Atkins
Samantha Ward
Sheldon Cooper
Taniyah Waters
The Fonz
Wile E. Coyote
Worf'''.split('\n')

def random_names(num_names: int) -> str:
    shuffle(sample_names)
    return '\n'.join(sample_names[:num_names])
