.686
.model flat

public _f

.data
sto	dq	100.0
piecdziesiat	dq	50.0

.code
_f	PROC
	push EBP
	mov EBP, ESP

	finit
	fld sto			; st(0) = 100.0
	fld	QWORD PTR [EBP+8]		; load argument, st(0) = 100.0 st(1) = arg
	fmulp			; st(0) = 100.0 * arg
	fld piecdziesiat	; st(0) = 100.0 * arg, st(1) = 50.0
	faddp			; st(0) = 100.0 * arg + 50.0

	pop EBP
	ret
_f	ENDP
END
