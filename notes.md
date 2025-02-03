### Questions:

## Thought Process

**Task 0:** 

Image size: 200x50x3?

1) Use libraries to generate necessary data.

For every word:

- One image of white background, black text, Arial font.
- 50 different fonts, for each font 5 images of different noise levels
- For each of the 50 images, generate one with green background and one that has a red background and is flipped text.


Hence for Task 1, we will have:

100 words * 250 images for each word = 100 * 250 = 25000 samples to train on.


**Task 1:**

Based off my previous experience trying to make a neural network for recognising handwritten digits, some points of the architecture I'm planning to use:

- 3 convolutional layers followed by an adaptive pooling layer and a fully connected layer.
- Cross-Entropy Loss
- Adam Optimizer with learning rate 0.001

I have 13k samples total, 10k to train and 2k to validate.
I am planning to run it for 20 epochs.


## Actual Implementation - Process

Changed image size to 250x100x3.
Used PIL to generate necessary data.

Changed image generation:

For every word:

- One image of white background, black text, Arial font.
- 21 different fonts, for each font 3 images of different noise levels, with 2 different capitalizations (each in a different colour)
- For each of the 132 images, generate one with green background and one that has a red background and is flipped text.

I now have a total of 13k images for training task 1.

Experienced very huge jumps in val_loss, I believe it's overfitting. Trying dropout layer with p=0.4

Still not helping, going to decrease learning rate and increase samples.
For each existing image I am going to have it in two different font sizes, basically doubling my samples. One of the fonts is too thin, getting noised out - going to remove that.

Also realised that I should have a test set as well, so now: 25k samples, 18k to train, 5k to val, 2k to test.

Increased epochs to 40, had consistent growth till 48%, with loss decreasing consistently.
Decided to let run for another 100 epochs.

