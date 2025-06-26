def checkmate(board_string):
    try:
        # Validate input
        if not board_string:
            return "Error: Empty board string provided"
        
        if not isinstance(board_string, str):
            return "Error: Board must be a string"
        
        # Parse the multi-line board string
        cleaned = board_string.strip().strip('\\').strip()
        if not cleaned:
            return "Error: Board string contains no valid content"
            
        rows = [line.rstrip() for line in cleaned.split('\n') if line.strip()]
        
        if not rows:
            return "Error: No valid rows found in board"
        
        board = rows
        size = len(board)
        
        if size == 0:
            return "Error: Board has zero size"
        
        # Validate board is square
        for i, row in enumerate(board):
            if len(row) != size:
                return f"Error: Board is not square - row {i} has length {len(row)}, expected {size}"
        
        # Find the King
        king_pos = None
        king_count = 0
        
        for i in range(size):
            for j in range(size):
                if board[i][j].upper() == 'K':
                    king_pos = (i, j)
                    king_count += 1
        
        # Must have exactly one King
        if king_count == 0:
            return "Error: No King found on the board"
        elif king_count > 1:
            return f"Error: Multiple Kings found ({king_count}) - only one King allowed"
        
        king_row, king_col = king_pos
        
        # Check if King is under attack by any piece
        if is_king_in_check(board, king_row, king_col, size):
            return "Success"
        else:
            return "Fail"
            
    except Exception as e:
        return f"Error: Unexpected error occurred - {str(e)}"

def is_king_in_check(board, king_row, king_col, size):
    """Check if the King at given position is under attack."""
    
    # Check for Pawn attacks
    if is_attacked_by_pawn(board, king_row, king_col, size):
        return True
    
    # Check for Rook attacks (horizontal and vertical)
    if is_attacked_by_rook(board, king_row, king_col, size):
        return True
    
    # Check for Bishop attacks (diagonal)
    if is_attacked_by_bishop(board, king_row, king_col, size):
        return True
    
    # Check for Queen attacks (combination of rook and bishop)
    if is_attacked_by_queen(board, king_row, king_col, size):
        return True
    
    # Check for Knight attacks (L-shaped moves)
    if is_attacked_by_knight(board, king_row, king_col, size):
        return True
    
    return False

def is_attacked_by_pawn(board, king_row, king_col, size):
    """Check if King is attacked by a Pawn."""
    # Pawns attack diagonally forward (move "up" the board)
    # Check for Pawn attacks
    pawn_attack_positions = [
        (king_row + 1, king_col - 1),  # bottom-left
        (king_row + 1, king_col + 1)   # bottom-right
    ]
    
    for row, col in pawn_attack_positions:
        if 0 <= row < size and 0 <= col < size:
            if board[row][col].upper() == 'P':
                return True
    
    return False

def is_valid_piece(piece):
    """Check if a character represents a valid chess piece."""
    return piece.upper() in ['K', 'Q', 'R', 'B', 'P', 'N']

def is_attacked_by_rook(board, king_row, king_col, size):
    # Check all four directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col].upper()
            
            if piece == 'R':  # Found attacking rook
                return True
            elif is_valid_piece(piece):  # Hit another valid piece (blocking)
                break
                
            row += dr
            col += dc
    
    return False

def is_attacked_by_bishop(board, king_row, king_col, size):
    # Check all four diagonal directions
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col].upper()
            
            if piece == 'B':  # Found attacking bishop
                return True
            elif is_valid_piece(piece):  # Hit another valid piece (blocking)
                break
                
            row += dr
            col += dc
    
    return False

def is_attacked_by_queen(board, king_row, king_col, size):
    # Queen combines rook and bishop movement
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Rook directions
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Bishop directions
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col].upper()
            
            if piece == 'Q':  # Found attacking queen
                return True
            elif is_valid_piece(piece):  # Hit another valid piece (blocking)
                break
                
            row += dr
            col += dc
    
    return False

def is_attacked_by_knight(board, king_row, king_col, size):
    # L-shape: 2 squares in one direction, 1 in perpendicular
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    for dr, dc in knight_moves:
        row, col = king_row + dr, king_col + dc
        
        if 0 <= row < size and 0 <= col < size:
            if board[row][col].upper() == 'N':
                return True
    
    return False
