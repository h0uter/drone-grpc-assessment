#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}

// pub mod hello { 
//     tonic::include_proto!("hello"); 
// }

pub mod drones { 
    tonic::include_proto!("drones"); 
}