use std::collections;
use std::fs::File;
use std::io::{BufRead, BufReader, Error};

// use log::debug;

mod day_1;

fn file_opener(file_name: &str) -> Result<File, Error> {
    let path = "./inputs/".to_string() + file_name;
    println!("Opening: {}", path);
    let file = File::open(path);
    return file;
}

fn read_int_input(file: &String) -> Vec<i32>{
    let mut input:Vec<i32> = Vec::new();
    // let mut buffer_reader = BufReader::new();
    match file_opener(file) {
        Ok(file_pointer) => {
            let buffer_reader = BufReader::new(file_pointer);
            for line in buffer_reader.lines() {
                let number = line.unwrap().trim().parse().expect("Unable to translate data to integer.");
                input.push(number);
            }
        }
        Err(e) => panic!("Unable to open {}: {}", file, e),
    }

    return input;

}


fn main() {
    let mut inputs = collections::HashMap::from([
        (1, "day_1.txt".to_string()),
        (2, "day_2.txt".to_string()),
    ]);

    // let mut input_data: Vec<i32> = vec![];
    let mut input_file: &String = &String::new();

    match inputs.get(&1) {
        Some(result) => input_file = result,
        None => println!("No input file for given day."),
    }


    let input_data = read_int_input(input_file);
    println!("My data has {} entries!!!", input_data.len());

    let d1p1 = day_1::part_1(&input_data);
    println!("Day 1 - Part 1 result: {}", d1p1);

    let d1p2 = day_1::part_2(&input_data);
    println!("Day 1 - Part 2 result: {}", d1p2);
}
