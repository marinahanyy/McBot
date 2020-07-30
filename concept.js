function setup(){var button =document.getElementById("start")
var input =document.getElementById("user_input").value;
var output =document.getElementById("output");
var bot = new RiveScript();
bot.loadFile("bot.rive",brainready,brainerror);
function brainready(){
 console.log('chat bot Ready') ;
 bot.sortReplies();

}
function brainerror(){

console.log('chat bot error');

}
button.mousePressed(chat);
function chat(){
 var reply = bot.reply('local-user',input);
 output.html(reply);
}
}