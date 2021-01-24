var faker = require('faker')
var fs = require('fs')
faker.locale = "de"

const generateRandomPerson = () => {
    return {
        id: faker.random.number(100),
        first_name: faker.name.firstName(),
        last_name: faker.name.lastName()
    };
};

const generateRandomPersonsList = (num) => {
    return Array.from({ length: num}, generateRandomPerson);
};

let testData = generateRandomPersonsList(20);

fs.writeFileSync('json_testfile.json', JSON.stringify(testData, null, '\t'));



