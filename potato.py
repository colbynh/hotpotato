import random
from dlList import DubLinkList


def get_rand_sequence(intSeed, lSize):
    random.seed(intSeed)
    myList = []
    curSize = lSize
    for i in range(1, lSize):
        start = (-2 * curSize)
        end = (2 * curSize)
        rInt = random.randint(start, end)
        curSize -= 1
        myList.append(rInt)

    return myList

def init_dll(data):
    llist = DubLinkList()
    llist.addNode_in_emptylist(data[0])
    for i in range(1, len(data)):
        llist.insert_node_end(data[i])
    return llist

def play_round(dll, move, actual_moves, cursor):
    total_moves = abs(move)
    # set cursor
    print("The music starts (%s): " % (move), end="")
    if move > 0:
        return handle_pos_move(dll, cursor, total_moves, actual_moves)
    elif move < 0:
        return handle_neg_move(dll, cursor, total_moves, actual_moves)
    else:
        return handle_neutral_move(dll, cursor)
    
def handle_pos_move(dll, cursor, total_moves, actual_moves):
    cur_node = cursor
    print(cur_node.item + "-> ", end = '')

    for m in range (1, total_moves):
        if cur_node.nRef == None:
            cur_node = dll.start_node
            print(cur_node.item + "-> ", end = "")
        print(cur_node.nRef.item + "-> ", end = "")
        cur_node = cur_node.nRef  
    print("is stuck holding the potato!")
    dll.handle_delete(cur_node, actual_moves)
    if cur_node.nRef != None:
        cursor = cur_node.nRef
    else: 
        cursor.pRef = None
        cursor = dll.start_node
    
    return cursor

def handle_neg_move(dll, cursor, total_moves, actual_moves):
    cur_node = cursor
    print(cur_node.item + "-> ", end = '')
    for m in range (0, total_moves):
        if cur_node.pRef == None:
            cur_node = dll.end_node
            print(cur_node.item + "-> ", end = "")
            continue
        else: 
            cur_node = cur_node.pRef
            print(cur_node.item + "-> ", end = "")
    cursor = cur_node.nRef
    print("is stuck holding the potato")
    dll.handle_delete(cur_node, actual_moves)

    if cur_node.pRef != None:
        cursor = cur_node.nRef
    else: 
        cursor = dll.end_node
    return cursor

def handle_neutral_move(dll, cursor):
    cur_node = cursor
    print(cur_node.item)
    if cursor.nRef != None:
        cursor = cursor.nRef
    else: 
        cursor = dll.start_node
    if cur_node.nRef == None:
        cursor = dll.start_node
    else:
        cursor = cur_node.nRef
    print(cur_node.item + " is stuck holding the potato!")
    dll.handle_delete(cur_node, 0)
    return cursor

def main():
    players = ["Aaron", "Beth", "Cathy", "Duncan", "Emery"]
    round_moves = get_rand_sequence(10, 5)
    dll = init_dll(players)
    cursor = dll.start_node
    cur_move = 1
    
    for move in round_moves:
        actual_moves = abs(move) - (dll.get_size()) 
        cursor = play_round(dll, move, actual_moves, cursor)
    print(dll.start_node.item + " is the winner!")

if __name__ == '__main__':
    main()