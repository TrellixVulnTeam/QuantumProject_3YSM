# Copyright 2020 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

embeddings = {'SIMULATED_2000Q_CLOUD_TEST':
              {'a0': [431, 424, 175, 302, 168, 296],
               'a1': [148, 172, 156, 164],
               'a2': [417, 292, 289],
               'and0,1': [173, 165],
               'and0,2': [155, 167, 159],
               'and1,0': [171, 174],
               'and1,1': [152],
               'and1,2': [407, 415, 145, 273, 401],
               'and2,0': [303, 287, 295],
               'and2,1': [276, 284],
               'and2,2': [422, 419, 420],
               'b0': [169, 300, 297],
               'b1': [280, 162, 290, 286, 294],
               'b2': [160, 288, 416, 423],
               'carry1,0': [293, 291, 166, 163],
               'carry1,1': [400, 272, 144, 154, 149, 157],
               'carry2,0': [283, 285],
               'carry2,1': [275, 403, 406, 414],
               'carry3,0': [411, 412],
               'sum1,1': [281, 158, 153],
               'sum2,1': [282, 410]},
              'SIMULATED_2000Q_CLOUD_ALPHA':
              {'a0': [431, 424, 175, 302, 168, 296],
               'a1': [148, 172, 156, 164],
               'a2': [417, 292, 289],
               'and0,1': [173, 165],
               'and0,2': [155, 167, 159],
               'and1,0': [171, 174],
               'and1,1': [152],
               'and1,2': [407, 415, 145, 273, 401],
               'and2,0': [303, 287, 295],
               'and2,1': [276, 284],
               'and2,2': [422, 419, 420],
               'b0': [169, 300, 297],
               'b1': [280, 162, 290, 286, 294],
               'b2': [160, 288, 416, 423],
               'carry1,0': [293, 291, 166, 163],
               'carry1,1': [400, 272, 144, 154, 149, 157],
               'carry2,0': [283, 285],
               'carry2,1': [275, 403, 406, 414],
               'carry3,0': [411, 412],
               'sum1,1': [281, 158, 153],
               'sum2,1': [282, 410]},
              'DW_2000Q_5':
              {'and2,1': [2033, 1777, 1905],
               'sum1,1': [1772, 1770],
               'carry1,0': [1513, 1514, 1642, 1524, 1516],
               'and2,2': [1918, 1914, 1916],
               'a1': [1650, 1778],
               'and2,0': [1640, 1768, 1646],
               'and0,1': [1521, 1520, 1527],
               'a0': [1776, 1648],
               'and0,2': [1775, 1783, 1791],
               'carry2,1': [1904, 1908],
               'carry2,0': [1641, 1897, 1769],
               'sum2,1': [1901, 1907, 1909],
               'a2': [1774, 1782, 1790, 1658, 1786],
               'b0': [1662, 1654],
               'b1': [1649, 1661, 1657, 1653],
               'b2': [1780, 1787, 1915, 1788],
               'and1,2': [2043, 2045, 2037, 2034, 1906],
               'carry3,0': [1902, 1910],
               'and1,0': [1655, 1523, 1651],
               'and1,1': [1781, 1773, 1785, 1789],
               'carry1,1': [1898, 1784, 1903, 1912, 1919, 1911]},
              'DW_2000Q_6':
              {'and2,1': [590, 582, 450, 578],
               'sum1,1': [469, 464, 592, 720],
               'carry1,0': [727, 851, 723],
               'and2,2': [577, 449, 455, 448],
               'a1': [707, 711, 719], 'and2,0': [709, 717, 725],
               'and0,1': [854, 843, 846], 'a0': [585, 841, 713],
               'and0,2': [456, 597, 584, 589], 'carry2,1': [457, 454, 462],
               'carry2,0': [722, 594, 466], 'sum2,1': [452, 467, 468, 460],
               'a2': [710, 704, 576], 'b0': [840, 712, 718], 'b1': [706, 834, 842, 839, 847],
               'b2': [579, 583, 591], 'and1,2': [715, 587, 459], 'carry3,0': [471, 463],
               'and1,0': [835, 837, 853, 845], 'and1,1': [586, 724, 716, 714],
               'carry1,1': [458, 453, 461]},
              'BAY17_P16_ALPHA':
              {'a0': [566, 5042], 'b0': [521], 'b1': [506], 'and0,1': [5057], 'b2': [5041], 
               'and0,2': [416, 4922], 'a1': [5102, 431], 'and1,0': [536], 
               'a2': [445, 5117, 446], 'and2,0': [4952], 'and1,1': [5026], 'and2,1': [4996], 
               'carry1,0': [551, 4967], 'and1,2': [5056, 371], 'and2,2': [326, 5116], 
               'sum1,1': [401], 'carry1,1': [341, 5011], 'carry2,0': [4891, 430], 
               'sum2,1': [4981], 'carry2,1': [356], 'carry3,0': [386, 4966]},
              'BAY17_P16_TEST':
              {'a0': [566, 5042], 'b0': [521], 'b1': [506], 'and0,1': [5057], 'b2': [5041], 
               'and0,2': [416, 4922], 'a1': [5102, 431], 'and1,0': [536], 
               'a2': [445, 5117, 446], 'and2,0': [4952], 'and1,1': [5026], 'and2,1': [4996], 
               'carry1,0': [551, 4967], 'and1,2': [5056, 371], 'and2,2': [326, 5116], 
               'sum1,1': [401], 'carry1,1': [341, 5011], 'carry2,0': [4891, 430], 
               'sum2,1': [4981], 'carry2,1': [356], 'carry3,0': [386, 4966]}
              }

