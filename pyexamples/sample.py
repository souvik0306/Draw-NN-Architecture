
import sys
sys.path.append('../')
from tikzeng import *
# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input('cat.14.jpg', to='(-3,0,0)', width=8, height=8, name="temp" ),
    to_Conv("conv1", 14, 6, offset="(0,0,0)", to="(0,0,0)", height=28, depth=28, width=1,caption='conv1'),

    to_Conv("conv2", 10, 16, offset="(2,0,0)", height=20, depth=20, width=6,caption='conv2'),
    to_Conv("conv3", 5, 16, offset="(4,0,0)", height=10, depth=10, width=6,caption='conv3'),
    to_connection( "conv1", "conv2"),

    to_SoftMax("soft1", 400 ,"(8,0,0)", "(pool1-east)",  width=1.5, height=3, depth=60,opacity=0.6,caption="fc1" ),
    to_connection( "conv3", "soft1"),

    to_SoftMax("soft2", 120 ,"(9,0,0)", "(pool1-east)",  width=1.5, height=3, depth=30,opacity=0.6,caption="fc2" ),
    to_SoftMax("soft3", 84 ,"(10,0,0)", "(pool1-east)",  width=1.5, height=3, depth=21,opacity=0.6,caption="fc3" ),
    to_SoftMax("soft4", 10 ,"(11,0,0)", "(pool1-east)",  width=1.5, height=3, depth=10,opacity=0.6,caption="fc4" ),

    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
