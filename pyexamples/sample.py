
import sys
sys.path.append('../')
from tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 14, 6, offset="(0,0,0)", to="(0,0,0)", height=28, depth=28, width=1,caption=' input'),
    to_Conv("conv2", 10, 16, offset="(2,0,0)", height=20, depth=20, width=6),
    to_Conv("conv3", 5, 16, offset="(4,0,0)", height=10, depth=10, width=6),
    to_connection( "conv1", "conv2"),

    to_SoftMax("soft1", 400 ,"(7,0,0)", "(pool1-east)",  width=1.5, height=3, depth=60,caption="FC" ),
    to_connection( "conv3", "soft1"),

    to_SoftMax("soft1", 120 ,"(8,0,0)", "(pool1-east)",  width=1.5, height=3, depth=30,caption="FC" ),
    to_SoftMax("soft1", 84 ,"(9,0,0)", "(pool1-east)",  width=1.5, height=3, depth=21,caption="FC" ),
    to_SoftMax("soft1", 10 ,"(10,0,0)", "(pool1-east)",  width=1.5, height=3, depth=2,caption="FC" ),

    # to_Pool("pool1", offset="(6,0,0)",height=28, depth=28, width=6,caption=' pool 2' ),
    # to_connection( "conv3", "pool1"),
    # to_Conv("conv3", 10, 10, offset="(8,0,0)", height=20, depth=20, width=20),
    # to_Pool("pool2", offset="(10,0,0)",height=10, depth=10, width=10,caption=' pool 2',to="(pool2-east)" ),
    # to_connection( "conv3", "pool2"),
    # to_connection( "end", "pool2"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
