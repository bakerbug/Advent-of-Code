extern crate core;

use std::fs::File;
use std::io::{BufRead, BufReader, Error, Write};
use std::{io, process};
use std::rc::Rc;

// use log::debug;

mod day_1;
mod day_2;
mod day_3;

fn file_opener(file_name: &String) -> Result<File, Error> {
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
        Err(e) => panic!("Unable to open {file}: {}", e),
    }
    return input;
}

fn read_string_input(file: &String) -> Vec<String>{
    let mut input: Vec<String> = Vec::new();
    match file_opener(file) {
        Ok(file_pointer) => {
            let buffer_reader = BufReader::new(file_pointer);
            for line in buffer_reader.lines() {
                let data_string = line.unwrap().trim().parse().expect("Unable to translate data to string.");
                input.push(data_string);
            }
        }
        Err(e) => panic!("Unable to open {file}: {}", e),
    }
    return input;

}

fn read_string_input_rc(file: &String) -> Vec<Rc<String>>{
    let mut input: Vec<Rc<String>> = Vec::new();
    match file_opener(file) {
        Ok(file_pointer) => {
            let buffer_reader = BufReader::new(file_pointer);
            for line in buffer_reader.lines() {
                let data_string = Rc::new(line.unwrap().trim().parse().expect("Unable to translate data to string."));
                input.push(data_string);
            }
        }
        Err(e) => panic!("Unable to open {file}: {}", e),
    }
    return input;

}

fn menu() -> char {
    println!("Welcome to Advent of Code 2021 implemented in Rust!");
    println!("Please enter the number for the day you wish to execute or 'a' for all of them.");
    print!("Selection>");
    io::stdout().flush().expect("Unable to print menu!");
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let first_letter = input.chars().nth(0).unwrap();
    return first_letter;
}

fn select_data_file(selection: char) -> String {
    if selection == 's' {
        return "sample.txt".to_string();
    }
    let result = format!("day_{}.txt", selection.to_string());
    return result;
}


fn main() {
    loop {
        let menu_option = menu();
        let input_file = select_data_file(menu_option);

        match menu_option {
            '1' => {
                let input_data = read_int_input(&input_file);
                let d1p1 = day_1::part_1(&input_data);
                println!("Day 1 - Part 1 result: {d1p1}");

                let d1p2 = day_1::part_2(&input_data);
                println!("Day 1 - Part 2 result: {d1p2}");
            }
            '2' => {
                let input_data = read_string_input(&input_file);
                let d2p1 = day_2::part_1(&input_data);
                println!("Day 2 - Part 1 result: {d2p1}");

                let d2p2 = day_2::part_2(&input_data);
                println!("Day 2 - Part 2 result: {d2p2}");
            }

            '3' | 's' => {
                let input_data = read_string_input(&input_file);
                let d3p1 = day_3::part_1(&input_data);
                println!("Day 3 - Part 1 result: {d3p1}");

                let input_data_rc = read_string_input_rc(&input_file);
                let d3p2: i32 = day_3::part_2(&input_data_rc);
                println!("Day 3 - Part 2 result: {d3p2}");
            }

            'Q' | 'q' => {
                process::exit(0x0000);
            }
            _ => { println!("Option not implemented!") }
        }
    }
}
