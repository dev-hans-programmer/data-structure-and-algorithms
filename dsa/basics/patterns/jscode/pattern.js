function pattern1() {
    let row = 5, col = 5;

    for(let i = 1 ; i <= row ; i++) {
        for(let j = 1 ; j<= col ; j++)
            process.stdout.write("* "); // no new line
        console.log()
    }
}

function pattern1Different() {
    let row = 5, col = 5;
    for(let i = 1 ; i<= row ; i++)  {
        let line = ''
        for(let j = 1 ; j <= col; j++)
            line+='* '
        console.log(line)
    }
            
}

pattern1Different()