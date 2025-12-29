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

# Displays correctly entered digits 
def display_page_progress(page_start, correct_upto):
    print("\nEnter Pi Digits Below:") #header

    # digits already known on this page 
    known = PI[page_start:min(correct_upto, page_start + 50)]

    # prints full rows (of 10 digits)
    for i in range(0, len(known) // 10 * 10, 10):
        print(known[i:i+10])

    # prints partial row 
    remainder = len(known) % 10
    if remainder != 0:
        print(known[-remainder:] + "-" * (10 - remainder)) # prints remaining digits
    else:
        print("----------") 

# bold text to represent correct digits
BOLD = "\033[1m" 
RESET = "\033[0m"

# shows full page of 50 digits after mistake 
def print_full_page(page_start, correct_upto):
    print("\nCorrect full page:")
    # loops through rows of 10 
    for i in range(page_start, page_start + 50, 10):
        row = ""
        # bolds correct digits
        for j in range(i, i + 10):
            if j < correct_upto:
                row += BOLD + PI[j] + RESET
            else:
                row += PI[j]
        print(row)


# runs game 
def play_game(start_index):
    current_index = start_index

    while current_index < len(PI):
        page_start = (current_index // 50) * 50 # determines current page
        page_end = page_start + 50  

        print(f"\nCurrent digit: {current_index}")
        print(f"\nDigits: {page_start + 1}–{page_end}")
        display_page_progress(page_start, current_index)

        guess = input("Next digits: ") 

        if not guess.isdigit():
            print("Enter digits only.")
            continue

        for i, digit in enumerate(guess): # allows for input of more than 1 digit
            if current_index >= len(PI):
                return current_index

            correct_digit = PI[current_index]

            # game stops if wrong, and shows digit failed at, shows correct digit,
            # and prints full page with bold highlighting
            if digit != correct_digit: 
                failed_digit_number = current_index + 1

                print("\nWrong!")
                print(f"Failed at digit {failed_digit_number}")
                print(f"Correct digit was: {correct_digit}")

                print_full_page(page_start, current_index)
                return current_index    

            current_index += 1  # uf correct - move forward 1 digit at a time

    return current_index



def main():
    start_digit = int(input("Start at which digit? "))

    if start_digit < 0 or start_digit > len(PI):
        print("Invalid starting digit.")
        return

    # user knows everything up to and including start_digit
    start_index = start_digit

    final_index = play_game(start_index)

    print("\n Game over!")
    print(f"You reached digit {final_index}")
    print(f"Total digits correct this session: {final_index - start_digit}")


    
if __name__ == "__main__":
    main()
