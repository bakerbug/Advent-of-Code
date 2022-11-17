use std::rc::Rc;
use crate::day_3::MostLeast::{Least, Most};

pub fn part_1(input: &Vec<String>) -> i32 {
    let datum_length = input[0].len();
    let data_length = input.len();
    let mut gamma: String = String::new();
    let mut epsilon: String = String::new();

    for a in 0..datum_length {  // Looping through each digit in a value
        let mut on = 0;
        let mut off = 0;
        for b in 0..data_length { // Looping though each value in the list
            let bits = &input.as_slice()[b];
            // println!("bits: >{}<", bits);
            let bit: u8 = bits.as_bytes()[a];  // bit is now the ASCII value of the 1 or 0 character
            // println!("Inspecting >{}<", bit as char);
            if bit as char == '1' {
                on += 1;
            }
            else if bit as char == '0' {
                off += 1;
            }
            else {
                panic!("{} is not binary!", bit);
            }
        }

        if on > off {
            gamma.push('1');
            epsilon.push('0');
        }
        else if off > on {
            gamma.push('0');
            epsilon.push('1');
        }
        else {
            panic!("On and Off bits are equal!");
        }
    }

    let gamma_int = i32::from_str_radix(gamma.as_str(), 2).expect("Gamma is not binary!");
    let epsilon_int = i32::from_str_radix(epsilon.as_str(), 2).expect("Epsilon is not binary!");

    return gamma_int * epsilon_int;
}

pub fn part_2(input: &Vec<Rc<String>>) -> i32 {
    let mut result = 0;
    let datum_length = input[0].len();

    let oxygen_rating_bin= find_most_common(&input, 0, MostLeast::Most);
    let co2_rating_bin = find_most_common(&input, 0, MostLeast::Least);

    let oxygen_rating = isize::from_str_radix(&oxygen_rating_bin.unwrap(), 2).unwrap();
    let co2_rating = isize::from_str_radix(&co2_rating_bin.unwrap(), 2).unwrap();

    println!("Oxy: {oxygen_rating}, CO2: {co2_rating}");
    let life_support_rating = oxygen_rating * co2_rating;
    println!("The life support rating is {life_support_rating}.");


    return 1;
}

#[derive(Debug, PartialEq, Eq, Clone, Copy)]
enum MostLeast {
    Most,
    Least,
}

fn find_most_common(input: &Vec<Rc<String>>, place: usize, which: MostLeast) -> Result<Rc<String>, String> {

    // println!("Data length is: {}", input.len());

    if input.len() == 1 {
        let result = Rc::clone(&input[0]);
        return Ok(result);
    }

    let mut on = 0;
    let mut off = 0;
    let mut high_bit: Vec<Rc<String>> = Vec::new();
    let mut low_bit: Vec<Rc<String>> = Vec::new();

    for word in 0..input.len() {

        let bit_value = compare_bit(&input, word, place);

        if bit_value {
            on += 1;
            high_bit.push(Rc::clone(&input[word]));
        } else {
            off += 1;
            low_bit.push(Rc::clone(&input[word]));
        }
    }

    let next = place + 1;

    if which == Most {
        if on > off {
           return find_most_common(&high_bit, next, which);
        }
        if off > on {
           return find_most_common(&low_bit, next, which);
        }
        if on == off {
            return find_most_common(&high_bit, next, which);
        }
    }
    if which == Least {
        if on > off {
           return find_most_common(&low_bit, next, which);
        }
        if off > on {
           return find_most_common(&high_bit, next, which);
        }

        if on == off {
            return find_most_common(&low_bit, next, which);
        }
    }

    return Err("Something went horribly wrong!".to_string());
}


fn compare_bit(question: &Vec<Rc<String>>, word: usize, place: usize,) -> bool {
    let bits = &question.as_slice()[word];
    let bit: u8 = bits.as_bytes()[place];  // bit is now the ASCII value of the 1 or 0 character
    return if bit as char == '1' {
        true
    } else {
        false
    }
}
