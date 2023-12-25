import json
import sys

TERMINATORS = "br","jmp","ret"

JUMPS = 'br', 'jmp'

gp = {}


# make basic blocks
def form_blocks(body) :
    curr_block = []

    for instr in body :

        #if it's a operation
        if 'op' in instr :
            curr_block.append(instr)

            if instr['op'] in TERMINATORS :
                yield curr_block
                curr_block = []
        
        #it's a label
        else :
            if curr_block:
                yield curr_block
            curr_block = [instr]
    
    if curr_block:
        yield curr_block


#give name to each basic block
def name_blocks(list_Of_Blocks,block_no):
    for block in list_Of_Blocks :
        # print(block)
        if 'label' not in block[0] :
            b_name = 'bb' + str(block_no)
            block.insert(0,{'label' : b_name})
            block_no += 1 


    return list_Of_Blocks,block_no


# make succsor graph
def s_graph(list_Of_Blocks,s_g):

    prev_label = 'start'

    for block in list_Of_Blocks:
        # print("\n",block)

        label = block[0]['label']
        
        if prev_label not in s_g :
            s_g[prev_label] = []

        if label not in s_g :
            s_g[label] = []
            
        for instruc in block :
            if 'op' in instruc and instruc['op'] in JUMPS :
                for jmp_labels in instruc['labels'] :
                    s_g[label].append(jmp_labels)
        
        s_g[prev_label].append(label)
        prev_label = label

    # for key in s_g :
    #     print("\n {} : {} ".format(key,s_g[key]))
    # print(s_g)
    return s_g

# convert to hashmap
def conv_map(list_Of_Blocks):
    out = {}
    for block in list_Of_Blocks :
        out[block[0]["label"]] = block[1:];

    # print(out)
    return out

#cfg extractor in python
def mycfg():
    my_g = {}
    block_no = 0;
    prog = json.load(sys.stdin)
    list_Of_Blocks = []
    for func in prog['functions'] :
        for block in form_blocks(func['instrs']):
            list_Of_Blocks.append(block)

        list_Of_Blocks, block_no = name_blocks(list_Of_Blocks,block_no)

    my_g = s_graph(list_Of_Blocks,my_g)

    map_block = conv_map(list_Of_Blocks);
    
    print("digraph G {")
    for node in my_g :
        print(f"    \"{node}\";")
    for node in my_g :
        for dest in my_g[node]:
            print(f"    \"{node}\" -> \"{dest}\";")
    print("}")

# what is this ?
if __name__ == '__main__':
    mycfg()
