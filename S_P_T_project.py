# S = Scissors, T = Stone, P = Paper.
print("Start Game.")
print("Enter Your names. ")
user_1 = str(input("User 1 : ")).capitalize()
user_2 = str(input("User 2 : ")).capitalize()
print("S = Scissors,\nT = Stone,\nP = Paper.")
print("Enter Your actions.")
d_u_1 = 0
d_u_2 = 0
num_of_action = 0
while num_of_action < 10:
    if d_u_1 == 5:
        print(f"Finally {user_1} Win. Score {d_u_1} : {d_u_2}")
        exit()
    elif d_u_2 == 5:
        print(f"Finally {user_2} Win. Score {d_u_2} : {d_u_1}")
        exit()
    else:
        ac_u_1 = str(input(f"{user_1} : ")).capitalize()
        ac_u_2 = str(input(f"{user_2} : ")).capitalize()
        if ac_u_1 == 'S' and ac_u_2 == 'P':
            d_u_1 += 1
            print(
                f" >>> {user_1} win. \nScore {user_1} : {d_u_1} || {user_2} : {d_u_2}")
            num_of_action += 1
        elif ac_u_1 == 'S' and ac_u_2 == 'T':
            d_u_2 += 1
            print(
                f" >>> {user_2} win. \nScore {user_1} : {d_u_1} || {user_2} : {d_u_2}")
            num_of_action += 1
        elif ac_u_1 == 'T' and ac_u_2 == 'S':
            d_u_1 += 1
            print(
                f" >>> {user_1} win. \nScore {user_1} : {d_u_1} || {user_2} : {d_u_2}")
            num_of_action += 1
        elif ac_u_1 == 'T' and ac_u_2 == 'P':
            d_u_2 += 1
            print(
                f" >>> {user_2} win. \nScore {user_1} : {d_u_1} || {user_2} : {d_u_2}")
            num_of_action += 1
        elif ac_u_1 == 'P' and ac_u_2 == 'S':
            d_u_2 += 1
            print(
                f" >>> {user_2} win. \nScore {user_1} : {d_u_1} || {user_2} : {d_u_2}")
            num_of_action += 1
        elif ac_u_1 == 'P' and ac_u_2 == 'T':
            d_u_1 += 1
            print(
                f" >>> {user_1} win. \nScore {user_1} : {d_u_1} || {user_2} : {d_u_2}")
            num_of_action += 1
        elif ac_u_1 == ac_u_2:
            pass
        else:
            print("Wrong Value. ")
