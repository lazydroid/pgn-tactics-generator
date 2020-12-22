#
# Check if the position is worth trying for a puzzle:
#	1. there's a sufficient drop in evaluation
#	2. there's enough material
#	3. the possibility of mate
#
import chess

def sign(a):
	if a > 0:
		return 1
	elif a < 0:
		return -1
	else:
		return 0

def material_value(board):
	return sum(v * (len(board.pieces(pt, True)) + len(board.pieces(pt, False))) for v, pt in zip([0,3,3,5.5,9], chess.PIECE_TYPES))

def material_count(board):
	return chess.popcount(board.occupied)

def investigate(a, b, board):
	# determine if the difference between position A and B is worth investigating for a puzzle

	if a.mate is not None and b.mate is not None :
		return sign(a.mate) == sign(b.mate)	# actually means that they're opposite

	if a.mate is not None and b.cp is not None :	# missed giving mate
		#if abs(b.cp) < 300 :	# playable within 3 pawns lost?
		return True

	if a.cp is not None and b.mate is not None :	# blundered a mate
		#if a.cp < -850 :		# already a lost cause, mate won't make it worse
		#if abs(b.mate) < 5 :	# less than 5 moves, otherwise it's a torture
		return True

	if a.cp is not None and b.cp is not None :
		if material_value(board) > 3 and material_count(board) > 6 :
			#if (((-110 < a.cp < 850 and 200 < b.cp < 850) 	# this is strange looking
			#	or (-850 < a.cp < 110 and -850 < b.cp < -200))
			if abs(a.cp + b.cp) > 300 :		# evaluation changed by more than 3 pawns
				if a.cp > -b.cp : return True	# blunder move -- do we need this check????

#	elif (a.cp is not None
#		and b.mate is not None
#		and material_value(board) > 3):
#		if ((a.cp < 110 and sign(b.mate) == -1) or (a.cp > -110 and sign(b.mate) == 1) ):
#			return True

	return False
