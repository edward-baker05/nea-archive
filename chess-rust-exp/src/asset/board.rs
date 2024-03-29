use crate::asset::tile::Tile;

pub struct Board {
    tiles: Vec<Option<Tile>>,
    turn: char,
}

impl Board {
    pub fn new() -> Board {
        Board {
            tiles: std::iter::repeat_with(|| None).take(64).collect::<Vec<_>>(),
            turn: 'W',
        }
    }

    pub fn load_from_fen(&mut self, fen: Option<&str>) {
        let fen_unwrapped = fen.unwrap();
        let fen_layout = fen_unwrapped
            .split_whitespace()
            .nth(0)
            .unwrap()
            .chars()
            .rev()
            .collect::<String>();
        let mut i = 0;
        for row in fen_layout.split("/").collect::<Vec<&str>>() {
            for piece in row.chars().rev() {
                if piece.is_numeric() {
                    for _ in 0..piece.to_digit(10).unwrap() {
                        self.tiles[i] = None;
                        i += 1;
                    }
                } else {
                    let colour = if piece.is_uppercase() { true } else { false };
                    self.tiles[i] = Some(Tile::new(colour, piece.to_ascii_lowercase()));
                    i += 1;
                }
            }
        }
        self.turn = fen_unwrapped
            .split_whitespace()
            .nth(1)
            .unwrap()
            .chars()
            .nth(0)
            .unwrap()
            .to_ascii_uppercase();
    }

<<<<<<< HEAD
    pub fn print_board(&self) {
=======
    pub fn print_board(self) -> Board {
>>>>>>> 6cc83f690286307d73d7403a8291c230f798d339
        println!(" +--+--+--+--+--+--+--+--+");
        let mut row_num = 8;
        for i in (0..8).rev() {
            print!("{}|", row_num);
            for j in 0..8 {
                let tile = self.tiles[(i * 8) + j].as_ref();
                match tile {
                    Some(tile) => print!("{}{}|", tile.get_colour(), tile.get_piece()),
                    None => print!("  |"),
                };
            }
            println!("\n +--+--+--+--+--+--+--+--+");
            row_num -= 1;
        }
        println!("  a  b  c  d  e  f  g  h\t{}'s turn", self.turn);
        self
    }

    fn is_check() {}

    pub fn is_checkmate(&self) -> u8 {
        0
    }
}
