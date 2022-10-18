// Use piece
use crate::asset::piece::Piece;

pub struct Board {
    pub board: Vec<Piece>,
    pub turn: char,
    pub move_count: u8,
}

impl Board {
    pub fn load_from_fen(&mut self, fen: String) -> Vec<i32> {
        // Parse FEN string
        let fen_board = fen
            .split_whitespace()
            .nth(0)
            .unwrap()
            .chars()
            .rev()
            .collect::<String>();
        let board_arr = fen_board.split("/").collect::<Vec<&str>>();
        for row in board_arr {
            for piece in row.chars() {
                if piece.is_numeric() {
                    for _ in 0..piece.to_digit(10).unwrap() {
                        self.board.push(Piece::new(' ', ' '));
                    }
                } else {
                    let colour = if piece.is_uppercase() { 'w' } else { 'b' };
                    let piece = Piece::new(piece, colour);
                    self.board.push(piece);
                }
            }
        }
        return (0..64).collect::<Vec<i32>>();
    }

    pub fn print_board(&self) {
        println!(" +--+--+--+--+--+--+--+--+");
        let mut row_num = 8;
        for i in (0..8).rev() {
            print!("{}|", row_num);
            for j in 0..8 {
                let piece = &self.board[(i * 8) + j];
                print!(
                    "{}{}|",
                    Piece::get_colour(&piece).to_uppercase(),
                    Piece::get_kind(&piece).to_uppercase()
                );
            }
            println!("\n +--+--+--+--+--+--+--+--+");
            row_num -= 1;
        }
        println!(
            "  a  b  c  d  e  f  g  h\t{}'s turn",
            self.turn.to_uppercase()
        );
    }

    pub fn r#move(&self, start: (i32, i32), end: (i32, i32)) {
        println!("Moving from {:?} to {:?}", start, end);
    }

    pub fn is_won(&self) -> bool {
        false
    }
}