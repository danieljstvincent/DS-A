"""
Common utilities used across all games.

This module provides shared functions that are used by multiple games
to reduce code duplication and maintain consistency.
"""

import os

def clear_screen():
    """
    Clear the terminal screen (OS-agnostic).
    
    Works on both Windows ('cls') and Unix-like systems ('clear').
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_input(prompt, validator=None, error_msg="Invalid input. Please try again."):
    """
    Get and validate user input with retry on invalid input.
    
    Args:
        prompt (str): Prompt to display to the user
        validator (callable, optional): Function that takes input string and returns 
            (is_valid: bool, value: any) tuple. If None, just returns input as-is.
        error_msg (str): Message to display when validation fails
    
    Returns:
        Validated input value (or original input if no validator)
    
    Raises:
        KeyboardInterrupt: If user interrupts input (Ctrl+C)
        EOFError: If input stream ends
    
    Example:
        >>> def validate_number(value):
        ...     try:
        ...         num = int(value)
        ...         if 1 <= num <= 10:
        ...             return (True, num)
        ...         return (False, None)
        ...     except ValueError:
        ...         return (False, None)
        >>> num = get_valid_input("Enter number 1-10: ", validate_number)
    """
    while True:
        try:
            value = input(prompt).strip()
            if validator:
                is_valid, result = validator(value)
                if is_valid:
                    return result
                else:
                    print(error_msg)
            else:
                return value
        except (KeyboardInterrupt, EOFError):
            raise

def validate_int_range(min_val, max_val):
    """
    Create a validator function for integer input within a range.
    
    Args:
        min_val (int): Minimum acceptable value (inclusive)
        max_val (int): Maximum acceptable value (inclusive)
    
    Returns:
        callable: Validator function that can be used with get_valid_input
    
    Example:
        >>> validator = validate_int_range(0, 10)
        >>> value = get_valid_input("Enter 0-10: ", validator)
    """
    def validator(value):
        try:
            num = int(value)
            if min_val <= num <= max_val:
                return (True, num)
            return (False, None)
        except ValueError:
            return (False, None)
    
    return validator

def validate_choice(choices, case_sensitive=False):
    """
    Create a validator function for input that must be one of the given choices.
    
    Args:
        choices (list): List of valid choice strings
        case_sensitive (bool): If False, comparison is case-insensitive
    
    Returns:
        callable: Validator function that can be used with get_valid_input
    
    Example:
        >>> validator = validate_choice(['yes', 'no'], case_sensitive=False)
        >>> answer = get_valid_input("Yes or No? ", validator)
    """
    def validator(value):
        if not case_sensitive:
            value = value.lower()
            choices_lower = [c.lower() for c in choices]
            if value in choices_lower:
                idx = choices_lower.index(value)
                return (True, choices[idx])  # Return original case
        else:
            if value in choices:
                return (True, value)
        return (False, None)
    
    return validator

def format_board(board, row_labels=None, col_labels=None, cell_formatter=None):
    """
    Format a 2D board/matrix for display with optional labels.
    
    Args:
        board (list): 2D list to format
        row_labels (list, optional): Labels for rows (left side)
        col_labels (list, optional): Labels for columns (top)
        cell_formatter (callable, optional): Function to format each cell value
    
    Returns:
        str: Formatted board as a string
    
    Example:
        >>> board = [['X', 'O', ' '], [' ', 'X', 'O'], ['O', ' ', 'X']]
        >>> print(format_board(board, row_labels=['1', '2', '3'], 
        ...                     col_labels=['A', 'B', 'C']))
    """
    if not board or not board[0]:
        return ""
    
    rows = len(board)
    cols = len(board[0])
    
    # Format cells
    formatted_cells = []
    for row in board:
        formatted_row = []
        for cell in row:
            if cell_formatter:
                formatted_row.append(cell_formatter(cell))
            else:
                formatted_row.append(str(cell))
        formatted_cells.append(formatted_row)
    
    lines = []
    
    # Column labels (top)
    if col_labels:
        label_line = "   "  # Space for row labels
        for label in col_labels:
            label_line += f" {label}"
        lines.append(label_line)
        lines.append("  " + "-" * (cols * 2 + 1))
    
    # Board rows
    for i, row in enumerate(formatted_cells):
        line_parts = []
        if row_labels:
            line_parts.append(f"{row_labels[i]}|")
        else:
            line_parts.append("|")
        
        line_parts.append(" ".join(row))
        
        if row_labels:
            line_parts.append(f"|{row_labels[i]}")
        else:
            line_parts.append("|")
        
        lines.append(" ".join(line_parts))
    
    # Column labels (bottom, optional)
    if col_labels:
        lines.append("  " + "-" * (cols * 2 + 1))
        label_line = "   "
        for label in col_labels:
            label_line += f" {label}"
        lines.append(label_line)
    
    return "\n".join(lines)

