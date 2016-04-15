#   Copyright (c) 2016, Xilinx, Inc.
#   All rights reserved.
# 
#   Redistribution and use in source and binary forms, with or without 
#   modification, are permitted provided that the following conditions are met:
#
#   1.  Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#
#   2.  Redistributions in binary form must reproduce the above copyright 
#       notice, this list of conditions and the following disclaimer in the 
#       documentation and/or other materials provided with the distribution.
#
#   3.  Neither the name of the copyright holder nor the names of its 
#       contributors may be used to endorse or promote products derived from 
#       this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
#   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
#   PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION). HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__author__      = "Naveen Purushotham, Yun Rock Qu"
__copyright__   = "Copyright 2016, Xilinx"
__email__       = "xpp_support@xilinx.com"


import pytest
from pynq import Overlay
from pynq.pmods.pmod_als import PMOD_ALS
from pynq.test.util import user_answer_yes

flag = user_answer_yes("\nALS attached to the board?")
if flag:
    global als_id
    als_id = int(input("Type in the PMOD ID of the ALS (1 ~ 4): "))

@pytest.mark.run(order=28)  
@pytest.mark.skipif(not flag, reason="need ALS attached in order to run")
def test_readlight():
    """Test for the ALS class.
    
    This test reads the ALS and asks the user to dim light manually. Then
    verify that a lower reading is displayed.
    
    """
    global als
    als = PMOD_ALS(als_id)
    
    n = als.read()
    print("\nCurrent ALS reading: {}.".format(n))
    assert user_answer_yes("Is a reading between 0-255 displayed?")
    input("Dim light by placing palm over the ALS and hit enter...")
    n = als.read()
    print("Current ALS reading: {}.".format(n))
    assert user_answer_yes("Is a lower reading displayed?")
    
    del als