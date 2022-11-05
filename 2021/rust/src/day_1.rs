// use log::debug;


pub fn part_1(data: &Vec<i32>) -> i32 {
    let mut increase = 0;
    let mut previous = 0;
    let size = data.len();
    for i in 0..size {
        if i == 0 {
            previous = data[i];
            continue;
        } else if data[i] > previous {
            increase += 1;
        }

        previous = data[i];
    }

    return increase;
}

pub fn part_2(data: &Vec<i32>) -> i32 {
    let mut first: i32 = 0;
    let mut second: i32 = 0;
    let mut third: i32 = 0;
    let mut increase: i32 = 0;
    let mut previous: i32 = 0;

    let size = data.len();

    for i in 0..size {
        match i {
            0 => first = data[i],
            1 => second = data[i],
            2 => {
                third = data[i];
                previous = first + second + third;
            },
            _ => {
                first = second;
                second = third;
                third = data[i];

                let current = first + second + third;
                if current > previous {
                    increase += 1;
                }
                previous = current;
            },
        }
    }

    return increase;
}
