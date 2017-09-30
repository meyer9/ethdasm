def main():
	MSTORE(0x40, 0x60)
	var1 = CALLDATALOAD(0x0)
	var2 = var1 // 0x100000000000000000000000000000000000000000000000000000000
	var3 = 0xffffffff & var2
	var4 = 0x41c0e1b5 == var3
	if var4: func1()
	var5 = 0xcfae3217 == var3
	if var5: func4()
	REVERT(0x0, 0x0)

def func1():
	var6 = CALLVALUE()
	var7 = ISZERO(var6)
	if var7: func2()
	REVERT(0x0, 0x0)

def func2():
	func10()

def func3():
	STOP()


def func4():
	var8 = CALLVALUE()
	var9 = ISZERO(var8)
	if var9: func5()
	REVERT(0x0, 0x0)


def func5():
	func12()


def func6(arg0):
	var10 = MLOAD(0x40)
	var11 = 0x20 + var10
	var12 = var11 - var10
	MSTORE(var10, var12)
	var13 = MLOAD(arg0)
	MSTORE(var11, var13)
	var14 = 0x20 + var11
	POP(var11)
	var15 = MLOAD(arg0)
	var16 = 0x20 + arg0


def func7(arg0, arg1, arg2, arg3):
	var17 = arg0 < arg3
	var18 = ISZERO(var17)
	if var18: func8()
	var19 = arg1 + arg0
	var20 = MLOAD(var19)
	var21 = arg2 + arg0
	MSTORE(var21, var20)
	var22 = arg0 + 0x20
	POP(arg0)
	func7()


def func8(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
	POP(arg0)
	POP(arg1)
	POP(arg2)
	POP(arg3)
	POP(arg5)
	var23 = arg4 + arg6
	var24 = 0x1f & arg4
	var25 = ISZERO(var24)
	if var25: func9()
	var26 = var23 - var24
	var27 = MLOAD(var26)
	var28 = 0x20 - var24
	var29 = 0x100 ** var28
	var30 = var29 - 0x1
	var31 = NOT(var30)
	var32 = var31 & var27
	MSTORE(var26, var32)
	var33 = 0x20 + var26
	POP(var23)


def func9(arg0, arg1, arg2, arg3, arg4):
	POP(arg0)
	POP(arg4)
	POP(arg2)
	POP(arg3)
	var34 = MLOAD(0x40)
	var35 = arg1 - var34
	RETURN(var34, var35)


def func10():
	var36 = SLOAD(0x0)
	var37 = 0x100 ** 0x0
	var38 = var36 // var37
	var39 = 0xffffffffffffffffffffffffffffffffffffffff & var38
	var40 = 0xffffffffffffffffffffffffffffffffffffffff & var39
	var41 = CALLER()
	var42 = 0xffffffffffffffffffffffffffffffffffffffff & var41
	var43 = var42 == var40
	var44 = ISZERO(var43)
	if var44: func11()
	var45 = SLOAD(0x0)
	var46 = 0x100 ** 0x0
	var47 = var45 // var46
	var48 = 0xffffffffffffffffffffffffffffffffffffffff & var47
	var49 = 0xffffffffffffffffffffffffffffffffffffffff & var48
	SUICIDE(var49)


def func11(arg0):
	arg0()


def func12():
	THROW()


def func13():
	var50 = SLOAD(0x1)
	var51 = 0x1 & var50
	var52 = ISZERO(var51)
	var53 = 0x100 * var52
	var54 = var53 - 0x1
	var55 = var54 & var50
	var56 = var55 // 0x2
	var57 = 0x1f + var56
	var58 = var57 // 0x20
	var59 = var58 * 0x20
	var60 = 0x20 + var59
	var61 = MLOAD(0x40)
	var62 = var61 + var60
	MSTORE(0x40, var62)
	MSTORE(var61, var56)
	var63 = 0x20 + var61
	var64 = SLOAD(0x1)
	var65 = 0x1 & var64
	var66 = ISZERO(var65)
	var67 = 0x100 * var66
	var68 = var67 - 0x1
	var69 = var68 & var64
	var70 = var69 // 0x2
	var71 = ISZERO(var70)
	if var71: func16()
	var72 = 0x1f < var70
	if var72: func14()
	var73 = SLOAD(0x1)
	var74 = var73 // 0x100
	var75 = var74 * 0x100
	MSTORE(var63, var75)
	var76 = 0x20 + var63
	func16()


def func14(arg0, arg1, arg2):
	var77 = arg2 + arg0
	MSTORE(0x0, arg1)
	var78 = SHA3(0x0, 0x20)


def func15(arg0, arg1, arg2):
	var79 = SLOAD(arg1)
	MSTORE(arg0, var79)
	var80 = 0x1 + arg1
	var81 = 0x20 + arg0
	var82 = arg2 > var81
	if var82: func15()
	var83 = var81 - arg2
	var84 = 0x1f & var83
	var85 = arg2 + var84


def func16(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
	POP(arg0)
	POP(arg1)
	POP(arg2)
	POP(arg3)
	POP(arg4)
	POP(arg6)
	arg7()
