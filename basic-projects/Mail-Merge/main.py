PLACEHOLDER = "[name]"


with open("Input/Letters/starting_letter.txt") as starting_letter:
    with open("Input/Names/invited_names.txt") as invited_names:
        base_letter = starting_letter.read()
        inv_list = invited_names.readlines()
        base_letter_name = "letter_for_"
        for name in inv_list:
            name = name.strip()
            letter_name = base_letter_name + name
            letter_res = base_letter.replace(PLACEHOLDER, name)
            with open(f"Output/ReadyToSend/{letter_name}.txt", "w") as res_file:
                res_file.write(letter_res)
