
def get_valid_number():
    while True:
        try:
            num = int(input("Enter a number between 3 and 9: "))
            if 3 <= num <= 9:
                return num
            else:
                print("Invalid input. Please enter a number between 3 and 9.")
        except ValueError:
            print("Invalid input. Please enter a whole number between 3 and 9.")


def generate_personal_code(student_id, keyword):
    first = keyword[0].upper()
    last  = keyword[-1].upper()
    return f"{first}-{student_id}-{last}"

def count_character_frequency(name):
    freq = {}
    for ch in name.lower():
        if ch == ' ':       
            continue
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


def find_unique_vowels_consonants(text):
    vowels_set     = set()
    consonants_set = set()
    vowel_letters  = set("aeiou")

    for ch in text.lower():
        if ch.isalpha():
            if ch in vowel_letters:
                vowels_set.add(ch)
            else:
                consonants_set.add(ch)

    return sorted(vowels_set), sorted(consonants_set)

def check_balanced_brackets(expression):
    stack        = []                        
    matching     = {')': '(', ']': '[', '}': '{'}
    opening      = set('([{')
    closing      = set(')]}')

    for ch in expression:
        if ch in opening:
            stack.append(ch)                 
        elif ch in closing:
            if not stack:                     
                return False
            if stack[-1] != matching[ch]:      
                return False
            stack.pop()                        

    return len(stack) == 0                    


def process_keyword_queue(keyword):
    queue = [] 

    for ch in keyword:
        queue.append(f"Analyse {ch}")

    print("\nQueue Processing:")
    while queue:
        task = queue.pop(0)
        print(f"  Processing: {task}")


def print_number_pattern(number):
    print("\nNumber Pattern:")
    for i in range(1, number + 1):
        print(" ".join(str(j) for j in range(1, i + 1)))


def recursive_digit_sum(student_id):
    if len(student_id) == 0:        # base case
        return 0
    return int(student_id[0]) + recursive_digit_sum(student_id[1:])


def display_summary(student_id, full_name, keyword, number,
                    bracket_expr, personal_code,
                    char_freq, vowels, consonants,
                    balanced, digit_sum):

    print("\n" + "=" * 50)
    print("           RESULTS SUMMARY")
    print("=" * 50)

    
    print(f"\nPersonal Code: {personal_code}")

    
    print("\nCharacter Frequency:")
    for ch, count in char_freq.items():
        print(f"  {ch} : {count}")

   
    print(f"\nUnique Vowels     : {', '.join(vowels)}")
    print(f"Unique Consonants : {', '.join(consonants)}")

   
    result = "Yes" if balanced else "No"
    print(f"\nBalanced Brackets : {result}")

    
    print(f"\nRecursive Digit Sum of Student ID ({student_id}): {digit_sum}")

    print("\n" + "=" * 50)



def main():
    print("=" * 50)
    print("     Personal Pattern Toolkit (CSF 101)")
    print("=" * 50)


    student_id   = input("\nEnter Student ID   : ").strip()
    full_name    = input("Enter Full Name    : ").strip()
    keyword      = input("Enter Keyword      : ").strip()
    number       = get_valid_number()                          # Task 1 validation
    bracket_expr = input("Enter bracket expression: ").strip()


    personal_code = generate_personal_code(student_id, keyword)


    char_freq = count_character_frequency(full_name)


    combined_text      = full_name + " " + keyword
    vowels, consonants = find_unique_vowels_consonants(combined_text)

    
    balanced = check_balanced_brackets(bracket_expr)


    digit_sum = recursive_digit_sum(student_id)


    display_summary(
        student_id, full_name, keyword, number,
        bracket_expr, personal_code,
        char_freq, vowels, consonants,
        balanced, digit_sum
    )

    
    process_keyword_queue(keyword)

    
    print_number_pattern(number)

    print("\n[Program Complete]")


if __name__ == "__main__":
    main()