# val/test swap
```
Epoch [1/100] Train Loss: 4.3877, Train Acc: 0.0314 || Val Loss: 4.0541, Val Acc: 0.0609
Checkpoint saved at epoch 1 with val_loss: 4.0541
Epoch [2/100] Train Loss: 3.9467, Train Acc: 0.0609 || Val Loss: 3.6711, Val Acc: 0.0831
Checkpoint saved at epoch 2 with val_loss: 3.6711
Epoch [3/100] Train Loss: 3.6316, Train Acc: 0.0690 || Val Loss: 3.4245, Val Acc: 0.0831
Checkpoint saved at epoch 3 with val_loss: 3.4245
Epoch [4/100] Train Loss: 3.4479, Train Acc: 0.0729 || Val Loss: 3.3141, Val Acc: 0.0863
Checkpoint saved at epoch 4 with val_loss: 3.3141
Epoch [5/100] Train Loss: 3.3407, Train Acc: 0.0796 || Val Loss: 3.2130, Val Acc: 0.0925
Checkpoint saved at epoch 5 with val_loss: 3.2130
Epoch [6/100] Train Loss: 3.2722, Train Acc: 0.0786 || Val Loss: 3.1583, Val Acc: 0.0991
Checkpoint saved at epoch 6 with val_loss: 3.1583
Epoch [7/100] Train Loss: 3.2284, Train Acc: 0.0872 || Val Loss: 3.1290, Val Acc: 0.1029
Checkpoint saved at epoch 7 with val_loss: 3.1290
Epoch [8/100] Train Loss: 3.1877, Train Acc: 0.0946 || Val Loss: 3.0913, Val Acc: 0.1105
Checkpoint saved at epoch 8 with val_loss: 3.0913
Epoch [9/100] Train Loss: 3.1553, Train Acc: 0.0998 || Val Loss: 3.0724, Val Acc: 0.1119
Checkpoint saved at epoch 9 with val_loss: 3.0724
Epoch [10/100] Train Loss: 3.1150, Train Acc: 0.1034 || Val Loss: 3.0395, Val Acc: 0.1235
Checkpoint saved at epoch 10 with val_loss: 3.0395
Epoch [11/100] Train Loss: 3.0815, Train Acc: 0.1119 || Val Loss: 2.9898, Val Acc: 0.1251
Checkpoint saved at epoch 11 with val_loss: 2.9898
Epoch [12/100] Train Loss: 3.0514, Train Acc: 0.1188 || Val Loss: 2.9748, Val Acc: 0.1291
Checkpoint saved at epoch 12 with val_loss: 2.9748
Epoch [13/100] Train Loss: 3.0084, Train Acc: 0.1255 || Val Loss: 2.9179, Val Acc: 0.1524
Checkpoint saved at epoch 13 with val_loss: 2.9179
Epoch [14/100] Train Loss: 2.9818, Train Acc: 0.1292 || Val Loss: 2.8873, Val Acc: 0.1648
Checkpoint saved at epoch 14 with val_loss: 2.8873
Epoch [15/100] Train Loss: 2.9467, Train Acc: 0.1364 || Val Loss: 2.8732, Val Acc: 0.1624
Checkpoint saved at epoch 15 with val_loss: 2.8732
Epoch [16/100] Train Loss: 2.9015, Train Acc: 0.1463 || Val Loss: 2.7913, Val Acc: 0.1758
Checkpoint saved at epoch 16 with val_loss: 2.7913
Epoch [17/100] Train Loss: 2.8715, Train Acc: 0.1541 || Val Loss: 2.7324, Val Acc: 0.1978
Checkpoint saved at epoch 17 with val_loss: 2.7324
Epoch [18/100] Train Loss: 2.8279, Train Acc: 0.1613 || Val Loss: 2.7133, Val Acc: 0.1998
Checkpoint saved at epoch 18 with val_loss: 2.7133
Epoch [19/100] Train Loss: 2.7851, Train Acc: 0.1763 || Val Loss: 2.6745, Val Acc: 0.2090
Checkpoint saved at epoch 19 with val_loss: 2.6745
Epoch [20/100] Train Loss: 2.7384, Train Acc: 0.1861 || Val Loss: 2.6271, Val Acc: 0.2236
Checkpoint saved at epoch 20 with val_loss: 2.6271
Epoch [21/100] Train Loss: 2.6993, Train Acc: 0.1928 || Val Loss: 2.5674, Val Acc: 0.2152
Checkpoint saved at epoch 21 with val_loss: 2.5674
Epoch [22/100] Train Loss: 2.6551, Train Acc: 0.2081 || Val Loss: 2.5630, Val Acc: 0.2232
Checkpoint saved at epoch 22 with val_loss: 2.5630
Epoch [23/100] Train Loss: 2.6137, Train Acc: 0.2168 || Val Loss: 2.6255, Val Acc: 0.2006
Epoch [24/100] Train Loss: 2.5786, Train Acc: 0.2263 || Val Loss: 2.4307, Val Acc: 0.2753
Checkpoint saved at epoch 24 with val_loss: 2.4307
Epoch [25/100] Train Loss: 2.5397, Train Acc: 0.2347 || Val Loss: 2.4746, Val Acc: 0.2527
Epoch [26/100] Train Loss: 2.4970, Train Acc: 0.2494 || Val Loss: 2.3458, Val Acc: 0.3119
Checkpoint saved at epoch 26 with val_loss: 2.3458
Epoch [27/100] Train Loss: 2.4513, Train Acc: 0.2551 || Val Loss: 2.3963, Val Acc: 0.2673
Epoch [28/100] Train Loss: 2.4138, Train Acc: 0.2765 || Val Loss: 2.2335, Val Acc: 0.3399
Checkpoint saved at epoch 28 with val_loss: 2.2335
Epoch [29/100] Train Loss: 2.3703, Train Acc: 0.2839 || Val Loss: 2.2185, Val Acc: 0.3457
Checkpoint saved at epoch 29 with val_loss: 2.2185
Epoch [30/100] Train Loss: 2.3295, Train Acc: 0.2981 || Val Loss: 2.1643, Val Acc: 0.3650
Checkpoint saved at epoch 30 with val_loss: 2.1643
Epoch [31/100] Train Loss: 2.2875, Train Acc: 0.3071 || Val Loss: 2.0879, Val Acc: 0.3940
Checkpoint saved at epoch 31 with val_loss: 2.0879
Epoch [32/100] Train Loss: 2.2468, Train Acc: 0.3193 || Val Loss: 2.0842, Val Acc: 0.4208
Checkpoint saved at epoch 32 with val_loss: 2.0842
Epoch [33/100] Train Loss: 2.1996, Train Acc: 0.3379 || Val Loss: 1.9828, Val Acc: 0.4314
Checkpoint saved at epoch 33 with val_loss: 1.9828
Epoch [34/100] Train Loss: 2.1630, Train Acc: 0.3469 || Val Loss: 1.9687, Val Acc: 0.4208
Checkpoint saved at epoch 34 with val_loss: 1.9687
Epoch [35/100] Train Loss: 2.1157, Train Acc: 0.3613 || Val Loss: 1.9103, Val Acc: 0.4390
Checkpoint saved at epoch 35 with val_loss: 1.9103
Epoch [36/100] Train Loss: 2.0731, Train Acc: 0.3785 || Val Loss: 1.8644, Val Acc: 0.4605
Checkpoint saved at epoch 36 with val_loss: 1.8644
Epoch [37/100] Train Loss: 2.0288, Train Acc: 0.3908 || Val Loss: 1.7882, Val Acc: 0.4989
Checkpoint saved at epoch 37 with val_loss: 1.7882
Epoch [38/100] Train Loss: 1.9882, Train Acc: 0.3976 || Val Loss: 1.8292, Val Acc: 0.4795
Epoch [39/100] Train Loss: 1.9490, Train Acc: 0.4132 || Val Loss: 1.6927, Val Acc: 0.5349
Checkpoint saved at epoch 39 with val_loss: 1.6927
Epoch [40/100] Train Loss: 1.9035, Train Acc: 0.4281 || Val Loss: 1.6694, Val Acc: 0.5447
Checkpoint saved at epoch 40 with val_loss: 1.6694
Epoch [41/100] Train Loss: 1.8621, Train Acc: 0.4410 || Val Loss: 1.6723, Val Acc: 0.5237
Epoch [42/100] Train Loss: 1.8273, Train Acc: 0.4502 || Val Loss: 1.5864, Val Acc: 0.5600
Checkpoint saved at epoch 42 with val_loss: 1.5864
Epoch [43/100] Train Loss: 1.7835, Train Acc: 0.4636 || Val Loss: 1.5659, Val Acc: 0.5646
Checkpoint saved at epoch 43 with val_loss: 1.5659
Epoch [44/100] Train Loss: 1.7398, Train Acc: 0.4807 || Val Loss: 1.5179, Val Acc: 0.5962
Checkpoint saved at epoch 44 with val_loss: 1.5179
Epoch [45/100] Train Loss: 1.7033, Train Acc: 0.4940 || Val Loss: 1.4596, Val Acc: 0.6232
Checkpoint saved at epoch 45 with val_loss: 1.4596
Epoch [46/100] Train Loss: 1.6641, Train Acc: 0.5069 || Val Loss: 1.4198, Val Acc: 0.6280
Checkpoint saved at epoch 46 with val_loss: 1.4198
Epoch [47/100] Train Loss: 1.6235, Train Acc: 0.5205 || Val Loss: 1.4112, Val Acc: 0.6030
Checkpoint saved at epoch 47 with val_loss: 1.4112
Epoch [48/100] Train Loss: 1.5911, Train Acc: 0.5237 || Val Loss: 1.3731, Val Acc: 0.6252
Checkpoint saved at epoch 48 with val_loss: 1.3731
Epoch [49/100] Train Loss: 1.5496, Train Acc: 0.5392 || Val Loss: 1.3421, Val Acc: 0.6288
Checkpoint saved at epoch 49 with val_loss: 1.3421
Epoch [50/100] Train Loss: 1.5210, Train Acc: 0.5497 || Val Loss: 1.2638, Val Acc: 0.6909
Checkpoint saved at epoch 50 with val_loss: 1.2638
Epoch [51/100] Train Loss: 1.4743, Train Acc: 0.5685 || Val Loss: 1.2530, Val Acc: 0.6921
Checkpoint saved at epoch 51 with val_loss: 1.2530
Epoch [52/100] Train Loss: 1.4425, Train Acc: 0.5762 || Val Loss: 1.1995, Val Acc: 0.6983
Checkpoint saved at epoch 52 with val_loss: 1.1995
Epoch [53/100] Train Loss: 1.4050, Train Acc: 0.5867 || Val Loss: 1.1859, Val Acc: 0.7051
Checkpoint saved at epoch 53 with val_loss: 1.1859
Epoch [54/100] Train Loss: 1.3766, Train Acc: 0.5993 || Val Loss: 1.2050, Val Acc: 0.6629
Epoch [55/100] Train Loss: 1.3365, Train Acc: 0.6092 || Val Loss: 1.1021, Val Acc: 0.7287
Checkpoint saved at epoch 55 with val_loss: 1.1021
Epoch [56/100] Train Loss: 1.3141, Train Acc: 0.6199 || Val Loss: 1.0889, Val Acc: 0.7161
Checkpoint saved at epoch 56 with val_loss: 1.0889
Epoch [57/100] Train Loss: 1.2753, Train Acc: 0.6259 || Val Loss: 1.0066, Val Acc: 0.7606
Checkpoint saved at epoch 57 with val_loss: 1.0066
Epoch [58/100] Train Loss: 1.2503, Train Acc: 0.6387 || Val Loss: 1.0011, Val Acc: 0.7550
Checkpoint saved at epoch 58 with val_loss: 1.0011
Epoch [59/100] Train Loss: 1.2201, Train Acc: 0.6439 || Val Loss: 1.0211, Val Acc: 0.7564
Epoch [60/100] Train Loss: 1.1892, Train Acc: 0.6536 || Val Loss: 0.9696, Val Acc: 0.7762
Checkpoint saved at epoch 60 with val_loss: 0.9696
Epoch [61/100] Train Loss: 1.1609, Train Acc: 0.6637 || Val Loss: 0.9391, Val Acc: 0.7708
Checkpoint saved at epoch 61 with val_loss: 0.9391
Epoch [62/100] Train Loss: 1.1323, Train Acc: 0.6716 || Val Loss: 0.9406, Val Acc: 0.7856
Epoch [63/100] Train Loss: 1.1079, Train Acc: 0.6835 || Val Loss: 0.8622, Val Acc: 0.7998
Checkpoint saved at epoch 63 with val_loss: 0.8622
Epoch [64/100] Train Loss: 1.0807, Train Acc: 0.6894 || Val Loss: 0.8380, Val Acc: 0.8028
Checkpoint saved at epoch 64 with val_loss: 0.8380
Epoch [65/100] Train Loss: 1.0634, Train Acc: 0.6912 || Val Loss: 0.7990, Val Acc: 0.8244
Checkpoint saved at epoch 65 with val_loss: 0.7990
Epoch [66/100] Train Loss: 1.0346, Train Acc: 0.7013 || Val Loss: 0.8070, Val Acc: 0.8150
Epoch [67/100] Train Loss: 1.0110, Train Acc: 0.7090 || Val Loss: 0.7596, Val Acc: 0.8366
Checkpoint saved at epoch 67 with val_loss: 0.7596
Epoch [68/100] Train Loss: 0.9921, Train Acc: 0.7153 || Val Loss: 0.7836, Val Acc: 0.8154
Epoch [72/100] Train Loss: 0.9111, Train Acc: 0.7379 || Val Loss: 0.7140, Val Acc: 0.8360
Checkpoint saved at epoch 72 with val_loss: 0.7140
Epoch [73/100] Train Loss: 0.8907, Train Acc: 0.7470 || Val Loss: 0.6631, Val Acc: 0.8643
Checkpoint saved at epoch 73 with val_loss: 0.6631
Epoch [74/100] Train Loss: 0.8591, Train Acc: 0.7565 || Val Loss: 0.6139, Val Acc: 0.8781
Checkpoint saved at epoch 74 with val_loss: 0.6139
Epoch [75/100] Train Loss: 0.8519, Train Acc: 0.7555 || Val Loss: 0.6151, Val Acc: 0.8693
Epoch [76/100] Train Loss: 0.8258, Train Acc: 0.7644 || Val Loss: 0.6283, Val Acc: 0.8677
Epoch [77/100] Train Loss: 0.8218, Train Acc: 0.7647 || Val Loss: 0.5867, Val Acc: 0.8773
Checkpoint saved at epoch 77 with val_loss: 0.5867
Epoch [78/100] Train Loss: 0.7930, Train Acc: 0.7754 || Val Loss: 0.5850, Val Acc: 0.8749
Checkpoint saved at epoch 78 with val_loss: 0.5850
Epoch [79/100] Train Loss: 0.7828, Train Acc: 0.7781 || Val Loss: 0.5713, Val Acc: 0.8805
Checkpoint saved at epoch 79 with val_loss: 0.5713
Epoch [80/100] Train Loss: 0.7611, Train Acc: 0.7813 || Val Loss: 0.5370, Val Acc: 0.8959
Checkpoint saved at epoch 80 with val_loss: 0.5370
Epoch [81/100] Train Loss: 0.7431, Train Acc: 0.7905 || Val Loss: 0.5409, Val Acc: 0.8907
Epoch [82/100] Train Loss: 0.7274, Train Acc: 0.7916 || Val Loss: 0.5213, Val Acc: 0.9005
Checkpoint saved at epoch 82 with val_loss: 0.5213
Epoch [83/100] Train Loss: 0.7108, Train Acc: 0.7976 || Val Loss: 0.5106, Val Acc: 0.8893
Checkpoint saved at epoch 83 with val_loss: 0.5106
Epoch [84/100] Train Loss: 0.6985, Train Acc: 0.8034 || Val Loss: 0.5429, Val Acc: 0.8819
Epoch [85/100] Train Loss: 0.6885, Train Acc: 0.8023 || Val Loss: 0.4772, Val Acc: 0.8973
Checkpoint saved at epoch 85 with val_loss: 0.4772
Epoch [86/100] Train Loss: 0.6704, Train Acc: 0.8104 || Val Loss: 0.4368, Val Acc: 0.9103
Checkpoint saved at epoch 86 with val_loss: 0.4368
Epoch [87/100] Train Loss: 0.6588, Train Acc: 0.8147 || Val Loss: 0.4689, Val Acc: 0.8983
Epoch [88/100] Train Loss: 0.6511, Train Acc: 0.8195 || Val Loss: 0.4518, Val Acc: 0.9105
Epoch [89/100] Train Loss: 0.6339, Train Acc: 0.8240 || Val Loss: 0.4407, Val Acc: 0.9125
Epoch [90/100] Train Loss: 0.6186, Train Acc: 0.8273 || Val Loss: 0.3954, Val Acc: 0.9257
Checkpoint saved at epoch 90 with val_loss: 0.3954
Epoch [91/100] Train Loss: 0.6068, Train Acc: 0.8328 || Val Loss: 0.4228, Val Acc: 0.9115
Epoch [92/100] Train Loss: 0.5916, Train Acc: 0.8333 || Val Loss: 0.4035, Val Acc: 0.9135
Epoch [93/100] Train Loss: 0.5813, Train Acc: 0.8369 || Val Loss: 0.4122, Val Acc: 0.9165
Epoch [94/100] Train Loss: 0.5765, Train Acc: 0.8402 || Val Loss: 0.3989, Val Acc: 0.9187
Epoch [95/100] Train Loss: 0.5577, Train Acc: 0.8441 || Val Loss: 0.3652, Val Acc: 0.9329
Checkpoint saved at epoch 95 with val_loss: 0.3652
Epoch [96/100] Train Loss: 0.5501, Train Acc: 0.8446 || Val Loss: 0.3789, Val Acc: 0.9223
Epoch [97/100] Train Loss: 0.5451, Train Acc: 0.8464 || Val Loss: 0.3576, Val Acc: 0.9339
Checkpoint saved at epoch 97 with val_loss: 0.3576
Epoch [98/100] Train Loss: 0.5247, Train Acc: 0.8504 || Val Loss: 0.3897, Val Acc: 0.9231
Epoch [99/100] Train Loss: 0.5168, Train Acc: 0.8548 || Val Loss: 0.3814, Val Acc: 0.9201
```