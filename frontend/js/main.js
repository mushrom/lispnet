function runCode( ){
    var incode = encodeURIComponent( foo.getValue( ));
    var out = document.getElementById( "output_box" );
    var pasteurl = document.getElementById( "paste_url" );
    console.log( incode );

    var txt = new XMLHttpRequest( );
    txt.onreadystatechange = function( ){
        if ( txt.readyState == 4 && txt.status == 200 ){
            //out.innerHTML = "<pre>" + txt.responseText + "</pre>";
            //out.innerHTML += "\n";
            //out.innerHTML += txt.responseText;
            out.innerHTML = txt.responseText + "\n===============\n\n" + out.innerHTML;
            var temp = "http://localhost/?paste=" + txt.responseText.split("\n")[0];
            pasteurl.innerHTML = "<a href='" + temp + "'> " + temp + "</a>";

        } else if ( txt.readyState == 4 ){
            errstr = "Error while submitting code: HTTP " + txt.status + "\n";
            out.innerHTML = errstr + "\n===============\n\n" + out.innerHTML;
        }
    }

    txt.open( "GET", "/netlisp/coderun/?code=" + incode, true );
    //txt.open( "GET", "LICENSE", true );
    txt.send( );
    //out.innerHTML = foo.getValue( "<br />\n" );
};

function getCodeList( ){
    var out = document.getElementById( "codelist_cont" );

    var txt = new XMLHttpRequest( );
    txt.onreadystatechange = function( ){
        if ( txt.readyState == 4 && txt.status == 200 ){
            //out.innerHTML = "<pre>" + txt.responseText + "</pre>";
            //out.innerHTML = txt.responseText;
            var foo = txt.responseText.split( "\n" );
            var accum = "";

            for ( var i = 0; i < foo.length; i++ ){
                accum += "<a onclick=\"loadCodeFile('" + foo[i] + "')\">";
                accum += "&gt;&gt; " + foo[i] + "</a><br />\n";
            }

            out.innerHTML = accum;
        }
    }

    txt.open( "GET", "/netlisp/code", true );
    txt.send( );
    console.log( getUrlParameters( "paste", true ));
};

function loadCodeFile( filename ){
    var txt = new XMLHttpRequest( );

    txt.onreadystatechange = function( ){
        console.log( "loadCodeFile: got here" );
        if ( txt.readyState == 4 && txt.status == 200 ){
            foo.setValue( txt.responseText );
        }
    }

    //foo.setValue( "Loading..." );
    txt.open( "GET", "/netlisp/code/" + filename, true );
    //txt.open( "GET", "LICENSE", true );
    txt.send( );
    //out.innerHTML = foo.getValue( "<br />\n" );

}

function stringContains( str, things ){
    var ret = true;

    for ( i = 0; i < things.length; i++ ){
        if ( str.indexOf(things[i]) < 0 ){
            ret = false;
            break;
        }
    }

    return ret;
}

function getUrlParameters( target, decode ){
    var cur = window.location.search;
    var ret = false;

    if ( stringContains( cur, ["?", "="] )){
        var params = cur.split("?")[1].split("&");

        for ( var i = 0; i < params.length; i++ ){
            var param = params[i].split( "=" );

            if ( param[0] == target && param.length > 1 ){
                ret = decode? decodeURIComponent( param[1] ) : param[1];
                break;
            }
        }
    }

    return ret;
};

CodeMirror.commands.save = function(){ runCode( ); };

var foo = CodeMirror.fromTextArea( document.getElementById( "uwot" ), {
    value: "(print \"Hello, world!\")",
    lineNumbers: true,
    keyMap: "vim",
    matchBrackets: true,
});

getCodeList( );

var curfile = getUrlParameters( "paste", true );
if ( curfile ){
    loadCodeFile( curfile );
}

function showExamples( ){
    ex   = document.getElementById( "example_cont" );
    code = document.getElementById( "codelist_cont" );

    ex.style.display   = "inline";
    code.style.display = "none";
}

function showCodelist( ){
    ex   = document.getElementById( "example_cont" );
    code = document.getElementById( "codelist_cont" );

    ex.style.display   = "none";
    code.style.display = "inline";
}

function clearBuffer( ){
    var out = document.getElementById( "output_box" );

    out.innerHTML = "[output buffer]";
}

var in_vim = true;

function toggleVimMode( ){
    var map = in_vim? "default" : "vim";
    var cmbox = foo.getTextArea( );
    var butt = document.getElementById( "vim_button" );

    foo.toTextArea( );

    foo = CodeMirror.fromTextArea( document.getElementById( "uwot" ), {
        lineNumbers: true,
        keyMap: map,
        matchBrackets: true,
    });

    in_vim = !in_vim;
    butt.innerHTML = in_vim? "Vim on" : "Vim off";
}
