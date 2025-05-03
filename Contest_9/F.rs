use std::io::{self, BufRead, Write};

fn solve_garden(w: i32, n: i64, field: Vec<Vec<i32>>) -> String {
    // Считаем, сколько растений уже есть в каждом ряду и столбце
    let mut row_count = [0; 2]; // Число растений в строках
    let mut col_count = [0; 2]; // Число растений в столбцах
    let mut total_plants = 0;   // Общее число растений на поле

    for i in 0..2 {
        for j in 0..2 {
            if field[i][j] == 1 {
                row_count[i] += 1;
                col_count[j] += 1;
                total_plants += 1;
            }
        }
    }

    // Сколько растений нужно добавить, чтобы в каждом ряду и столбце было ровно W растений
    let needed_in_rows: Vec<i32> = (0..2).map(|i| w - row_count[i]).collect();
    let needed_in_cols: Vec<i32> = (0..2).map(|j| w - col_count[j]).collect();

    // Проверяем, возможно ли это сделать
    if needed_in_rows.iter().any(|&x| x < 0) || needed_in_cols.iter().any(|&x| x < 0) {
        return "NO".to_string();
    }

    // Считаем, сколько растений нужно добавить
    let total_needed: i64 = needed_in_rows.iter().map(|&x| x as i64).sum();

    // Проверяем, совпадает ли с суммой по столбцам
    let total_needed_cols: i64 = needed_in_cols.iter().map(|&x| x as i64).sum();
    if total_needed != total_needed_cols {
        return "NO".to_string();
    }

    // Проверяем, совпадает ли общее число растений с N
    if total_plants as i64 + total_needed != n {
        return "NO".to_string();
    }

    "YES".to_string()
}

fn main() {
    let stdin = io::stdin();
    let stdout = io::stdout();
    let mut reader = stdin.lock();
    let mut writer = BufWriter::new(stdout);

    let mut input = String::new();
    reader.read_line(&mut input).unwrap();
    let t: i32 = input.trim().parse().unwrap(); // Число тестовых случаев

    for _ in 0..t {
        let mut input = String::new();
        reader.read_line(&mut input).unwrap();
        let mut iter = input.trim().split_whitespace();
        let w: i32 = iter.next().unwrap().parse().unwrap();
        let _h: i32 = iter.next().unwrap().parse().unwrap(); // H не используется
        let n: i64 = iter.next().unwrap().parse().unwrap();

        let mut field = vec![vec![0; 2]; 2];
        for i in 0..2 {
            let mut row_input = String::new();
            reader.read_line(&mut row_input).unwrap();
            let row: Vec<i32> = row_input
                .trim()
                .split_whitespace()
                .map(|x| x.parse().unwrap())
                .collect();
            for j in 0..2 {
                field[i][j] = row[j];
            }
        }

        let result = solve_garden(w, n, field);
        writeln!(writer, "{}", result).unwrap();
    }

    writer.flush().unwrap();
}