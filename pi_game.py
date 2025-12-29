import json
import os 

pi_pages = [
    "31415926535897932384626433832795028841971693993751",
    "05820974944592307816406286208998628034825342117067",
    "98214808651328230664709384460955058223172535940812",
    "84811174502841027019385211055596446229489549303819",
    "64428810975665933446128475648233786783165271201909",
    "14564856692346034861045432664821339360726024914127",
    "37245870066063155881748815209209628292540917153643",
    "67892590360011330530548820466521384146951941511609",
    "43305727036575959195309218611738193261179310511854",
    "80744623799627495673518857527248912279381830119491",
]

PI = "".join(pi_pages)

def load_stats():
    """Load statistics from file if it exists, otherwise return defaults"""
    if os.path.exists("pi_stats.json"):
        with open("pi_stats.json", 'r') as f:
            return json.load(f)
    return {"personal_best": 0}
    
def save_stats(stats):
    """Save statistics to file"""
    with open("pi_stats.json", 'w') as f:
        json.dump(stats, f, indent=2)  

def display_page_progress(page_start, correct_upto):
    print("\nEnter Pi Digits Below:")

    known = PI[page_start:min(correct_upto, page_start + 50)]

    for i in range(0, len(known) // 10 * 10, 10):
        print(known[i:i+10])

    remainder = len(known) % 10
    if remainder != 0:
        print(known[-remainder:] + "-" * (10 - remainder))
    else:
        print("----------") 

BOLD = "\033[1m" 
RESET = "\033[0m"

def print_full_page(page_start, correct_upto):
    print("\nCorrect full page:")
    for i in range(page_start, page_start + 50, 10):
        row = ""
        for j in range(i, i + 10):
            if j < correct_upto:
                row += BOLD + PI[j] + RESET
            else:
                row += PI[j]
        print(row)

def play_game(start_index):
    current_index = start_index
    session_correct = 0

    while current_index < len(PI):
        page_start = (current_index // 50) * 50
        page_end = page_start + 50  

        print(f"\nCurrent digit: {current_index}")
        print(f"\nDigits: {page_start + 1}–{page_end}")
        display_page_progress(page_start, current_index)

        guess = input("Next digits: ") 

        if not guess.isdigit():
            print("Enter digits only.")
            continue

        for i, digit in enumerate(guess):
            if current_index >= len(PI):
                return current_index, session_correct

            correct_digit = PI[current_index]

            if digit != correct_digit: 
                failed_digit_number = current_index + 1

                print("\nWrong!")
                print(f"Failed at digit {failed_digit_number}")
                print(f"Correct digit was: {correct_digit}")

                print_full_page(page_start, current_index)
                return current_index, session_correct 

            current_index += 1
            session_correct += 1
            print(f"Session correct: {session_correct}", end="\r")

    return current_index, session_correct

def main():
    stats = load_stats() 
    
    start_digit = int(input("\nStart after which digit? "))

    if start_digit < 0 or start_digit > len(PI):
        print("Invalid starting digit.")
        return

    start_index = start_digit
    final_index, session_correct = play_game(start_index)

    print("\nGame over!")
    print(f"You reached digit {final_index}")
    print(f"Total digits correct this session: {session_correct}")
    
    if session_correct > stats["personal_best"]:
        stats["personal_best"] = session_correct
        print("\nNEW PERSONAL BEST!")

    save_stats(stats)
    
    print(f"Personal best: {stats['personal_best']} total correct digits")
    
if __name__ == "__main__":
    main()
