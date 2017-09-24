def main():
	MSTORE(0x40, 0x60)
	var1 = CALLDATASIZE()
	var2 = ISZERO(var1)
	if var2: func1()
	var3 = CALLDATALOAD(00)
	var4 = var3 // 0x100000000000000000000000000000000000000000000000000000000
	var5 = var4 == 0x41c0e1b5
	if var5: func2()
	var6 = 0xf3fef3a3 == var4
	if var6: func3()

def func1():
	var7 = MLOAD(0x40)
	var8 = CALLER()
	var9 = 0xffffffffffffffffffffffffffffffffffffffff & var8
	MSTORE(var7, var9)
	var10 = CALLVALUE()
	var11 = var7 + 0x20
	MSTORE(var11, var10)
	var12 = MLOAD(0x40)
	var13 = var7 - var12
	var14 = var13 + 0x40
	LOG1(var12, var14, 0xe841da81d6a9283cfb7d2ae1dbeb8bca7a33a7aee241abae36d4c810d25ab448)
	func4()

def func2():
	var15 = CALLVALUE()
	if var15: THROW()
	var16 = SLOAD(00)
	var17 = 0xffffffffffffffffffffffffffffffffffffffff & var16
	var18 = CALLER()
	var19 = var18 & 0xffffffffffffffffffffffffffffffffffffffff
	var20 = var19 == var17
	var21 = ISZERO(var20)
	if var21: THROW()
	var22 = SLOAD(00)
	var23 = 0xffffffffffffffffffffffffffffffffffffffff & var22
	SUICIDE(var23)

def func3():
	var24 = CALLVALUE()
	if var24: THROW()
	var25 = CALLDATALOAD(0x04)
	var26 = CALLDATALOAD(0x24)
	var27 = SLOAD(00)
	var28 = 0xffffffffffffffffffffffffffffffffffffffff & var27
	var29 = CALLER()
	var30 = var29 & 0xffffffffffffffffffffffffffffffffffffffff
	var31 = var30 == var28
	var32 = ISZERO(var31)
	if var32: THROW()
	var33 = var25 & 0xffffffffffffffffffffffffffffffffffffffff
	var34 = ISZERO(var26)
	var35 = var34 * 0x08fc
	var36 = CALL(var35, var33, var26, 0x60, 00, 0x60, 00)
	POP(var33)
	POP(0x60)
	POP(var26)
	POP(var35)
	var37 = ISZERO(var36)
	if var37: THROW()
	var38 = MLOAD(0x40)
	var39 = var25 & 0xffffffffffffffffffffffffffffffffffffffff
	MSTORE(var38, var39)
	var40 = var38 + 0x20
	MSTORE(var40, var26)
	var41 = MLOAD(0x40)
	var42 = var38 - var41
	var43 = 0x40 + var42
	LOG1(var41, var43, 7f51d406915971d4ac1c91af96be5187ea6ab64753785aad519a533def80a41e)
	POP(var26)
	POP(var25)
	func4()

def func4():
	STOP()
