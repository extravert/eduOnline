const htmlEscape = require("./index")

// console.log(htmlEscape)

const htmlStr = '<h1 title="abc">这是h1标签<span>123&nbsp;</aspan></h1>'

const dt = new Date()
console.log(dt)
const dtnew = htmlEscape.dateFormat(dt)
console.log(dtnew)



//导入的是一个对象，不能直接当函数用
const str = htmlEscape.htmlEscape(htmlStr)

console.log(str)

const str1 = htmlEscape.htmlUnEscape(str)
console.log(str1)
