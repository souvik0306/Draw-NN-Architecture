
import sys
sys.path.append('../')
from tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 32, 3, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=1,caption=' input'),
    # to_connection( "conv2", "conv1"),
    to_Conv("conv2", 28, 6, offset="(3,0,0)", height=56, depth=56, width=6),
    to_connection( "pool1", "conv2"),
    to_Pool("pool1", offset="(6,0,0)",height=28, depth=28, width=6,caption=' pool 2' ),
    # to_connection( "conv3", "pool1"),
    to_Conv("conv3", 10, 10, offset="(9,0,0)", height=20, depth=20, width=20),
    to_Pool("pool2", offset="(14,0,0)",height=10, depth=10, width=10,caption=' pool 2',to="(pool2-east)" ),
    to_connection( "conv3", "pool2"),
    # to_connection( "end", "pool2"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
