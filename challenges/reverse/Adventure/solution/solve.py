map=[['D', '•', '•', '•', '•', 'X', '•', '•', 'X', '•'], ['•', '•', '•', '•', '•', '•', 'X', '•', 'X', 'X'], ['X', 'X', 'X', '•', '•', '•', 'X', '•', '•', '•'], ['X', '•', '•', '•', 'X', 'X', '•', 'X', '•', 'X'], ['•', '•', '•', '•', '•', '•', 'X', '•', 'X', 'X'], ['•', '•', '•', '•', '•', '•', '•', 'X', '•', '•'], ['•', 'X', '•', 'X', 'X', '•', 'X', '•', 'X', '•'], ['X', 'X', '•', '•', '•', 'X', '•', '•', '•', 'X'], ['•', 'X', 'X', '•', '•', 'X', 'X', '•', '•', 'X'], ['•', 'X', '•', '•', 'X', '•', 'X', '•', '•', 'E']]

moves=['D', 'D', 'D', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'D', 'D', 'R', 'D', 'D', 'R', 'D', 'R']
backpack="ui3g{FTC2CSIs1}_9n1kc1p_hAiaib35uqom_UQV4Dv3n7Ur3"

player_x, player_y = 9, 9

def reverse_move_right(backpack):
    k = len(backpack) // 4
    return backpack[-k:] + backpack[:-k][::-1]

def reverse_move_down(backpack):
    k = len(backpack) // 2
    return backpack[-k:][::-1] + backpack[:-k]

def reverse_transformation(backpack, moves):
    global player_x, player_y
    for move in reversed(moves):
        if move == 'D':
            backpack = reverse_move_down(backpack)
            if map[player_y][player_x] == 'X':
                backpack = backpack[1:-1]
            player_y -= 1
        elif move == 'R':
            backpack = reverse_move_right(backpack)
            if map[player_y][player_x] == 'X':
                backpack = backpack[1:-1]
            player_x -= 1
    return backpack

original_backpack = reverse_transformation(backpack.encode(), moves)
print(f'flag: {original_backpack.decode()}')
