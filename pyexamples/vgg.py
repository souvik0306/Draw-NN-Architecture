
import sys
sys.path.append('../')
from tikzeng import *
# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input('cat.14.jpg', to='(-3,0,0)', width=8, height=10, name= "temp"),
    to_Conv("conv1", 224, 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=28, width=1,caption='c1'),
    to_Conv("conv2", 224, 64, offset="(1,0,0)", to="(0,0,0)", height=64, depth=28, width=1,caption='c2'),
    
    to_Pool("pool1",offset="(3,0,0)",height=32, depth=28, width=4,caption='p1' ),
    to_Conv("conv1", 112, 128, offset="(4,0,0)", to="(0,0,0)", height=32, depth=28, width=3,caption='c3'),
    to_Conv("conv2", 112, 128, offset="(5,0,0)", to="(0,0,0)", height=32, depth=28, width=3,caption='c4'),
  
 
    to_Pool("pool1",offset="(7,0,0)",height=16, depth=14, width=6,caption='p2' ),
    to_Conv("conv1", 56, 256, offset="(8,0,0)", to="(0,0,0)", height=16, depth=14, width=5,caption='c5'),
    to_Conv("conv2", 56, 256, offset="(9,0,0)", to="(0,0,0)", height=16, depth=14, width=5,caption='c6'),
  
  
    to_Pool("pool1",offset="(11,0,0)",height=8, depth=7, width=7,caption='p2' ),
    to_Conv("conv1", 28, 512, offset="(13,0,0)", to="(0,0,0)",height=8, depth=7, width=5,caption='c7'),
    to_Conv("conv2", 28, 512, offset="(14.5,0,0)", to="(0,0,0)",height=8, depth=7, width=5,caption='c8'),
    to_Conv("conv2", 28, 512, offset="(16,0,0)", to="(0,0,0)",height=8, depth=7, width=5,caption='c9'),

    to_Conv("conv1", 14, 512, offset="(17.5,0,0)", to="(0,0,0)",height=4, depth=7, width=6,caption='c10'),
    to_Conv("conv2", 14, 512, offset="(19,0,0)", to="(0,0,0)",height=4, depth=7, width=6,caption='c11'),
    to_Conv("conv2", 14, 512, offset="(20.5,0,0)", to="(0,0,0)",height=4, depth=7, width=6,caption='c12'),
    to_Pool("pool1",offset="(22,0,0)",height=3, depth=5, width=5,caption='p3' ),

    to_Conv("conv2", 1, 4096, offset="(23.5,0,0)", height=2, depth=3, width=9,caption='fc1'),
    to_Conv("conv3", 1, 4096, offset="(25.5,0,0)", height=2, depth=3, width=9,caption='fc2'),

    to_SoftMax("soft1", 1000 ,"(27.8,0,0)",  width=4, height=2, depth=2,opacity=0.6,caption="softmax" ),
    # to_ConvConvRelu( 'name', 56, n_filer=(64,64), offset="(30,0,0)", to="(0,0,0)", width=(2,2), height=2, depth=2, caption="e " ),

    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
