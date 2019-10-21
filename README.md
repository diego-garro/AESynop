# Synoptic Module for Python 3

This is a module for evaluating of synoptic reports from meteorological land statios.

## Installation

...


## Group types clases

The reports contain diferent formats of groups, every format is described following:

### 1. ABCDD:

**Parameters:** group (string), file_error="" (string), synop_type="main" (string)

#### Section 1:
* iRixhVV

#### Section 3:
* 8NsChshs

### 2. ABBCC:

**Parameters:** group (string), file_error="" (string), synop_type="main" (string)

#### Section 1:
* Nddff
* 9ggGG

#### Section 2:
* 1PwaPwaHwaHwa
* 2PwPwHwHw
* 3dw1dw1dw2dw2
* 4Pw1Pw1Hw1Hw1
* 5Pw2Pw2Hw2Hw2

#### Section 3:
* 9SpSpspsp

### 3. ABCCC:

**Parameters:** group (string), file_error="" (string), synop_type="main" (string)

#### Section 1:
* 1snTTT
* 2snTdTdTd
* 5aPPP

#### Section 2:
* 0SsTwTwTw
* 8swTbTbTb

#### Section 3:
* 1snTxTxTx
* 2snTnTnTn
* 3Ejjj
* 4E'sss

### 4. ABBBB:

**Parameters:** group (string), file_error="" (string), synop_type="main" (string)

#### Section 1:
* 4PPPP
* 3PoPoPoPo

#### Section 3:
* 7R24R24R24R24

### 5. ABBBC:

**Parameters:** group (string), file_error="" (string), synop_type="main" (string)

#### Section 1:
* 6RRRtR

#### Section 3:
* 6RRRtR

### 6. ABBCD:

**Parameters:** group (string), file_error="" (string), synop_type="main" (string)

#### Section 1:
* 7wwW1W2

### 7. ABCDE:

**Parameters:** group (string), file_error="" (string), synop_type="main" (string)

#### Section 1:
* 8NhCLCMCH

#### Section 3:
* 0CsDLDMDH
* 5j1j2j3j4
* j5j6j7j8j9

### 8. AABBB:

**Parameters:** group (string), file_error="" (string), synop_type="main" (string)

#### Section 2:
* 70HwaHwaHwa

### 9. ABCCD:

**Parameters:** group (string), file_error="" (string), synop_type="main" (string)

#### Section 2:
* 6IsEsEsRs