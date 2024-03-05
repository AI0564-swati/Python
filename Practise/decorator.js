// An exapmle of decorator in Node

// const middleware = (req, res, next) => {
//     console.log(`before passing ctrl to next middleware`);
//     next(); // decorator
//     console.log(`after passing ctrl to next middleware`);
// };

const delay = (n) => new Promise((r) => setTimeout(() => r(), n * 1000))

const deco = async (fn) => {
    console.time("Time Taken")
    await fn()
    console.timeEnd("Time Taken")
}

const myFunc = async () => {
    console.log('start')
    await delay(5)
    console.log('done')
}

deco(myFunc)
// @deco
// myFunc()