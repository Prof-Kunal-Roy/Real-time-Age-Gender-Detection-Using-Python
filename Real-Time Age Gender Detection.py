<!DOCTYPE html>
<!-- saved from url=(0091)http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb -->
<html lang="en-us"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>Real-Time Age Gender Detection using OpenCV - Jupyter Notebook</title>
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./Real-Time Age Gender Detection_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./Real-Time Age Gender Detection_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    


<script type="text/javascript" src="./Real-Time Age Gender Detection_files/MathJax.js.download" charset="utf-8"></script>

<script type="text/javascript">
// MathJax disabled, set as null to distinguish from *missing* MathJax,
// where it will be undefined, and should prompt a dialog later.
window.mathjax_url = "/static/components/MathJax/MathJax.js";
</script>

<link rel="stylesheet" href="./Real-Time Age Gender Detection_files/bootstrap-tour.min.css" type="text/css">
<link rel="stylesheet" href="./Real-Time Age Gender Detection_files/codemirror.css">


    <link rel="stylesheet" href="./Real-Time Age Gender Detection_files/style.min.css" type="text/css">
    

<link rel="stylesheet" href="./Real-Time Age Gender Detection_files/override.css" type="text/css">
<link rel="stylesheet" href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb" id="kernel-css" type="text/css">


    <link rel="stylesheet" href="./Real-Time Age Gender Detection_files/custom.css" type="text/css">
    <script src="./Real-Time Age Gender Detection_files/promise.min.js.download" type="text/javascript" charset="utf-8"></script>
    <script src="./Real-Time Age Gender Detection_files/react.production.min.js.download" type="text/javascript"></script>
    <script src="./Real-Time Age Gender Detection_files/react-dom.production.min.js.download" type="text/javascript"></script>
    <script src="./Real-Time Age Gender Detection_files/index.js.download" type="text/javascript"></script>
    <script src="./Real-Time Age Gender Detection_files/require.js.download" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20230307183922",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./Real-Time Age Gender Detection_files/contents.js.download"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888; display: contents}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./Real-Time Age Gender Detection_files/custom.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="nbextensions/jupyterlab-plotly/extension" src="./Real-Time Age Gender Detection_files/extension.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="nbextensions/jupyter-js-widgets/extension" src="./Real-Time Age Gender Detection_files/extension.js(1).download"></script><style type="text/css">div.MathJax_MathML {text-align: center; margin: .75em 0px; display: block!important}
.MathJax_MathML {font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
span.MathJax_MathML {display: inline!important}
.MathJax_mmlExBox {display: block!important; overflow: hidden; height: 1px; width: 60ex; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0}
[class="MJX-tex-oldstyle"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-oldstyle-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
[class="MJX-tex-caligraphic"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-caligraphic-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
@font-face /*1*/ {font-family: MathJax_Caligraphic-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf')}
@font-face /*2*/ {font-family: MathJax_Caligraphic-WEB; font-weight: bold; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Bold.otf')}
[mathvariant="double-struck"] {font-family: MathJax_AMS, MathJax_AMS-WEB}
[mathvariant="script"] {font-family: MathJax_Script, MathJax_Script-WEB}
[mathvariant="fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB}
[mathvariant="bold-script"] {font-family: MathJax_Script, MathJax_Caligraphic-WEB; font-weight: bold}
[mathvariant="bold-fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB; font-weight: bold}
[mathvariant="monospace"] {font-family: monospace}
[mathvariant="sans-serif"] {font-family: sans-serif}
[mathvariant="bold-sans-serif"] {font-family: sans-serif; font-weight: bold}
[mathvariant="sans-serif-italic"] {font-family: sans-serif; font-style: italic}
[mathvariant="sans-serif-bold-italic"] {font-family: sans-serif; font-style: italic; font-weight: bold}
@font-face /*3*/ {font-family: MathJax_AMS-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_AMS-Regular.otf')}
@font-face /*4*/ {font-family: MathJax_Script-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Script-Regular.otf')}
@font-face /*5*/ {font-family: MathJax_Fraktur-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Regular.otf')}
@font-face /*6*/ {font-family: MathJax_Fraktur-WEB; font-weight: bold; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Bold.otf')}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Blank; src: url('about:blank')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style>/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/* Override the correction for the prompt area in https://github.com/jupyter/notebook/blob/dd41d9fd5c4f698bd7468612d877828a7eeb0e7a/IPython/html/static/notebook/less/outputarea.less#L110 */
.jupyter-widgets-output-area div.output_subarea {
    max-width: 100%;
}

/* Work-around for the bug fixed in https://github.com/jupyter/notebook/pull/2961 */
.jupyter-widgets-output-area > .out_prompt_overlay {
    display: none;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/* <DEPRECATED> */
.p-Widget, /* </DEPRECATED> */
.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}

/* <DEPRECATED> */
.p-Widget.p-mod-hidden, /* </DEPRECATED> */
.lm-Widget.lm-mod-hidden {
  display: none !important;
}
</style><style>.lm-AccordionPanel[data-orientation='horizontal'] > .lm-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/* <DEPRECATED> */
.p-CommandPalette, /* </DEPRECATED> */
.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* <DEPRECATED> */
.p-CommandPalette-search, /* </DEPRECATED> */
.lm-CommandPalette-search {
  flex: 0 0 auto;
}

/* <DEPRECATED> */
.p-CommandPalette-content, /* </DEPRECATED> */
.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}

/* <DEPRECATED> */
.p-CommandPalette-header, /* </DEPRECATED> */
.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

/* <DEPRECATED> */
.p-CommandPalette-item, /* </DEPRECATED> */
.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}

/* <DEPRECATED> */
.p-CommandPalette-itemIcon, /* </DEPRECATED> */
.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}

/* <DEPRECATED> */
.p-CommandPalette-itemContent, /* </DEPRECATED> */
.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}

/* <DEPRECATED> */
.p-CommandPalette-itemShortcut, /* </DEPRECATED> */
.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

/* <DEPRECATED> */
.p-CommandPalette-itemLabel, /* </DEPRECATED> */
.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
  border: 1px solid transparent;
  background-color: transparent;
  position: absolute;
  z-index: 1;
  right: 3%;
  top: 0;
  bottom: 0;
  margin: auto;
  padding: 7px 0;
  display: none;
  vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
  content: 'X';
  display: block;
  width: 15px;
  height: 15px;
  text-align: center;
  color: #000;
  font-weight: normal;
  font-size: 12px;
  cursor: pointer;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/* <DEPRECATED> */
.p-DockPanel, /* </DEPRECATED> */
.lm-DockPanel {
  z-index: 0;
}

/* <DEPRECATED> */
.p-DockPanel-widget, /* </DEPRECATED> */
.lm-DockPanel-widget {
  z-index: 0;
}

/* <DEPRECATED> */
.p-DockPanel-tabBar, /* </DEPRECATED> */
.lm-DockPanel-tabBar {
  z-index: 1;
}

/* <DEPRECATED> */
.p-DockPanel-handle, /* </DEPRECATED> */
.lm-DockPanel-handle {
  z-index: 2;
}

/* <DEPRECATED> */
.p-DockPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}

/* <DEPRECATED> */
.p-DockPanel-handle:after, /* </DEPRECATED> */
.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}

/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}

/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/* <DEPRECATED> */
.p-DockPanel-overlay, /* </DEPRECATED> */
.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}

/* <DEPRECATED> */
.p-DockPanel-overlay.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/* <DEPRECATED> */
.p-Menu, /* </DEPRECATED> */
.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* <DEPRECATED> */
.p-Menu-content, /* </DEPRECATED> */
.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}

/* <DEPRECATED> */
.p-Menu-item, /* </DEPRECATED> */
.lm-Menu-item {
  display: table-row;
}

/* <DEPRECATED> */
.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed,
/* </DEPRECATED> */
.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}

/* <DEPRECATED> */
.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon,
/* </DEPRECATED> */
.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}

/* <DEPRECATED> */
.p-Menu-itemLabel, /* </DEPRECATED> */
.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}

/* <DEPRECATED> */
.p-Menu-itemShortcut, /* </DEPRECATED> */
.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/* <DEPRECATED> */
.p-MenuBar, /* </DEPRECATED> */
.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* <DEPRECATED> */
.p-MenuBar-content, /* </DEPRECATED> */
.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}

/* <DEPRECATED> */
.p--MenuBar-item, /* </DEPRECATED> */
.lm-MenuBar-item {
  box-sizing: border-box;
}

/* <DEPRECATED> */
.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel,
/* </DEPRECATED> */
.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/* <DEPRECATED> */
.p-ScrollBar, /* </DEPRECATED> */
.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* <DEPRECATED> */
.p-ScrollBar[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}

/* <DEPRECATED> */
.p-ScrollBar[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}

/* <DEPRECATED> */
.p-ScrollBar-button, /* </DEPRECATED> */
.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}

/* <DEPRECATED> */
.p-ScrollBar-track, /* </DEPRECATED> */
.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}

/* <DEPRECATED> */
.p-ScrollBar-thumb, /* </DEPRECATED> */
.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/* <DEPRECATED> */
.p-SplitPanel-child, /* </DEPRECATED> */
.lm-SplitPanel-child {
  z-index: 0;
}

/* <DEPRECATED> */
.p-SplitPanel-handle, /* </DEPRECATED> */
.lm-SplitPanel-handle {
  z-index: 1;
}

/* <DEPRECATED> */
.p-SplitPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}

/* <DEPRECATED> */
.p-SplitPanel-handle:after, /* </DEPRECATED> */
.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}

/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}

/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/* <DEPRECATED> */
.p-TabBar, /* </DEPRECATED> */
.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* <DEPRECATED> */
.p-TabBar[data-orientation='horizontal'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}

/* <DEPRECATED> */
.p-TabBar[data-orientation='vertical'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}

/* <DEPRECATED> */
.p-TabBar-content, /* </DEPRECATED> */
.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}

/* <DEPRECATED> */
.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}

/* <DEPRECATED> */
.p-TabBar[data-orientation='vertical'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}

/* <DEPRECATED> */
.p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
  touch-action: none; /* Disable native Drag/Drop */
}

/* <DEPRECATED> */
.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon,
/* </DEPRECATED> */
.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}

/* <DEPRECATED> */
.p-TabBar-tabLabel, /* </DEPRECATED> */
.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
}

/* <DEPRECATED> */
.p-TabBar-tab.p-mod-hidden, /* </DEPRECATED> */
.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}

/* <DEPRECATED> */
.p-TabBar.p-mod-dragging .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}

/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}

/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}

/* <DEPRECATED> */
.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
  background: inherit;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/* <DEPRECATED> */
.p-TabPanel-tabBar, /* </DEPRECATED> */
.lm-TabPanel-tabBar {
  z-index: 1;
}

/* <DEPRECATED> */
.p-TabPanel-stackedPanel, /* </DEPRECATED> */
.lm-TabPanel-stackedPanel {
  z-index: 0;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
</style><style>/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

 .jupyter-widgets-disconnected::before {
    content: "\f127"; /* chain-broken */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #d9534f;
    padding: 3px;
    align-self: flex-start;
}
</style><style>/**
 * The material design colors are adapted from google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/dist/palette.var.css
 *
 * The license for the material design color CSS variables is as follows (see
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/LICENSE)
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 Dan Le Van
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
:root {
  --md-red-50: #FFEBEE;
  --md-red-100: #FFCDD2;
  --md-red-200: #EF9A9A;
  --md-red-300: #E57373;
  --md-red-400: #EF5350;
  --md-red-500: #F44336;
  --md-red-600: #E53935;
  --md-red-700: #D32F2F;
  --md-red-800: #C62828;
  --md-red-900: #B71C1C;
  --md-red-A100: #FF8A80;
  --md-red-A200: #FF5252;
  --md-red-A400: #FF1744;
  --md-red-A700: #D50000;

  --md-pink-50: #FCE4EC;
  --md-pink-100: #F8BBD0;
  --md-pink-200: #F48FB1;
  --md-pink-300: #F06292;
  --md-pink-400: #EC407A;
  --md-pink-500: #E91E63;
  --md-pink-600: #D81B60;
  --md-pink-700: #C2185B;
  --md-pink-800: #AD1457;
  --md-pink-900: #880E4F;
  --md-pink-A100: #FF80AB;
  --md-pink-A200: #FF4081;
  --md-pink-A400: #F50057;
  --md-pink-A700: #C51162;

  --md-purple-50: #F3E5F5;
  --md-purple-100: #E1BEE7;
  --md-purple-200: #CE93D8;
  --md-purple-300: #BA68C8;
  --md-purple-400: #AB47BC;
  --md-purple-500: #9C27B0;
  --md-purple-600: #8E24AA;
  --md-purple-700: #7B1FA2;
  --md-purple-800: #6A1B9A;
  --md-purple-900: #4A148C;
  --md-purple-A100: #EA80FC;
  --md-purple-A200: #E040FB;
  --md-purple-A400: #D500F9;
  --md-purple-A700: #AA00FF;

  --md-deep-purple-50: #EDE7F6;
  --md-deep-purple-100: #D1C4E9;
  --md-deep-purple-200: #B39DDB;
  --md-deep-purple-300: #9575CD;
  --md-deep-purple-400: #7E57C2;
  --md-deep-purple-500: #673AB7;
  --md-deep-purple-600: #5E35B1;
  --md-deep-purple-700: #512DA8;
  --md-deep-purple-800: #4527A0;
  --md-deep-purple-900: #311B92;
  --md-deep-purple-A100: #B388FF;
  --md-deep-purple-A200: #7C4DFF;
  --md-deep-purple-A400: #651FFF;
  --md-deep-purple-A700: #6200EA;

  --md-indigo-50: #E8EAF6;
  --md-indigo-100: #C5CAE9;
  --md-indigo-200: #9FA8DA;
  --md-indigo-300: #7986CB;
  --md-indigo-400: #5C6BC0;
  --md-indigo-500: #3F51B5;
  --md-indigo-600: #3949AB;
  --md-indigo-700: #303F9F;
  --md-indigo-800: #283593;
  --md-indigo-900: #1A237E;
  --md-indigo-A100: #8C9EFF;
  --md-indigo-A200: #536DFE;
  --md-indigo-A400: #3D5AFE;
  --md-indigo-A700: #304FFE;

  --md-blue-50: #E3F2FD;
  --md-blue-100: #BBDEFB;
  --md-blue-200: #90CAF9;
  --md-blue-300: #64B5F6;
  --md-blue-400: #42A5F5;
  --md-blue-500: #2196F3;
  --md-blue-600: #1E88E5;
  --md-blue-700: #1976D2;
  --md-blue-800: #1565C0;
  --md-blue-900: #0D47A1;
  --md-blue-A100: #82B1FF;
  --md-blue-A200: #448AFF;
  --md-blue-A400: #2979FF;
  --md-blue-A700: #2962FF;

  --md-light-blue-50: #E1F5FE;
  --md-light-blue-100: #B3E5FC;
  --md-light-blue-200: #81D4FA;
  --md-light-blue-300: #4FC3F7;
  --md-light-blue-400: #29B6F6;
  --md-light-blue-500: #03A9F4;
  --md-light-blue-600: #039BE5;
  --md-light-blue-700: #0288D1;
  --md-light-blue-800: #0277BD;
  --md-light-blue-900: #01579B;
  --md-light-blue-A100: #80D8FF;
  --md-light-blue-A200: #40C4FF;
  --md-light-blue-A400: #00B0FF;
  --md-light-blue-A700: #0091EA;

  --md-cyan-50: #E0F7FA;
  --md-cyan-100: #B2EBF2;
  --md-cyan-200: #80DEEA;
  --md-cyan-300: #4DD0E1;
  --md-cyan-400: #26C6DA;
  --md-cyan-500: #00BCD4;
  --md-cyan-600: #00ACC1;
  --md-cyan-700: #0097A7;
  --md-cyan-800: #00838F;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84FFFF;
  --md-cyan-A200: #18FFFF;
  --md-cyan-A400: #00E5FF;
  --md-cyan-A700: #00B8D4;

  --md-teal-50: #E0F2F1;
  --md-teal-100: #B2DFDB;
  --md-teal-200: #80CBC4;
  --md-teal-300: #4DB6AC;
  --md-teal-400: #26A69A;
  --md-teal-500: #009688;
  --md-teal-600: #00897B;
  --md-teal-700: #00796B;
  --md-teal-800: #00695C;
  --md-teal-900: #004D40;
  --md-teal-A100: #A7FFEB;
  --md-teal-A200: #64FFDA;
  --md-teal-A400: #1DE9B6;
  --md-teal-A700: #00BFA5;

  --md-green-50: #E8F5E9;
  --md-green-100: #C8E6C9;
  --md-green-200: #A5D6A7;
  --md-green-300: #81C784;
  --md-green-400: #66BB6A;
  --md-green-500: #4CAF50;
  --md-green-600: #43A047;
  --md-green-700: #388E3C;
  --md-green-800: #2E7D32;
  --md-green-900: #1B5E20;
  --md-green-A100: #B9F6CA;
  --md-green-A200: #69F0AE;
  --md-green-A400: #00E676;
  --md-green-A700: #00C853;

  --md-light-green-50: #F1F8E9;
  --md-light-green-100: #DCEDC8;
  --md-light-green-200: #C5E1A5;
  --md-light-green-300: #AED581;
  --md-light-green-400: #9CCC65;
  --md-light-green-500: #8BC34A;
  --md-light-green-600: #7CB342;
  --md-light-green-700: #689F38;
  --md-light-green-800: #558B2F;
  --md-light-green-900: #33691E;
  --md-light-green-A100: #CCFF90;
  --md-light-green-A200: #B2FF59;
  --md-light-green-A400: #76FF03;
  --md-light-green-A700: #64DD17;

  --md-lime-50: #F9FBE7;
  --md-lime-100: #F0F4C3;
  --md-lime-200: #E6EE9C;
  --md-lime-300: #DCE775;
  --md-lime-400: #D4E157;
  --md-lime-500: #CDDC39;
  --md-lime-600: #C0CA33;
  --md-lime-700: #AFB42B;
  --md-lime-800: #9E9D24;
  --md-lime-900: #827717;
  --md-lime-A100: #F4FF81;
  --md-lime-A200: #EEFF41;
  --md-lime-A400: #C6FF00;
  --md-lime-A700: #AEEA00;

  --md-yellow-50: #FFFDE7;
  --md-yellow-100: #FFF9C4;
  --md-yellow-200: #FFF59D;
  --md-yellow-300: #FFF176;
  --md-yellow-400: #FFEE58;
  --md-yellow-500: #FFEB3B;
  --md-yellow-600: #FDD835;
  --md-yellow-700: #FBC02D;
  --md-yellow-800: #F9A825;
  --md-yellow-900: #F57F17;
  --md-yellow-A100: #FFFF8D;
  --md-yellow-A200: #FFFF00;
  --md-yellow-A400: #FFEA00;
  --md-yellow-A700: #FFD600;

  --md-amber-50: #FFF8E1;
  --md-amber-100: #FFECB3;
  --md-amber-200: #FFE082;
  --md-amber-300: #FFD54F;
  --md-amber-400: #FFCA28;
  --md-amber-500: #FFC107;
  --md-amber-600: #FFB300;
  --md-amber-700: #FFA000;
  --md-amber-800: #FF8F00;
  --md-amber-900: #FF6F00;
  --md-amber-A100: #FFE57F;
  --md-amber-A200: #FFD740;
  --md-amber-A400: #FFC400;
  --md-amber-A700: #FFAB00;

  --md-orange-50: #FFF3E0;
  --md-orange-100: #FFE0B2;
  --md-orange-200: #FFCC80;
  --md-orange-300: #FFB74D;
  --md-orange-400: #FFA726;
  --md-orange-500: #FF9800;
  --md-orange-600: #FB8C00;
  --md-orange-700: #F57C00;
  --md-orange-800: #EF6C00;
  --md-orange-900: #E65100;
  --md-orange-A100: #FFD180;
  --md-orange-A200: #FFAB40;
  --md-orange-A400: #FF9100;
  --md-orange-A700: #FF6D00;

  --md-deep-orange-50: #FBE9E7;
  --md-deep-orange-100: #FFCCBC;
  --md-deep-orange-200: #FFAB91;
  --md-deep-orange-300: #FF8A65;
  --md-deep-orange-400: #FF7043;
  --md-deep-orange-500: #FF5722;
  --md-deep-orange-600: #F4511E;
  --md-deep-orange-700: #E64A19;
  --md-deep-orange-800: #D84315;
  --md-deep-orange-900: #BF360C;
  --md-deep-orange-A100: #FF9E80;
  --md-deep-orange-A200: #FF6E40;
  --md-deep-orange-A400: #FF3D00;
  --md-deep-orange-A700: #DD2C00;

  --md-brown-50: #EFEBE9;
  --md-brown-100: #D7CCC8;
  --md-brown-200: #BCAAA4;
  --md-brown-300: #A1887F;
  --md-brown-400: #8D6E63;
  --md-brown-500: #795548;
  --md-brown-600: #6D4C41;
  --md-brown-700: #5D4037;
  --md-brown-800: #4E342E;
  --md-brown-900: #3E2723;

  --md-grey-50: #FAFAFA;
  --md-grey-100: #F5F5F5;
  --md-grey-200: #EEEEEE;
  --md-grey-300: #E0E0E0;
  --md-grey-400: #BDBDBD;
  --md-grey-500: #9E9E9E;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;

  --md-blue-grey-50: #ECEFF1;
  --md-blue-grey-100: #CFD8DC;
  --md-blue-grey-200: #B0BEC5;
  --md-blue-grey-300: #90A4AE;
  --md-blue-grey-400: #78909C;
  --md-blue-grey-500: #607D8B;
  --md-blue-grey-600: #546E7A;
  --md-blue-grey-700: #455A64;
  --md-blue-grey-800: #37474F;
  --md-blue-grey-900: #263238;
}</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
This file is copied from the JupyterLab project to define default styling for
when the widget styling is compiled down to eliminate CSS variables. We make one
change - we comment out the font import below.
*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/


/*
 * Optional monospace font for input/output prompt.
 */
 /* Commented out in ipywidgets since we don't need it. */
/* @import url('https://fonts.googleapis.com/css?family=Roboto+Mono'); */

/*
 * Added for compabitility with output area
 */
:root {
  --jp-icon-search: none;
  --jp-ui-select-caret: none;
}


:root {

  /* Borders

  The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-700);
  --jp-border-color1: var(--md-grey-500);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-100);

  /* UI Fonts

  The UI font CSS variables are used for the typography all of the JupyterLab
  user interface elements that are not directly user generated content.
  */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: calc(var(--jp-ui-font-size1)/var(--jp-ui-font-scale-factor));
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: calc(var(--jp-ui-font-size1)*var(--jp-ui-font-scale-factor));
  --jp-ui-font-size3: calc(var(--jp-ui-font-size2)*var(--jp-ui-font-scale-factor));
  --jp-ui-icon-font-size: 14px; /* Ensures px perfect FontAwesome icons */
  --jp-ui-font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;

  /* Use these font colors against the corresponding main layout colors.
     In a light theme, these go from dark to light.
  */

  --jp-ui-font-color0: rgba(0,0,0,1.0);
  --jp-ui-font-color1: rgba(0,0,0,0.8);
  --jp-ui-font-color2: rgba(0,0,0,0.5);
  --jp-ui-font-color3: rgba(0,0,0,0.3);

  /* Use these against the brand/accent/warn/error colors.
     These will typically go from light to darker, in both a dark and light theme
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* For backwards compatibility, we still define these below until ipywidgets 8.0.
  See https://github.com/jupyter-widgets/ipywidgets/pull/2801 */
  --jp-inverse-ui-font-color0: rgba(255,255,255,1);
  --jp-inverse-ui-font-color1: rgba(255,255,255,1.0);
  --jp-inverse-ui-font-color2: rgba(255,255,255,0.7);
  --jp-inverse-ui-font-color3: rgba(255,255,255,0.5);

  /* Content Fonts

  Content font variables are used for typography of user generated content.
  */

  --jp-content-font-size: 13px;
  --jp-content-line-height: 1.5;
  --jp-content-font-color0: black;
  --jp-content-font-color1: black;
  --jp-content-font-color2: var(--md-grey-700);
  --jp-content-font-color3: var(--md-grey-500);

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: calc(var(--jp-ui-font-size1)/var(--jp-ui-font-scale-factor));
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: calc(var(--jp-ui-font-size1)*var(--jp-ui-font-scale-factor));
  --jp-ui-font-size3: calc(var(--jp-ui-font-size2)*var(--jp-ui-font-scale-factor));

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.307;
  --jp-code-padding: 5px;
  --jp-code-font-family: monospace;


  /* Layout

  The following are the main layout colors use in JupyterLab. In a light
  theme these would go from light to dark.
  */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-700);
  --jp-brand-color1: var(--md-blue-500);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);

  --jp-accent-color0: var(--md-green-700);
  --jp-accent-color1: var(--md-green-500);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-700);
  --jp-warn-color1: var(--md-orange-500);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);

  --jp-error-color0: var(--md-red-700);
  --jp-error-color1: var(--md-red-500);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);

  --jp-success-color0: var(--md-green-700);
  --jp-success-color1: var(--md-green-500);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);

  --jp-info-color0: var(--md-cyan-700);
  --jp-info-color1: var(--md-cyan-500);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-editor-background: #f7f7f7;
  --jp-cell-editor-border-color: #cfcfcf;
  --jp-cell-editor-background-edit: var(--jp-ui-layout-color1);
  --jp-cell-editor-border-color-edit: var(--jp-brand-color1);
  --jp-cell-prompt-width: 100px;
  --jp-cell-prompt-font-family: 'Roboto Mono', monospace;
  --jp-cell-prompt-letter-spacing: 0px;
  --jp-cell-prompt-opacity: 1.0;
  --jp-cell-prompt-opacity-not-active: 0.4;
  --jp-cell-prompt-font-color-not-active: var(--md-grey-700);
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307FC1;
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #BF5B3D;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-scroll-padding: 100px;

  /* Console specific styles */

  --jp-console-background: var(--md-grey-100);

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--md-grey-400);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color0);
  --jp-toolbar-box-shadow: 0px 0px 2px 0px rgba(0,0,0,0.24);
  --jp-toolbar-header-margin: 4px 4px 0px 4px;
  --jp-toolbar-active-background: var(--md-grey-300);
}
</style><style>/* This file has code derived from PhosphorJS CSS files, as noted below. The license for this PhosphorJS code is:

Copyright (c) 2014-2017, PhosphorJS Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*/

/*
 * The following section is derived from https://github.com/phosphorjs/phosphor/blob/23b9d075ebc5b73ab148b6ebfc20af97f85714c4/packages/widgets/style/tabbar.css 
 * We've scoped the rules so that they are consistent with exactly our code.
 */

.jupyter-widgets.widget-tab > .p-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] {
  flex-direction: column;
}


.jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  flex-direction: row;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  flex-direction: column;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-hidden {
  display: none !important;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  transition: none;
}

/* End tabbar.css */
</style><style>/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * We assume that the CSS variables in
 * https://github.com/jupyterlab/jupyterlab/blob/master/src/default-theme/variables.css
 * have been defined.
 */

:root {
    --jp-widgets-color: var(--jp-content-font-color1);
    --jp-widgets-label-color: var(--jp-widgets-color);
    --jp-widgets-readout-color: var(--jp-widgets-color);
    --jp-widgets-font-size: var(--jp-ui-font-size1);
    --jp-widgets-margin: 2px;
    --jp-widgets-inline-height: 28px;
    --jp-widgets-inline-width: 300px;
    --jp-widgets-inline-width-short: calc(var(--jp-widgets-inline-width) / 2 - var(--jp-widgets-margin));
    --jp-widgets-inline-width-tiny: calc(var(--jp-widgets-inline-width-short) / 2 - var(--jp-widgets-margin));
    --jp-widgets-inline-margin: 4px; /* margin between inline elements */
    --jp-widgets-inline-label-width: 80px;
    --jp-widgets-border-width: var(--jp-border-width);
    --jp-widgets-vertical-height: 200px;
    --jp-widgets-horizontal-tab-height: 24px;
    --jp-widgets-horizontal-tab-width: 144px;
    --jp-widgets-horizontal-tab-top-border: 2px;
    --jp-widgets-progress-thickness: 20px;
    --jp-widgets-container-padding: 15px;
    --jp-widgets-input-padding: 4px;
    --jp-widgets-radio-item-height-adjustment: 8px;
    --jp-widgets-radio-item-height: calc(var(--jp-widgets-inline-height) - var(--jp-widgets-radio-item-height-adjustment));
    --jp-widgets-slider-track-thickness: 4px;
    --jp-widgets-slider-border-width: var(--jp-widgets-border-width);
    --jp-widgets-slider-handle-size: 16px;
    --jp-widgets-slider-handle-border-color: var(--jp-border-color1);
    --jp-widgets-slider-handle-background-color: var(--jp-layout-color1);
    --jp-widgets-slider-active-handle-color: var(--jp-brand-color1);
    --jp-widgets-menu-item-height: 24px;
    --jp-widgets-dropdown-arrow: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCAxOCAxOCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTggMTg7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDpub25lO30KPC9zdHlsZT4KPHBhdGggZD0iTTUuMiw1LjlMOSw5LjdsMy44LTMuOGwxLjIsMS4ybC00LjksNWwtNC45LTVMNS4yLDUuOXoiLz4KPHBhdGggY2xhc3M9InN0MCIgZD0iTTAtMC42aDE4djE4SDBWLTAuNnoiLz4KPC9zdmc+Cg");
    --jp-widgets-input-color: var(--jp-ui-font-color1);
    --jp-widgets-input-background-color: var(--jp-layout-color1);
    --jp-widgets-input-border-color: var(--jp-border-color1);
    --jp-widgets-input-focus-border-color: var(--jp-brand-color2);
    --jp-widgets-input-border-width: var(--jp-widgets-border-width);
    --jp-widgets-disabled-opacity: 0.6;

    /* From Material Design Lite */
    --md-shadow-key-umbra-opacity: 0.2;
    --md-shadow-key-penumbra-opacity: 0.14;
    --md-shadow-ambient-shadow-opacity: 0.12;
}

.jupyter-widgets {
    margin: var(--jp-widgets-margin);
    box-sizing: border-box;
    color: var(--jp-widgets-color);
    overflow: visible;
}

.jupyter-widgets.jupyter-widgets-disconnected::before {
    line-height: var(--jp-widgets-inline-height);
    height: var(--jp-widgets-inline-height);
}

.jp-Output-result > .jupyter-widgets {
    margin-left: 0;
    margin-right: 0;
}

/* vbox and hbox */

.widget-inline-hbox {
    /* Horizontal widgets */
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    align-items: baseline;
}

.widget-inline-vbox {
    /* Vertical Widgets */
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.widget-box {
    box-sizing: border-box;
    display: flex;
    margin: 0;
    overflow: auto;
}

.widget-gridbox {
    box-sizing: border-box;
    display: grid;
    margin: 0;
    overflow: auto;
}

.widget-hbox {
    flex-direction: row;
}

.widget-vbox {
    flex-direction: column;
}

/* General Button Styling */

.jupyter-button {
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 0px;
    padding-bottom: 0px;
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: center;
    font-size: var(--jp-widgets-font-size);
    cursor: pointer;

    height: var(--jp-widgets-inline-height);
    border: 0px solid;
    line-height: var(--jp-widgets-inline-height);
    box-shadow: none;

    color: var(--jp-ui-font-color1);
    background-color: var(--jp-layout-color2);
    border-color: var(--jp-border-color2);
    border: none;
    user-select: none;
}

.jupyter-button i.fa {
    margin-right: var(--jp-widgets-inline-margin);
    pointer-events: none;
}

.jupyter-button:empty:before {
    content: "\200b"; /* zero-width space */
}

.jupyter-widgets.jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

.jupyter-button i.fa.center {
    margin-right: 0;
}

.jupyter-button:hover:enabled, .jupyter-button:focus:enabled {
    /* MD Lite 2dp shadow */
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
                0 3px 1px -2px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity)),
                0 1px 5px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity));
}

.jupyter-button:active, .jupyter-button.mod-active {
    /* MD Lite 4dp shadow */
    box-shadow: 0 4px 5px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
                0 1px 10px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity)),
                0 2px 4px -1px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity));
    color: var(--jp-ui-font-color1);
    background-color: var(--jp-layout-color3);
}

.jupyter-button:focus:enabled {
    outline: 1px solid var(--jp-widgets-input-focus-border-color);
}

/* Button "Primary" Styling */

.jupyter-button.mod-primary {
    color: var(--jp-ui-inverse-font-color1, var(--jp-inverse-ui-font-color1));
    background-color: var(--jp-brand-color1);
}

.jupyter-button.mod-primary.mod-active {
    color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
    background-color: var(--jp-brand-color0);
}

.jupyter-button.mod-primary:active {
    color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
    background-color: var(--jp-brand-color0);
}

/* Button "Success" Styling */

.jupyter-button.mod-success {
    color: var(--jp-ui-inverse-font-color1, var(--jp-inverse-ui-font-color1));
    background-color: var(--jp-success-color1);
}

.jupyter-button.mod-success.mod-active {
    color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
    background-color: var(--jp-success-color0);
}

.jupyter-button.mod-success:active {
    color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
    background-color: var(--jp-success-color0);
}

 /* Button "Info" Styling */

.jupyter-button.mod-info {
    color: var(--jp-ui-inverse-font-color1, var(--jp-inverse-ui-font-color1));
    background-color: var(--jp-info-color1);
}

.jupyter-button.mod-info.mod-active {
    color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
    background-color: var(--jp-info-color0);
}

.jupyter-button.mod-info:active {
    color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
    background-color: var(--jp-info-color0);
}

/* Button "Warning" Styling */

.jupyter-button.mod-warning {
    color: var(--jp-ui-inverse-font-color1, var(--jp-inverse-ui-font-color1));
    background-color: var(--jp-warn-color1);
}

.jupyter-button.mod-warning.mod-active {
    color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
    background-color: var(--jp-warn-color0);
}

.jupyter-button.mod-warning:active {
    color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
    background-color: var(--jp-warn-color0);
}

/* Button "Danger" Styling */

.jupyter-button.mod-danger {
    color: var(--jp-ui-inverse-font-color1, var(--jp-inverse-ui-font-color1));
    background-color: var(--jp-error-color1);
}

.jupyter-button.mod-danger.mod-active {
    color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
    background-color: var(--jp-error-color0);
}

.jupyter-button.mod-danger:active {
    color: var(--jp-ui-inverse-font-color0, var(--jp-inverse-ui-font-color0));
    background-color: var(--jp-error-color0);
}

/* Widget Button, Widget Toggle Button, Widget Upload */

.widget-button, .widget-toggle-button, .widget-upload {
    width: var(--jp-widgets-inline-width-short);
}

/* Widget Label Styling */

/* Override Bootstrap label css */
.jupyter-widgets label {
    margin-bottom: initial;
}

.widget-label-basic {
    /* Basic Label */
    color: var(--jp-widgets-label-color);
    font-size: var(--jp-widgets-font-size);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: var(--jp-widgets-inline-height);
}

.widget-label {
    /* Label */
    color: var(--jp-widgets-label-color);
    font-size: var(--jp-widgets-font-size);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: var(--jp-widgets-inline-height);
}

.widget-inline-hbox .widget-label {
    /* Horizontal Widget Label */
    color: var(--jp-widgets-label-color);
    text-align: right;
    margin-right: calc( var(--jp-widgets-inline-margin) * 2 );
    width: var(--jp-widgets-inline-label-width);
    flex-shrink: 0;
}

.widget-inline-vbox .widget-label {
    /* Vertical Widget Label */
    color: var(--jp-widgets-label-color);
    text-align: center;
    line-height: var(--jp-widgets-inline-height);
}

/* Widget Readout Styling */

.widget-readout {
    color: var(--jp-widgets-readout-color);
    font-size: var(--jp-widgets-font-size);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    overflow: hidden;
    white-space: nowrap;
    text-align: center;
}

.widget-readout.overflow {
    /* Overflowing Readout */

    /* From Material Design Lite
        shadow-key-umbra-opacity: 0.2;
        shadow-key-penumbra-opacity: 0.14;
        shadow-ambient-shadow-opacity: 0.12;
     */
    -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                        0 3px 1px -2px rgba(0, 0, 0, 0.14),
                        0 1px 5px 0 rgba(0, 0, 0, 0.12);

    -moz-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                     0 3px 1px -2px rgba(0, 0, 0, 0.14),
                     0 1px 5px 0 rgba(0, 0, 0, 0.12);

    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                0 3px 1px -2px rgba(0, 0, 0, 0.14),
                0 1px 5px 0 rgba(0, 0, 0, 0.12);
}

.widget-inline-hbox .widget-readout {
    /* Horizontal Readout */
    text-align: center;
    max-width: var(--jp-widgets-inline-width-short);
    min-width: var(--jp-widgets-inline-width-tiny);
    margin-left: var(--jp-widgets-inline-margin);
}

.widget-inline-vbox .widget-readout {
    /* Vertical Readout */
    margin-top: var(--jp-widgets-inline-margin);
    /* as wide as the widget */
    width: inherit;
}

/* Widget Checkbox Styling */

.widget-checkbox {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-checkbox input[type="checkbox"] {
    margin: 0px calc( var(--jp-widgets-inline-margin) * 2 ) 0px 0px;
    line-height: var(--jp-widgets-inline-height);
    font-size: large;
    flex-grow: 1;
    flex-shrink: 0;
    align-self: center;
}

/* Widget Valid Styling */

.widget-valid {
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width-short);
    font-size: var(--jp-widgets-font-size);
}

.widget-valid i:before {
    line-height: var(--jp-widgets-inline-height);
    margin-right: var(--jp-widgets-inline-margin);
    margin-left: var(--jp-widgets-inline-margin);
}

.widget-valid.mod-valid i:before {
    color: green;
}

.widget-valid.mod-invalid i:before {
    color: red;
}

.widget-valid.mod-valid .widget-valid-readout {
    display: none;
}

/* Widget Text and TextArea Stying */

.widget-textarea, .widget-text {
    width: var(--jp-widgets-inline-width);
}

.widget-text input[type="text"], .widget-text input[type="number"], .widget-text input[type="password"] {
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-text input[type="text"]:disabled, .widget-text input[type="number"]:disabled, .widget-text input[type="password"]:disabled, .widget-textarea textarea:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

.widget-text input[type="text"], .widget-text input[type="number"], .widget-text input[type="password"], .widget-textarea textarea {
    box-sizing: border-box;
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    flex-grow: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    flex-shrink: 1;
    outline: none !important;
}
    
.widget-text input[type="text"], .widget-text input[type="password"], .widget-textarea textarea {
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2);
}

.widget-text input[type="number"] {
    padding: var(--jp-widgets-input-padding) 0 var(--jp-widgets-input-padding) calc(var(--jp-widgets-input-padding) *  2);
}

.widget-textarea textarea {
    height: inherit;
    width: inherit;
}

.widget-text input:focus, .widget-textarea textarea:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

/* Widget Slider */

.widget-slider .ui-slider {
    /* Slider Track */
    border: var(--jp-widgets-slider-border-width) solid var(--jp-layout-color3);
    background: var(--jp-layout-color3);
    box-sizing: border-box;
    position: relative;
    border-radius: 0px;
}

.widget-slider .ui-slider .ui-slider-handle {
    /* Slider Handle */
    outline: none !important; /* focused slider handles are colored - see below */
    position: absolute;
    background-color: var(--jp-widgets-slider-handle-background-color);
    border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-handle-border-color);
    box-sizing: border-box;
    z-index: 1;
    background-image: none; /* Override jquery-ui */
}

/* Override jquery-ui */
.widget-slider .ui-slider .ui-slider-handle:hover, .widget-slider .ui-slider .ui-slider-handle:focus {
    background-color: var(--jp-widgets-slider-active-handle-color);
    border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-active-handle-color);
}

.widget-slider .ui-slider .ui-slider-handle:active {
    background-color: var(--jp-widgets-slider-active-handle-color);
    border-color: var(--jp-widgets-slider-active-handle-color);
    z-index: 2;
    transform: scale(1.2);
}

.widget-slider  .ui-slider .ui-slider-range {
    /* Interval between the two specified value of a double slider */
    position: absolute;
    background: var(--jp-widgets-slider-active-handle-color);
    z-index: 0;
}

/* Shapes of Slider Handles */

.widget-hslider .ui-slider .ui-slider-handle {
    width: var(--jp-widgets-slider-handle-size);
    height: var(--jp-widgets-slider-handle-size);
    margin-top: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-handle-size)) / 2 - var(--jp-widgets-slider-border-width));
    margin-left: calc(var(--jp-widgets-slider-handle-size) / -2 + var(--jp-widgets-slider-border-width));
    border-radius: 50%;
    top: 0;
}

.widget-vslider .ui-slider .ui-slider-handle {
    width: var(--jp-widgets-slider-handle-size);
    height: var(--jp-widgets-slider-handle-size);
    margin-bottom: calc(var(--jp-widgets-slider-handle-size) / -2 + var(--jp-widgets-slider-border-width));
    margin-left: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-handle-size)) / 2 - var(--jp-widgets-slider-border-width));
    border-radius: 50%;
    left: 0;
}

.widget-hslider .ui-slider .ui-slider-range {
    height: calc( var(--jp-widgets-slider-track-thickness) * 2 );
    margin-top: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-track-thickness) * 2 ) / 2 - var(--jp-widgets-slider-border-width));
}

.widget-vslider .ui-slider .ui-slider-range {
    width: calc( var(--jp-widgets-slider-track-thickness) * 2 );
    margin-left: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-track-thickness) * 2 ) / 2 - var(--jp-widgets-slider-border-width));
}

/* Horizontal Slider */

.widget-hslider {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);

    /* Override the align-items baseline. This way, the description and readout
    still seem to align their baseline properly, and we don't have to have
    align-self: stretch in the .slider-container. */
    align-items: center;
}

.widgets-slider .slider-container {
    overflow: visible;
}

.widget-hslider .slider-container {
    height: var(--jp-widgets-inline-height);
    margin-left: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    margin-right: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    flex: 1 1 var(--jp-widgets-inline-width-short);
}

.widget-hslider .ui-slider {
    /* Inner, invisible slide div */
    height: var(--jp-widgets-slider-track-thickness);
    margin-top: calc((var(--jp-widgets-inline-height) - var(--jp-widgets-slider-track-thickness)) / 2);
    width: 100%;
}

/* Vertical Slider */

.widget-vbox .widget-label {
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-vslider {
    /* Vertical Slider */
    height: var(--jp-widgets-vertical-height);
    width: var(--jp-widgets-inline-width-tiny);
}

.widget-vslider .slider-container {
    flex: 1 1 var(--jp-widgets-inline-width-short);
    margin-left: auto;
    margin-right: auto;
    margin-bottom: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    margin-top: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    display: flex;
    flex-direction: column;
}

.widget-vslider .ui-slider-vertical {
    /* Inner, invisible slide div */
    width: var(--jp-widgets-slider-track-thickness);
    flex-grow: 1;
    margin-left: auto;
    margin-right: auto;
}

/* Widget Progress Styling */

.progress-bar {
    -webkit-transition: none;
    -moz-transition: none;
    -ms-transition: none;
    -o-transition: none;
    transition: none;
}

.progress-bar {
    height: var(--jp-widgets-inline-height);
}

.progress-bar {
    background-color: var(--jp-brand-color1);
}

.progress-bar-success {
    background-color: var(--jp-success-color1);
}

.progress-bar-info {
    background-color: var(--jp-info-color1);
}

.progress-bar-warning {
    background-color: var(--jp-warn-color1);
}

.progress-bar-danger {
    background-color: var(--jp-error-color1);
}

.progress {
    background-color: var(--jp-layout-color2);
    border: none;
    box-shadow: none;
}

/* Horisontal Progress */

.widget-hprogress {
    /* Progress Bar */
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width);
    align-items: center;

}

.widget-hprogress .progress {
    flex-grow: 1;
    margin-top: var(--jp-widgets-input-padding);
    margin-bottom: var(--jp-widgets-input-padding);
    align-self: stretch;
    /* Override bootstrap style */
    height: initial;
}

/* Vertical Progress */

.widget-vprogress {
    height: var(--jp-widgets-vertical-height);
    width: var(--jp-widgets-inline-width-tiny);
}

.widget-vprogress .progress {
    flex-grow: 1;
    width: var(--jp-widgets-progress-thickness);
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0;
}

/* Select Widget Styling */

.widget-dropdown {
    height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);
}

.widget-dropdown > select {
    padding-right: 20px;
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    border-radius: 0;
    height: inherit;
    flex: 1 1 var(--jp-widgets-inline-width-short);
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    box-sizing: border-box;
    outline: none !important;
    box-shadow: none;
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    vertical-align: top;
    padding-left: calc( var(--jp-widgets-input-padding) * 2);
	appearance: none;
	-webkit-appearance: none;
	-moz-appearance: none;
    background-repeat: no-repeat;
	background-size: 20px;
	background-position: right center;
    background-image: var(--jp-widgets-dropdown-arrow);
}
.widget-dropdown > select:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-dropdown > select:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* To disable the dotted border in Firefox around select controls.
   See http://stackoverflow.com/a/18853002 */
.widget-dropdown > select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 #000;
}

/* Select and SelectMultiple */

.widget-select {
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    align-items: flex-start;
}

.widget-select > select {
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    flex: 1 1 var(--jp-widgets-inline-width-short);
    outline: none !important;
    overflow: auto;
    height: inherit;

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    padding-top: 5px;
}

.widget-select > select:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.wiget-select > select > option {
    padding-left: var(--jp-widgets-input-padding);
    line-height: var(--jp-widgets-inline-height);
    /* line-height doesn't work on some browsers for select options */
    padding-top: calc(var(--jp-widgets-inline-height)-var(--jp-widgets-font-size)/2);
    padding-bottom: calc(var(--jp-widgets-inline-height)-var(--jp-widgets-font-size)/2);
}



/* Toggle Buttons Styling */

.widget-toggle-buttons {
    line-height: var(--jp-widgets-inline-height);
}

.widget-toggle-buttons .widget-toggle-button {
    margin-left: var(--jp-widgets-margin);
    margin-right: var(--jp-widgets-margin);
}

.widget-toggle-buttons .jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Radio Buttons Styling */

.widget-radio {
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);
}

.widget-radio-box {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    box-sizing: border-box;
    flex-grow: 1;
    margin-bottom: var(--jp-widgets-radio-item-height-adjustment);
}

.widget-radio-box label {
    height: var(--jp-widgets-radio-item-height);
    line-height: var(--jp-widgets-radio-item-height);
    font-size: var(--jp-widgets-font-size);
}

.widget-radio-box input {
    height: var(--jp-widgets-radio-item-height);
    line-height: var(--jp-widgets-radio-item-height);
    margin: 0 calc( var(--jp-widgets-input-padding) * 2 ) 0 1px;
    float: left;
}

/* Color Picker Styling */

.widget-colorpicker {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-colorpicker > .widget-colorpicker-input {
    flex-grow: 1;
    flex-shrink: 1;
    min-width: var(--jp-widgets-inline-width-tiny);
}

.widget-colorpicker input[type="color"] {
    width: var(--jp-widgets-inline-height);
    height: var(--jp-widgets-inline-height);
    padding: 0 2px; /* make the color square actually square on Chrome on OS X */
    background: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    border-left: none;
    flex-grow: 0;
    flex-shrink: 0;
    box-sizing: border-box;
    align-self: stretch;
    outline: none !important;
}

.widget-colorpicker.concise input[type="color"] {
    border-left: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
}

.widget-colorpicker input[type="color"]:focus, .widget-colorpicker input[type="text"]:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-colorpicker input[type="text"] {
    flex-grow: 1;
    outline: none !important;
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    background: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    font-size: var(--jp-widgets-font-size);
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2 );
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    flex-shrink: 1;
    box-sizing: border-box;
}

.widget-colorpicker input[type="text"]:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Date Picker Styling */

.widget-datepicker {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-datepicker input[type="date"] {
    flex-grow: 1;
    flex-shrink: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    outline: none !important;
    height: var(--jp-widgets-inline-height);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2 );
    box-sizing: border-box;
}

.widget-datepicker input[type="date"]:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-datepicker input[type="date"]:invalid {
    border-color: var(--jp-warn-color1);
}

.widget-datepicker input[type="date"]:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Play Widget */

.widget-play {
    width: var(--jp-widgets-inline-width-short);
    display: flex;
    align-items: stretch;
}

.widget-play .jupyter-button {
    flex-grow: 1;
    height: auto;
}

.widget-play .jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Tab Widget */

.jupyter-widgets.widget-tab {
    display: flex;
    flex-direction: column;
}

.jupyter-widgets.widget-tab > .p-TabBar {
    /* Necessary so that a tab can be shifted down to overlay the border of the box below. */
    overflow-x: visible;
    overflow-y: visible;
}

.jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
    /* Make sure that the tab grows from bottom up */
    align-items: flex-end;
    min-width: 0;
    min-height: 0;
}

.jupyter-widgets.widget-tab > .widget-tab-contents {
    width: 100%;
    box-sizing: border-box;
    margin: 0;
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    border: var(--jp-border-width) solid var(--jp-border-color1);
    padding: var(--jp-widgets-container-padding);
    flex-grow: 1;
    overflow: auto;
}

.jupyter-widgets.widget-tab > .p-TabBar {
    font: var(--jp-widgets-font-size) Helvetica, Arial, sans-serif;
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + var(--jp-border-width));
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
    flex: 0 1 var(--jp-widgets-horizontal-tab-width);
    min-width: 35px;
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + var(--jp-border-width));
    line-height: var(--jp-widgets-horizontal-tab-height);
    margin-left: calc(-1 * var(--jp-border-width));
    padding: 0px 10px;
    background: var(--jp-layout-color2);
    color: var(--jp-ui-font-color2);
    border: var(--jp-border-width) solid var(--jp-border-color1);
    border-bottom: none;
    position: relative;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current {
    color: var(--jp-ui-font-color0);
    /* We want the background to match the tab content background */
    background: var(--jp-layout-color1);
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + 2 * var(--jp-border-width));
    transform: translateY(var(--jp-border-width));
    overflow: visible;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current:before {
    position: absolute;
    top: calc(-1 * var(--jp-border-width));
    left: calc(-1 * var(--jp-border-width));
    content: '';
    height: var(--jp-widgets-horizontal-tab-top-border);
    width: calc(100% + 2 * var(--jp-border-width));
    background: var(--jp-brand-color1);
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:first-child {
    margin-left: 0;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:hover:not(.p-mod-current) {
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
}

.jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon {
    margin-left: 4px;
}

/* This font-awesome strategy may not work across FA4 and FA5, but we don't
actually support closable tabs, so it really doesn't matter */
.jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon:before {
    font-family: FontAwesome;
    content: '\f00d'; /* close */
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
    line-height: var(--jp-widgets-horizontal-tab-height);
}

/* Accordion Widget */

.p-Collapse {
    display: flex;
    flex-direction: column;
    align-items: stretch;
}

.p-Collapse-header {
    padding: var(--jp-widgets-input-padding);
    cursor: pointer;
    color: var(--jp-ui-font-color2);
    background-color: var(--jp-layout-color2);
    border: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    padding: calc(var(--jp-widgets-container-padding) * 2 / 3) var(--jp-widgets-container-padding);
    font-weight: bold;
}

.p-Collapse-header:hover {
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
}

.p-Collapse-open > .p-Collapse-header {
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color0);
    cursor: default;
    border-bottom: none;
}

.p-Collapse-contents {
    padding: var(--jp-widgets-container-padding);
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    border-left: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    border-right: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    border-bottom: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    overflow: auto;
}

.p-Accordion {
    display: flex;
    flex-direction: column;
    align-items: stretch;
}

.p-Accordion .p-Collapse {
    margin-bottom: 0;
}

.p-Accordion .p-Collapse + .p-Collapse {
    margin-top: 4px;
}



/* HTML widget */

.widget-html, .widget-htmlmath {
    font-size: var(--jp-widgets-font-size);
}

.widget-html > .widget-html-content, .widget-htmlmath > .widget-html-content {
    /* Fill out the area in the HTML widget */
    align-self: stretch;
    flex-grow: 1;
    flex-shrink: 1;
    /* Makes sure the baseline is still aligned with other elements */
    line-height: var(--jp-widgets-inline-height);
    /* Make it possible to have absolutely-positioned elements in the html */
    position: relative;
}


/* Image widget  */

.widget-image {
    max-width: 100%;
    height: auto;
}
</style><style>/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */
</style><link id="favicon" type="image/x-icon" rel="shortcut icon" href="http://localhost:8888/static/base/images/favicon-notebook.ico"></head>

<body class="notebook_app command_mode" data-jupyter-api-token="1223f29387a7f5a56e19ef855e00ac2ab20de58f5b17d110" data-base-url="/" data-ws-url="" data-notebook-name="Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb" data-notebook-path="Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb" dir="ltr"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div>

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=1223f29387a7f5a56e19ef855e00ac2ab20de58f5b17d110" title="dashboard">
      <img src="./Real-Time Age Gender Detection_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  


<span id="save_widget" class="save_widget">
    <span id="notebook_name" class="filename">Real-Time Age Gender Detection using OpenCV</span>
    <span class="checkpoint_status" title="Tue, Feb 14, 2023 8:21 PM">Last Checkpoint: 02/14/2023</span>
    <span class="autosave_status">(autosaved)</span>
</span>


  

<span id="kernel_logo_widget">
  
  <img class="current_kernel_logo" alt="Current Kernel Logo" src="./Real-Time Age Gender Detection_files/logo-64x64.png" title="Python 3 (ipykernel)" style="display: inline;">
  
</span>


  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
<div id="menubar-container" class="container">
<div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
            <button type="button" class="btn btn-default navbar-btn navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <i class="fa fa-bars"></i>
              <span class="navbar-text">Menu</span>
            </button>
            <p id="kernel_indicator" class="navbar-text indicator_area">
              <span class="kernel_indicator_name">Python 3 (ipykernel)</span>
              <i id="kernel_indicator_icon" class="kernel_idle_icon" title="Kernel Idle"></i>
            </p>
            <i id="readonly-indicator" class="navbar-text" title="This notebook is read-only" style="display: none;">
                <span class="fa-stack">
                    <i class="fa fa-save fa-stack-1x"></i>
                    <i class="fa fa-ban fa-stack-2x text-danger"></i>
                </span>
            </i>
            <i id="modal_indicator" class="navbar-text modal_indicator" title="Command Mode"></i>
            <span id="notification_area"><div id="notification_kernel" class="notification_widget btn btn-xs navbar-btn undefined info" style="display: none;"><span></span></div><div id="notification_notebook" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div><div id="notification_trusted" class="notification_widget btn btn-xs navbar-btn" style="cursor: help;" role="button" disabled="disabled"><span title="Javascript enabled for notebook display">Trusted</span></div><div id="notification_widgets" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div></span>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="dropdown-toggle" id="filelink" data-toggle="dropdown" aria-haspopup="true" aria-controls="file_menu">File</a>
                    <ul id="file_menu" class="dropdown-menu" role="menu" aria-labelledby="filelink">
                        <li id="new_notebook" class="menu_focus_highlight dropdown dropdown-submenu" role="none">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">New Notebook<span class="sr-only">Dropdown</span></a>
                            <ul class="dropdown-menu" id="menu-new-notebook-submenu" role="menu">
                            <li id="new-notebook-submenu-python3"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Python 3 (ipykernel)</a></li></ul>
                        </li>
                        <li id="open_notebook" role="none" title="Opens a new window with the Dashboard view">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Open...</a></li>
                        <!-- <hr/> -->
                        <li class="divider" role="none"></li>
                        <li id="copy_notebook" role="none" title="Open a copy of this notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Make a Copy...</a></li>
                        <li id="save_notebook_as" role="none" title="Save a copy of the notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Save as...</a></li>
                        <li id="rename_notebook" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Rename...</a></li>
                        <li id="save_checkpoint" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Save and Checkpoint</span><span class="kb"><kbd>Ctrl-S</kbd></span></a></li>
                        <!-- <hr/> -->
                        <li class="divider" role="none"></li>
                        <li id="restore_checkpoint" class="menu_focus_highlight dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Revert to Checkpoint<span class="sr-only">Dropdown</span></a>
                          <ul class="dropdown-menu"><li><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Tuesday, February 14, 2023 8:21 PM</a></li></ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="print_preview" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Print Preview</a></li>
                        <li class="dropdown-submenu menu_focus_highlight" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Download as<span class="sr-only">Dropdown</span></a>
                            <ul id="download_menu" class="dropdown-menu">
                                
                                <li id="download_asciidoc">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">AsciiDoc (.asciidoc)</a>
                                </li>
                                
                                <li id="download_html">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">HTML (.html)</a>
                                </li>
                                
                                <li id="download_latex">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">LaTeX (.tex)</a>
                                </li>
                                
                                <li id="download_markdown">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Markdown (.md)</a>
                                </li>
                                
                                <li id="download_notebook">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Notebook (.ipynb)</a>
                                </li>
                                
                                <li id="download_pdf">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">PDF via LaTeX (.pdf)</a>
                                </li>
                                
                                <li id="download_rst">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">reST (.rst)</a>
                                </li>
                                
                                <li id="download_script">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Python (.py)</a>
                                </li>
                                
                                <li id="download_slides">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Reveal.js slides (.slides.html)</a>
                                </li>
                                
                                <li id="download_webpdf">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">PDF via HTML (.html)</a>
                                </li>
                                
                            </ul>
                        </li>
                        <li class="dropdown-submenu hidden" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Deploy as</a>
                            <ul id="deploy_menu" class="dropdown-menu"></ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="trust_notebook" role="none" title="Trust the output of this notebook" class="disabled">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Trusted Notebook</a></li>
                        <li class="divider" role="none"></li>
                        <li id="close_and_halt" role="none" title="Shutdown this notebook&#39;s kernel, and close this window">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Close and Halt</a></li>
                    </ul>
                </li>

                <li class="dropdown"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="dropdown-toggle" id="editlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="edit_menu">Edit</a>
                    <ul id="edit_menu" class="dropdown-menu" role="menu" aria-labelledby="editlink">
                        <li id="cut_cell" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Cut Cells</span><span class="kb"><kbd>X</kbd></span></a></li>
                        <li id="copy_cell" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Copy Cells</span><span class="kb"><kbd>C</kbd></span></a></li>
                        <li id="paste_cell_above" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-disabled="true" class="menu-shortcut-container"><span class="action">Paste Cells Above</span><span class="kb"><kbd>Shift-V</kbd></span></a></li>
                        <li id="paste_cell_below" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-disabled="true" class="menu-shortcut-container"><span class="action">Paste Cells Below</span><span class="kb"><kbd>V</kbd></span></a></li>
                        <li id="paste_cell_replace" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-disabled="true">Paste Cells &amp; Replace</a></li>
                        <li id="delete_cell" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Delete Cells</span><span class="kb"><kbd>D</kbd>,<kbd>D</kbd></span></a></li>
                        <li id="undelete_cell" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-disabled="true" class="menu-shortcut-container"><span class="action">Undo Delete Cells</span><span class="kb"><kbd>Z</kbd></span></a></li>
                        <li class="divider" role="none"></li>
                        <li id="split_cell" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Split Cell</span><span class="kb"><kbd>Ctrl-Shift-Minus</kbd></span></a></li>
                        <li id="merge_cell_above" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Merge Cell Above</a></li>
                        <li id="merge_cell_below" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Merge Cell Below</a></li>
                        <li class="divider" role="none"></li>
                        <li id="move_cell_up" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Move Cell Up</a></li>
                        <li id="move_cell_down" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Move Cell Down</a></li>
                        <li class="divider" role="none"></li>
                        <li id="edit_nb_metadata" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Edit Notebook Metadata</a></li>
                        <li class="divider" role="none"></li>
                        <li id="find_and_replace" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem"> Find and Replace </a></li>
                        <li class="divider" role="none"></li>
                        <li id="cut_cell_attachments" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Cut Cell Attachments</a></li>
                        <li id="copy_cell_attachments" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Copy Cell Attachments</a></li>
                        <li id="paste_cell_attachments" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-disabled="true">Paste Cell Attachments</a></li>
                        <li class="divider" role="none"></li>
                        <li id="insert_image" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-disabled="true">  Insert Image </a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="dropdown-toggle" id="viewlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="view_menu">View</a>
                    <ul id="view_menu" class="dropdown-menu" role="menu" aria-labelledby="viewlink">
                        <li id="toggle_header" role="none" title="Show/Hide the logo and notebook title (above menu bar)">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Toggle Header</a>
                        </li>
                        <li id="toggle_toolbar" role="none" title="Show/Hide the action icons (below menu bar)">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Toggle Toolbar</a>
                        </li>
                        <li id="toggle_line_numbers" role="none" title="Show/Hide line numbers in cells">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Toggle Line Numbers</span><span class="kb"><kbd>Shift-L</kbd></span></a>
                        </li>
                        <li id="menu-cell-toolbar" class="menu_focus_highlight dropdown-submenu" role="none">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Cell Toolbar</a>
                            <ul class="dropdown-menu" id="menu-cell-toolbar-submenu"><li data-name="None"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">None</a></li><li data-name="Edit%20Metadata"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Edit Metadata</a></li><li data-name="Raw%20Cell%20Format"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Raw Cell Format</a></li><li data-name="Slideshow"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Slideshow</a></li><li data-name="Attachments"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Attachments</a></li><li data-name="Tags"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Tags</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="dropdown-toggle" id="insertlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="insert_menu">Insert</a>
                    <ul id="insert_menu" class="dropdown-menu" role="menu" aria-labelledby="insertlink">
                        <li id="insert_cell_above" role="none" title="Insert an empty Code cell above the currently active cell">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Insert Cell Above</span><span class="kb"><kbd>A</kbd></span></a></li>
                        <li id="insert_cell_below" role="none" title="Insert an empty Code cell below the currently active cell">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Insert Cell Below</span><span class="kb"><kbd>B</kbd></span></a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="dropdown-toggle" id="celllink" data-toggle="dropdown" aria-haspopup="true" aria-controls="cell_menu">Cell</a>
                    <ul id="cell_menu" class="dropdown-menu" role="menu" aria-labelledby="celllink">
                        <li id="run_cell" role="none" title="Run this cell, and move cursor to the next one">
                            <a role="menuitem" href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="menu-shortcut-container"><span class="action">Run Cells</span><span class="kb"><kbd>Ctrl-Enter</kbd></span></a></li>
                        <li id="run_cell_select_below" role="none" title="Run this cell, select below">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Run Cells and Select Below</span><span class="kb"><kbd>Shift-Enter</kbd></span></a></li>
                        <li id="run_cell_insert_below" role="none" title="Run this cell, insert below">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Run Cells and Insert Below</span><span class="kb"><kbd>Alt-Enter</kbd></span></a></li>
                        <li id="run_all_cells" role="none" title="Run all cells in the notebook">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Run All</a></li>
                        <li id="run_all_cells_above" role="none" title="Run all cells above (but not including) this cell">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Run All Above</a></li>
                        <li id="run_all_cells_below" role="none" title="Run this cell and all cells below it">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem">Run All Below</a></li>
                        <li class="divider" role="none"></li>
                        <li id="change_cell_type" class="menu_focus_highlight dropdown-submenu" role="none" title="All cells in the notebook have a cell type. By default, new cells are created as &#39;Code&#39; cells">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Cell Type</a>
                            <ul class="dropdown-menu" role="menu">
                              <li id="to_code" role="none" title="Contents will be sent to the kernel for execution, and output will display in the footer of cell">
                                  <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="menu-shortcut-container"><span class="action">Code</span><span class="kb"><kbd>Y</kbd></span></a></li>
                              <li id="to_markdown" title="Contents will be rendered as HTML and serve as explanatory text">
                                  <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="menu-shortcut-container"><span class="action">Markdown</span><span class="kb"><kbd>M</kbd></span></a></li>
                              <li id="to_raw" title="Contents will pass through nbconvert unmodified">
                                  <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="menu-shortcut-container"><span class="action">Raw NBConvert</span><span class="kb"><kbd>R</kbd></span></a></li>
                            </ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="current_outputs" class="menu_focus_highlight dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Current Outputs</a>
                            <ul class="dropdown-menu" role="menu">
                                <li id="toggle_current_output" role="none" title="Hide/Show the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="menu-shortcut-container"><span class="action">Toggle</span><span class="kb"><kbd>O</kbd></span></a>
                                </li>
                                <li id="toggle_current_output_scroll" title="Scroll the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="menu-shortcut-container"><span class="action">Toggle Scrolling</span><span class="kb"><kbd>Shift-O</kbd></span></a>
                                </li>
                                <li id="clear_current_output" title="Clear the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Clear</a>
                                </li>
                            </ul>
                        </li>
                        <li id="all_outputs" class="menu_focus_highlight dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">All Output</a>
                            <ul class="dropdown-menu" role="menu">
                                <li id="toggle_all_output" role="none" title="Hide/Show the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Toggle</a>
                                </li>
                                <li id="toggle_all_output_scroll" title="Scroll the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_all_output" title="Clear the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Clear</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="dropdown-toggle" data-toggle="dropdown" id="kernellink">Kernel</a>
                    <ul id="kernel_menu" class="dropdown-menu" aria-labelledby="kernellink">
                        <li id="int_kernel" title="Send Keyboard Interrupt (CTRL-C) to the Kernel">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="menu-shortcut-container"><span class="action">Interrupt</span><span class="kb"><kbd>I</kbd>,<kbd>I</kbd></span></a>
                        </li>
                        <li id="restart_kernel" title="Restart the Kernel">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="menu-shortcut-container"><span class="action">Restart</span><span class="kb"><kbd>0</kbd>,<kbd>0</kbd></span></a>
                        </li>
                        <li id="restart_clear_output" title="Restart the Kernel and clear all output">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Restart &amp; Clear Output</a>
                        </li>
                        <li id="restart_run_all" title="Restart the Kernel and re-run the notebook">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Restart &amp; Run All</a>
                        </li>
                        <li id="reconnect_kernel" title="Reconnect to the Kernel">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Reconnect</a>
                        </li>
                        <li id="shutdown_kernel" title="Shutdown the Kernel">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Shutdown</a>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="menu-change-kernel" class="menu_focus_highlight dropdown-submenu" role="menuitem">
                            <a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Change kernel</a>
                            <ul class="dropdown-menu" id="menu-change-kernel-submenu"><li id="kernel-submenu-python3"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Python 3 (ipykernel)</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" data-toggle="dropdown" class="dropdown-toggle">Widgets</a><ul id="widget-submenu" class="dropdown-menu"><li title="Save the notebook with the widget state information for static rendering"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Save Notebook Widget State</a></li><li title="Clear the widget state information from the notebook"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Clear Notebook Widget State</a></li><ul class="divider"></ul><li title="Download the widget state as a JSON file"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Download Widget State</a></li><li title="Embed interactive widgets"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Embed Widgets</a></li></ul></li><li class="dropdown"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="dropdown-toggle" data-toggle="dropdown">Help</a>
                    <ul id="help_menu" class="dropdown-menu">
                        
                        <li id="notebook_tour" title="A quick tour of the notebook user interface"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">User Interface Tour</a></li>
                        <li id="keyboard_shortcuts" title="Opens a tooltip with all keyboard shortcuts"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" class="menu-shortcut-container"><span class="action">Keyboard Shortcuts</span><span class="kb"><kbd>H</kbd></span></a></li>
                        <li id="edit_keyboard_shortcuts" title="Opens a dialog allowing you to edit Keyboard shortcuts"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">Edit Keyboard Shortcuts</a></li>
                        <li class="divider"></li>
                        

						
                        
                            
                                <li><a rel="noreferrer" href="http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Notebook Help
                                </a></li>
                            
                                <li><a rel="noreferrer" href="https://help.github.com/articles/markdown-basics/" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Markdown
                                </a></li>
                            
                            
                        
                        <li id="kernel-help-links" class="divider"></li><li><a target="_blank" title="Opens in a new window" href="https://docs.python.org/3.9?v=20230307183922"><i class="fa fa-external-link menu-icon pull-right"></i><span>Python Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://ipython.org/documentation.html?v=20230307183922"><i class="fa fa-external-link menu-icon pull-right"></i><span>IPython Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://docs.scipy.org/doc/numpy/reference/?v=20230307183922"><i class="fa fa-external-link menu-icon pull-right"></i><span>NumPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://docs.scipy.org/doc/scipy/reference/?v=20230307183922"><i class="fa fa-external-link menu-icon pull-right"></i><span>SciPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://matplotlib.org/contents.html?v=20230307183922"><i class="fa fa-external-link menu-icon pull-right"></i><span>Matplotlib Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="http://docs.sympy.org/latest/index.html?v=20230307183922"><i class="fa fa-external-link menu-icon pull-right"></i><span>SymPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://pandas.pydata.org/pandas-docs/stable/?v=20230307183922"><i class="fa fa-external-link menu-icon pull-right"></i><span>pandas Reference</span></a></li><li class="divider"></li>
                        <li title="About Jupyter Notebook"><a id="notebook_about" href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#">About</a></li>
                        
                    </ul>
                </li>
              </ul>
            </div>
        </div>
    </div>
</div>

<div id="maintoolbar" class="navbar">
  <div class="toolbar-inner navbar-inner navbar-nobg">
    <div id="maintoolbar-container" class="container toolbar"><div class="btn-group" id="save-notbook"><button class="btn btn-default" title="Save and Checkpoint" data-jupyter-action="jupyter-notebook:save-notebook"><i class="fa-save fa"></i></button></div><div class="btn-group" id="insert_above_below"><button class="btn btn-default" title="insert cell below" data-jupyter-action="jupyter-notebook:insert-cell-below"><i class="fa-plus fa"></i></button></div><div class="btn-group" id="cut_copy_paste"><button class="btn btn-default" title="cut selected cells" data-jupyter-action="jupyter-notebook:cut-cell"><i class="fa-cut fa"></i></button><button class="btn btn-default" title="copy selected cells" data-jupyter-action="jupyter-notebook:copy-cell"><i class="fa-copy fa"></i></button><button class="btn btn-default" title="paste cells below" data-jupyter-action="jupyter-notebook:paste-cell-below"><i class="fa-paste fa"></i></button></div><div class="btn-group" id="move_up_down"><button class="btn btn-default" title="move selected cells up" data-jupyter-action="jupyter-notebook:move-cell-up"><i class="fa-arrow-up fa"></i></button><button class="btn btn-default" title="move selected cells down" data-jupyter-action="jupyter-notebook:move-cell-down"><i class="fa-arrow-down fa"></i></button></div><div class="btn-group" id="run_int"><button class="btn btn-default" aria-label="Run" title="run cell, select below" data-jupyter-action="jupyter-notebook:run-cell-and-select-next"><i class="fa-play fa"></i><span class="toolbar-btn-label">Run</span></button><button class="btn btn-default" title="interrupt the kernel" data-jupyter-action="jupyter-notebook:interrupt-kernel"><i class="fa-stop fa"></i></button><button class="btn btn-default" title="restart the kernel (with dialog)" data-jupyter-action="jupyter-notebook:confirm-restart-kernel"><i class="fa-repeat fa"></i></button><button class="btn btn-default" title="restart the kernel, then re-run the whole notebook (with dialog)" data-jupyter-action="jupyter-notebook:confirm-restart-kernel-and-run-all-cells"><i class="fa-forward fa"></i></button></div><select id="cell_type" aria-label="combobox, select cell type" role="combobox" class="form-control select-xs"><option value="code">Code</option><option value="markdown">Markdown</option><option value="raw">Raw NBConvert</option><option value="heading">Heading</option><option value="multiselect" disabled="disabled" style="display: none;">-</option></select><div class="btn-group" id="cmd_palette"><button class="btn btn-default" title="open the command palette" data-jupyter-action="jupyter-notebook:show-command-palette"><i class="fa-keyboard-o fa"></i></button></div></div>
  </div>
</div>
</div>

<div class="lower-header-bar"></div>

</div>

<div id="site" style="display: block; height: 498.875px;">


<div id="ipython-main-app">
    <div id="notebook_panel">
        <div id="notebook" tabindex="-1"><div class="container" id="notebook-container"><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[7]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 56.5938px; left: 119.469px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 122.469px; margin-bottom: -17px; border-right-width: 33px; min-height: 79px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 119.469px; top: 51px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">cv2</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">math</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">time</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">argparse</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 33px; width: 1px; border-bottom: 0px solid transparent; top: 79px;"></div><div class="CodeMirror-gutters" style="display: none; height: 112px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[8]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 379.594px; left: 265.734px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 522.859px; margin-bottom: -17px; border-right-width: 33px; min-height: 402px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 265.734px; top: 374px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">getFaceBox</span>(<span class="cm-variable">net</span>, <span class="cm-variable">frame</span>,<span class="cm-variable">conf_threshold</span> <span class="cm-operator">=</span> <span class="cm-number">0.75</span>):</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">frameOpencvDnn</span> <span class="cm-operator">=</span> <span class="cm-variable">frame</span>.<span class="cm-property">copy</span>()</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">frameHeight</span> <span class="cm-operator">=</span> <span class="cm-variable">frameOpencvDnn</span>.<span class="cm-property">shape</span>[<span class="cm-number">0</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">frameWidth</span> <span class="cm-operator">=</span> <span class="cm-variable">frameOpencvDnn</span>.<span class="cm-property">shape</span>[<span class="cm-number">1</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">blob</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">dnn</span>.<span class="cm-property">blobFromImage</span>(<span class="cm-variable">frameOpencvDnn</span>,<span class="cm-number">1.0</span>,(<span class="cm-number">300</span>,<span class="cm-number">300</span>),</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">                                 [<span class="cm-number">104</span>, <span class="cm-number">117</span>, <span class="cm-number">123</span>], <span class="cm-keyword">True</span>, <span class="cm-keyword">False</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">net</span>.<span class="cm-property">setInput</span>(<span class="cm-variable">blob</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">detections</span> <span class="cm-operator">=</span> <span class="cm-variable">net</span>.<span class="cm-property">forward</span>()</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">bboxes</span> <span class="cm-operator">=</span> []</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">for</span> <span class="cm-variable">i</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-variable">detections</span>.<span class="cm-property">shape</span>[<span class="cm-number">2</span>]):</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">confidence</span> <span class="cm-operator">=</span> <span class="cm-variable">detections</span>[<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-variable">i</span>,<span class="cm-number">2</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-keyword">if</span> <span class="cm-variable">confidence</span> <span class="cm-operator">&gt;</span> <span class="cm-variable">conf_threshold</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">            <span class="cm-variable">x1</span> <span class="cm-operator">=</span> <span class="cm-builtin">int</span>(<span class="cm-variable">detections</span>[<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-variable">i</span>,<span class="cm-number">3</span>]<span class="cm-operator">*</span> <span class="cm-variable">frameWidth</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">            <span class="cm-variable">y1</span> <span class="cm-operator">=</span> <span class="cm-builtin">int</span>(<span class="cm-variable">detections</span>[<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-variable">i</span>,<span class="cm-number">4</span>]<span class="cm-operator">*</span> <span class="cm-variable">frameHeight</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">            <span class="cm-variable">x2</span> <span class="cm-operator">=</span> <span class="cm-builtin">int</span>(<span class="cm-variable">detections</span>[<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-variable">i</span>,<span class="cm-number">5</span>]<span class="cm-operator">*</span> <span class="cm-variable">frameWidth</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">            <span class="cm-variable">y2</span> <span class="cm-operator">=</span> <span class="cm-builtin">int</span>(<span class="cm-variable">detections</span>[<span class="cm-number">0</span>,<span class="cm-number">0</span>,<span class="cm-variable">i</span>,<span class="cm-number">6</span>]<span class="cm-operator">*</span> <span class="cm-variable">frameHeight</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">            <span class="cm-variable">bboxes</span>.<span class="cm-property">append</span>([<span class="cm-variable">x1</span>,<span class="cm-variable">y1</span>,<span class="cm-variable">x2</span>,<span class="cm-variable">y2</span>])</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">            <span class="cm-variable">cv2</span>.<span class="cm-property">rectangle</span>(<span class="cm-variable">frameOpencvDnn</span>,(<span class="cm-variable">x1</span>,<span class="cm-variable">y1</span>),(<span class="cm-variable">x2</span>,<span class="cm-variable">y2</span>),(<span class="cm-number">0</span>,<span class="cm-number">255</span>,<span class="cm-number">0</span>),</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">                          <span class="cm-builtin">int</span>(<span class="cm-builtin">round</span>(<span class="cm-variable">frameHeight</span><span class="cm-operator">/</span><span class="cm-number">150</span>)),<span class="cm-number">8</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">return</span> <span class="cm-variable">frameOpencvDnn</span> , <span class="cm-variable">bboxes</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 33px; width: 1px; border-bottom: 0px solid transparent; top: 402px;"></div><div class="CodeMirror-gutters" style="display: none; height: 435px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[11]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 192.594px; left: 242.672px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 730.719px; margin-bottom: -17px; border-right-width: 33px; min-height: 215px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 242.672px; top: 187px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">faceProto</span> <span class="cm-operator">=</span> <span class="cm-string">"opencv_face_detector.pbtxt"</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">faceModel</span> <span class="cm-operator">=</span> <span class="cm-string">"opencv_face_detector_uint8.pb"</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">ageProto</span> <span class="cm-operator">=</span> <span class="cm-string">"age_deploy.prototxt"</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">ageModel</span> <span class="cm-operator">=</span> <span class="cm-string">"age_net.caffemodel"</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">genderProto</span> <span class="cm-operator">=</span> <span class="cm-string">"gender_deploy.prototxt"</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">genderModel</span> <span class="cm-operator">=</span> <span class="cm-string">"gender_net.caffemodel"</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">MODEL_MEAN_VALUES</span> <span class="cm-operator">=</span> (<span class="cm-number">78.4263377603</span>, <span class="cm-number">87.7689143744</span>, <span class="cm-number">114.895847746</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">ageList</span> <span class="cm-operator">=</span> [<span class="cm-string">'(0-2)'</span>, <span class="cm-string">'(4-6)'</span>, <span class="cm-string">'(8-12)'</span>, <span class="cm-string">'(15-20)'</span>, <span class="cm-string">'(25-32)'</span>, <span class="cm-string">'(38-43)'</span>, <span class="cm-string">'(48-53)'</span>, <span class="cm-string">'(60-100)'</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">genderList</span> <span class="cm-operator">=</span> [<span class="cm-string">'Male'</span>, <span class="cm-string">'Female'</span>]</span></pre></div></div></div></div></div><div style="position: absolute; height: 33px; width: 1px; border-bottom: 0px solid transparent; top: 215px;"></div><div class="CodeMirror-gutters" style="display: none; height: 248px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[12]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 107.594px; left: 96.4062px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 415.031px; margin-bottom: -17px; border-right-width: 33px; min-height: 130px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 96.4062px; top: 102px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment">#load the network</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">ageNet</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">dnn</span>.<span class="cm-property">readNet</span>(<span class="cm-variable">ageModel</span>,<span class="cm-variable">ageProto</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">genderNet</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">dnn</span>.<span class="cm-property">readNet</span>(<span class="cm-variable">genderModel</span>, <span class="cm-variable">genderProto</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">faceNet</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">dnn</span>.<span class="cm-property">readNet</span>(<span class="cm-variable">faceModel</span>, <span class="cm-variable">faceProto</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">cap</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">VideoCapture</span>(<span class="cm-number">0</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">padding</span> <span class="cm-operator">=</span> <span class="cm-number">20</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 33px; width: 1px; border-bottom: 0px solid transparent; top: 130px;"></div><div class="CodeMirror-gutters" style="display: none; height: 163px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[13]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 583.594px; left: 388.969px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="bottom: 0px;"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 946.297px; margin-bottom: -17px; border-right-width: 33px; min-height: 606px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 388.969px; top: 578px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">while</span> <span class="cm-variable">cv2</span>.<span class="cm-property">waitKey</span>(<span class="cm-number">1</span>) <span class="cm-operator">&lt;</span> <span class="cm-number">0</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-comment">#read frame</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">t</span> <span class="cm-operator">=</span> <span class="cm-variable">time</span>.<span class="cm-property">time</span>()</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">hasFrame</span> , <span class="cm-variable">frame</span> <span class="cm-operator">=</span> <span class="cm-variable">cap</span>.<span class="cm-property">read</span>()</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">if</span> <span class="cm-keyword">not</span> <span class="cm-variable">hasFrame</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">cv2</span>.<span class="cm-property">waitKey</span>()</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-keyword">break</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-comment">#creating a smaller frame for better optimization</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">small_frame</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">resize</span>(<span class="cm-variable">frame</span>,(<span class="cm-number">0</span>,<span class="cm-number">0</span>),<span class="cm-variable">fx</span> <span class="cm-operator">=</span> <span class="cm-number">0.5</span>,<span class="cm-variable">fy</span> <span class="cm-operator">=</span> <span class="cm-number">0.5</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">frameFace</span> ,<span class="cm-variable">bboxes</span> <span class="cm-operator">=</span> <span class="cm-variable">getFaceBox</span>(<span class="cm-variable">faceNet</span>,<span class="cm-variable">small_frame</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">if</span> <span class="cm-keyword">not</span> <span class="cm-variable">bboxes</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-builtin">print</span>(<span class="cm-string">"No face Detected, Checking next frame"</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-keyword">continue</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">for</span> <span class="cm-variable">bbox</span> <span class="cm-keyword">in</span> <span class="cm-variable">bboxes</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">face</span> <span class="cm-operator">=</span> <span class="cm-variable">small_frame</span>[<span class="cm-builtin">max</span>(<span class="cm-number">0</span>,<span class="cm-variable">bbox</span>[<span class="cm-number">1</span>]<span class="cm-operator">-</span><span class="cm-variable">padding</span>):<span class="cm-builtin">min</span>(<span class="cm-variable">bbox</span>[<span class="cm-number">3</span>]<span class="cm-operator">+</span><span class="cm-variable">padding</span>,<span class="cm-variable">frame</span>.<span class="cm-property">shape</span>[<span class="cm-number">0</span>]<span class="cm-operator">-</span><span class="cm-number">1</span>),</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">                <span class="cm-builtin">max</span>(<span class="cm-number">0</span>,<span class="cm-variable">bbox</span>[<span class="cm-number">0</span>]<span class="cm-operator">-</span><span class="cm-variable">padding</span>):<span class="cm-builtin">min</span>(<span class="cm-variable">bbox</span>[<span class="cm-number">2</span>]<span class="cm-operator">+</span><span class="cm-variable">padding</span>, <span class="cm-variable">frame</span>.<span class="cm-property">shape</span>[<span class="cm-number">1</span>]<span class="cm-operator">-</span><span class="cm-number">1</span>)]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">blob</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">dnn</span>.<span class="cm-property">blobFromImage</span>(<span class="cm-variable">face</span>, <span class="cm-number">1.0</span>, (<span class="cm-number">227</span>, <span class="cm-number">227</span>), <span class="cm-variable">MODEL_MEAN_VALUES</span>, <span class="cm-variable">swapRB</span><span class="cm-operator">=</span><span class="cm-keyword">False</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">genderNet</span>.<span class="cm-property">setInput</span>(<span class="cm-variable">blob</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">genderPreds</span> <span class="cm-operator">=</span> <span class="cm-variable">genderNet</span>.<span class="cm-property">forward</span>()</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">gender</span> <span class="cm-operator">=</span> <span class="cm-variable">genderList</span>[<span class="cm-variable">genderPreds</span>[<span class="cm-number">0</span>].<span class="cm-property">argmax</span>()]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-builtin">print</span>(<span class="cm-string">"Gender : {}, conf = {:.3f}"</span>.<span class="cm-property">format</span>(<span class="cm-variable">gender</span>, <span class="cm-variable">genderPreds</span>[<span class="cm-number">0</span>].<span class="cm-property">max</span>()))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">ageNet</span>.<span class="cm-property">setInput</span>(<span class="cm-variable">blob</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">agePreds</span> <span class="cm-operator">=</span> <span class="cm-variable">ageNet</span>.<span class="cm-property">forward</span>()</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">age</span> <span class="cm-operator">=</span> <span class="cm-variable">ageList</span>[<span class="cm-variable">agePreds</span>[<span class="cm-number">0</span>].<span class="cm-property">argmax</span>()]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-builtin">print</span>(<span class="cm-string">"Age Output : {}"</span>.<span class="cm-property">format</span>(<span class="cm-variable">agePreds</span>))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-builtin">print</span>(<span class="cm-string">"Age : {}, conf = {:.3f}"</span>.<span class="cm-property">format</span>(<span class="cm-variable">age</span>, <span class="cm-variable">agePreds</span>[<span class="cm-number">0</span>].<span class="cm-property">max</span>()))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">label</span> <span class="cm-operator">=</span> <span class="cm-string">"{},{}"</span>.<span class="cm-property">format</span>(<span class="cm-variable">gender</span>, <span class="cm-variable">age</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">cv2</span>.<span class="cm-property">putText</span>(<span class="cm-variable">frameFace</span>, <span class="cm-variable">label</span>, (<span class="cm-variable">bbox</span>[<span class="cm-number">0</span>], <span class="cm-variable">bbox</span>[<span class="cm-number">1</span>]<span class="cm-operator">-</span><span class="cm-number">10</span>), <span class="cm-variable">cv2</span>.<span class="cm-property">FONT_HERSHEY_SIMPLEX</span>, <span class="cm-number">0.8</span>, (<span class="cm-number">0</span>, <span class="cm-number">255</span>, <span class="cm-number">255</span>), <span class="cm-number">2</span>, <span class="cm-variable">cv2</span>.<span class="cm-property">LINE_AA</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">cv2</span>.<span class="cm-property">imshow</span>(<span class="cm-string">"Age Gender Demo"</span>, <span class="cm-variable">frameFace</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">       </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-null cm-error">    </span><span class="cm-builtin">print</span>(<span class="cm-string">"time : {:.3f}"</span>.<span class="cm-property">format</span>(<span class="cm-variable">time</span>.<span class="cm-property">time</span>() <span class="cm-operator">-</span> <span class="cm-variable">t</span>))</span></pre></div></div></div></div></div><div style="position: absolute; height: 33px; width: 1px; border-bottom: 0px solid transparent; top: 606px;"></div><div class="CodeMirror-gutters" style="display: none; height: 639px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to unscroll output; double click to hide"></div><div class="output output_scroll"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.985
Age Output : [[0.01798835 0.05146371 0.08423866 0.04323056 0.32332736 0.42546952
  0.01715979 0.03712213]]
Age : (38-43), conf = 0.425
time : 0.216
Gender : Male, conf = 0.909
Age Output : [[1.3046450e-04 1.4448238e-03 1.0140065e-02 2.5533466e-02 6.7083113e-02
  8.9410514e-01 3.4342441e-04 1.2193952e-03]]
Age : (38-43), conf = 0.894
time : 0.115
Gender : Male, conf = 0.966
Age Output : [[2.2140300e-04 4.3292712e-02 1.5922068e-01 2.8924683e-01 2.4976312e-01
  2.5767633e-01 2.0132236e-04 3.7754286e-04]]
Age : (15-20), conf = 0.289
time : 0.125
Gender : Male, conf = 0.931
Age Output : [[5.1756502e-05 4.3625953e-03 4.0433057e-02 8.9806110e-02 4.4793832e-01
  4.1687787e-01 1.7363534e-04 3.5664541e-04]]
Age : (25-32), conf = 0.448
time : 0.098
Gender : Male, conf = 0.972
Age Output : [[7.9911588e-05 5.9101218e-04 7.2869047e-04 8.6781074e-04 7.5341664e-02
  9.1870743e-01 2.9065053e-03 7.7705295e-04]]
Age : (38-43), conf = 0.919
time : 0.118
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.999
Age Output : [[7.6000833e-07 4.0514233e-06 2.4616954e-04 4.4938289e-03 3.9152396e-01
  5.9969914e-01 2.4555535e-03 1.5765289e-03]]
Age : (38-43), conf = 0.600
time : 0.094
Gender : Male, conf = 0.999
Age Output : [[7.6000833e-07 4.0514233e-06 2.4616954e-04 4.4938289e-03 3.9152396e-01
  5.9969914e-01 2.4555535e-03 1.5765289e-03]]
Age : (38-43), conf = 0.600
time : 0.098
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.988
Age Output : [[0.00379296 0.00546913 0.00896626 0.09759425 0.4448655  0.3580461
  0.03523748 0.04602821]]
Age : (25-32), conf = 0.445
time : 0.102
Gender : Male, conf = 0.988
Age Output : [[0.00379296 0.00546913 0.00896626 0.09759425 0.4448655  0.3580461
  0.03523748 0.04602821]]
Age : (25-32), conf = 0.445
time : 0.105
Gender : Male, conf = 0.994
Age Output : [[0.00149349 0.0025181  0.00726723 0.0197972  0.2843906  0.5911561
  0.02442885 0.06894843]]
Age : (38-43), conf = 0.591
time : 0.108
Gender : Male, conf = 0.989
Age Output : [[8.4815019e-06 1.8270765e-04 3.2923605e-02 6.7456178e-02 6.3677013e-01
  2.6069680e-01 1.0092269e-03 9.5287838e-04]]
Age : (25-32), conf = 0.637
time : 0.103
Gender : Male, conf = 0.995
Age Output : [[9.2159571e-05 1.9476378e-03 5.6384150e-02 2.2767369e-01 3.1556383e-01
  3.8438427e-01 5.9622610e-03 7.9919007e-03]]
Age : (38-43), conf = 0.384
time : 0.107
Gender : Male, conf = 0.995
Age Output : [[2.6794125e-05 8.4796496e-04 5.3696733e-02 2.7677992e-01 2.5634524e-01
  4.0481743e-01 2.7889237e-03 4.6969499e-03]]
Age : (38-43), conf = 0.405
time : 0.090
Gender : Male, conf = 0.998
Age Output : [[3.4625054e-06 1.6531117e-04 2.3517022e-01 4.0300968e-01 1.4738025e-01
  2.1390082e-01 6.3943851e-05 3.0637029e-04]]
Age : (15-20), conf = 0.403
time : 0.096
Gender : Male, conf = 0.998
Age Output : [[2.6964544e-06 2.3283076e-04 3.7599674e-01 2.0965558e-01 2.1172079e-01
  2.0184799e-01 7.6098062e-05 4.6730958e-04]]
Age : (8-12), conf = 0.376
time : 0.081
Gender : Male, conf = 0.997
Age Output : [[1.2007155e-06 4.2194202e-05 4.7116935e-02 2.9688281e-01 2.2711371e-01
  4.2857319e-01 4.3162232e-05 2.2688106e-04]]
Age : (38-43), conf = 0.429
time : 0.104
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.999
Age Output : [[6.3663967e-05 1.2407138e-03 2.1334971e-01 4.9219498e-01 6.5523207e-02
  2.2596736e-01 1.9652802e-04 1.4637987e-03]]
Age : (15-20), conf = 0.492
time : 0.081
Gender : Male, conf = 0.968
Age Output : [[2.9387986e-04 8.5479636e-03 3.9910510e-02 4.1252872e-01 3.7408993e-01
  1.6300656e-01 5.3515192e-04 1.0873018e-03]]
Age : (15-20), conf = 0.413
time : 0.085
Gender : Male, conf = 0.993
Age Output : [[0.0088159  0.39500028 0.08417628 0.32235277 0.11204841 0.07524645
  0.00096329 0.00139663]]
Age : (4-6), conf = 0.395
time : 0.102
Gender : Male, conf = 0.994
Age Output : [[0.00122777 0.01285955 0.06213171 0.1931383  0.42362827 0.30508444
  0.00092658 0.00100346]]
Age : (25-32), conf = 0.424
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[0.00502381 0.09154598 0.06340625 0.14569122 0.30751356 0.37812984
  0.00403979 0.00464954]]
Age : (38-43), conf = 0.378
time : 0.103
Gender : Male, conf = 0.993
Age Output : [[0.01489544 0.56494796 0.12924899 0.03168789 0.17527965 0.07853332
  0.00324334 0.00216339]]
Age : (4-6), conf = 0.565
time : 0.085
Gender : Male, conf = 0.993
Age Output : [[0.01489544 0.56494796 0.12924899 0.03168789 0.17527965 0.07853332
  0.00324334 0.00216339]]
Age : (4-6), conf = 0.565
time : 0.102
Gender : Male, conf = 0.987
Age Output : [[0.00255912 0.03287851 0.07076821 0.05754727 0.20686604 0.621234
  0.00290541 0.00524148]]
Age : (38-43), conf = 0.621
time : 0.082
Gender : Male, conf = 0.935
Age Output : [[0.00154237 0.00727568 0.02010678 0.08444816 0.24817091 0.62985045
  0.00317729 0.00542842]]
Age : (38-43), conf = 0.630
time : 0.099
Gender : Male, conf = 0.983
Age Output : [[0.0024925  0.06240255 0.09099004 0.35296413 0.25105995 0.23769146
  0.00110361 0.00129582]]
Age : (15-20), conf = 0.353
time : 0.091
Gender : Male, conf = 0.944
Age Output : [[0.00052553 0.01748464 0.13586755 0.32828718 0.3572436  0.15954833
  0.0004417  0.00060148]]
Age : (25-32), conf = 0.357
time : 0.104
Gender : Male, conf = 0.982
Age Output : [[2.7416131e-04 5.0111143e-03 2.9422877e-02 4.2138454e-01 1.8871416e-01
  3.4121612e-01 4.6182331e-03 9.3587739e-03]]
Age : (15-20), conf = 0.421
time : 0.097
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.975
Age Output : [[0.00050579 0.00267479 0.00885926 0.23437941 0.4864536  0.2626841
  0.00077822 0.00366489]]
Age : (25-32), conf = 0.486
time : 0.106
Gender : Male, conf = 0.947
Age Output : [[2.7656471e-04 1.7960824e-02 2.3138877e-02 6.1471379e-01 2.3577039e-01
  1.0722426e-01 3.0702053e-04 6.0830638e-04]]
Age : (15-20), conf = 0.615
time : 0.114
Gender : Male, conf = 0.940
Age Output : [[4.1242890e-04 4.0656780e-03 1.3088226e-02 9.5080592e-02 1.7083949e-01
  7.1418184e-01 6.6129642e-04 1.6704693e-03]]
Age : (38-43), conf = 0.714
time : 0.101
Gender : Male, conf = 0.995
Age Output : [[3.0890820e-05 6.9258502e-04 1.1676616e-02 7.7465609e-02 1.8127543e-01
  7.2775364e-01 2.8254799e-04 8.2273333e-04]]
Age : (38-43), conf = 0.728
time : 0.084
Gender : Male, conf = 0.995
Age Output : [[3.0890820e-05 6.9258502e-04 1.1676616e-02 7.7465609e-02 1.8127543e-01
  7.2775364e-01 2.8254799e-04 8.2273333e-04]]
Age : (38-43), conf = 0.728
time : 0.097
Gender : Male, conf = 0.996
Age Output : [[2.3917889e-04 2.8401537e-02 1.6029175e-01 3.5938284e-01 2.1201055e-01
  2.3887585e-01 2.5359538e-04 5.4461916e-04]]
Age : (15-20), conf = 0.359
time : 0.082
Gender : Male, conf = 0.979
Age Output : [[2.7115879e-04 4.8280098e-03 6.2437183e-03 1.0960423e-01 1.8308997e-01
  6.9284904e-01 1.2280291e-03 1.8858587e-03]]
Age : (38-43), conf = 0.693
time : 0.106
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.554
Age Output : [[1.22535479e-04 3.60035081e-03 9.87138133e-03 3.92061844e-02
  1.13040015e-01 8.33152771e-01 4.61444492e-04 5.45355608e-04]]
Age : (38-43), conf = 0.833
time : 0.116
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 1.000
Age Output : [[5.3983080e-05 7.9778940e-05 9.2212264e-05 4.3823777e-04 9.9814069e-01
  8.6555985e-04 2.5195742e-04 7.7626588e-05]]
Age : (25-32), conf = 0.998
time : 0.123
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 1.000
Age Output : [[0.02050577 0.03222859 0.00481791 0.00570063 0.8861698  0.04015612
  0.00452642 0.00589476]]
Age : (25-32), conf = 0.886
time : 0.118
Gender : Male, conf = 1.000
Age Output : [[2.1741476e-03 4.6813739e-03 8.8198081e-04 2.7557646e-03 9.4984657e-01
  3.6010068e-02 2.2753268e-03 1.3747073e-03]]
Age : (25-32), conf = 0.950
time : 0.122
Gender : Male, conf = 1.000
Age Output : [[0.00277041 0.0080286  0.00142109 0.00405186 0.9615093  0.01899417
  0.00114251 0.00208203]]
Age : (25-32), conf = 0.962
time : 0.116
Gender : Male, conf = 1.000
Age Output : [[0.00159114 0.00603327 0.00135768 0.00346207 0.9504834  0.03498064
  0.00108043 0.00101148]]
Age : (25-32), conf = 0.950
time : 0.118
No face Detected, Checking next frame
Gender : Male, conf = 1.000
Age Output : [[2.9237228e-05 7.0543712e-05 4.1857198e-05 2.2916229e-04 9.9717784e-01
  2.2918175e-03 7.4691285e-05 8.4881634e-05]]
Age : (25-32), conf = 0.997
time : 0.123
Gender : Male, conf = 1.000
Age Output : [[1.8477582e-05 3.1291333e-05 2.1983957e-05 2.5680865e-04 9.9765682e-01
  1.9210028e-03 4.3775766e-05 4.9802384e-05]]
Age : (25-32), conf = 0.998
time : 0.127
Gender : Male, conf = 1.000
Age Output : [[9.3327259e-04 2.6766926e-03 2.8998035e-04 1.3167381e-03 9.9024898e-01
  3.8506293e-03 3.8558163e-04 2.9821592e-04]]
Age : (25-32), conf = 0.990
time : 0.115
Gender : Male, conf = 1.000
Age Output : [[0.0043963  0.00472249 0.00130338 0.00647548 0.94786435 0.03183852
  0.00174558 0.00165406]]
Age : (25-32), conf = 0.948
time : 0.116
No face Detected, Checking next frame
Gender : Male, conf = 1.000
Age Output : [[0.37957722 0.03861989 0.01167402 0.01874655 0.17316245 0.320077
  0.02777963 0.03036327]]
Age : (0-2), conf = 0.380
time : 0.104
Gender : Male, conf = 1.000
Age Output : [[0.37957722 0.03861989 0.01167402 0.01874655 0.17316245 0.320077
  0.02777963 0.03036327]]
Age : (0-2), conf = 0.380
time : 0.125
Gender : Male, conf = 1.000
Age Output : [[0.521887   0.06567189 0.00901734 0.01052034 0.1957967  0.15200806
  0.02224268 0.02285601]]
Age : (0-2), conf = 0.522
time : 0.109
Gender : Male, conf = 1.000
Age Output : [[0.6640911  0.16698016 0.00977486 0.0062521  0.08436979 0.04539003
  0.01092398 0.01221792]]
Age : (0-2), conf = 0.664
time : 0.102
Gender : Male, conf = 1.000
Age Output : [[8.3672647e-05 7.6577620e-04 1.2314317e-03 5.9400511e-04 9.9207604e-01
  4.8101842e-03 2.5452737e-04 1.8434276e-04]]
Age : (25-32), conf = 0.992
time : 0.089
Gender : Male, conf = 1.000
Age Output : [[2.1219319e-05 1.1240511e-03 1.5855101e-03 7.1149453e-04 9.8700249e-01
  9.4299149e-03 9.7857635e-05 2.7379483e-05]]
Age : (25-32), conf = 0.987
time : 0.098
Gender : Male, conf = 1.000
Age Output : [[7.4229461e-06 1.9114494e-04 1.0205650e-03 1.1376165e-03 9.6605366e-01
  3.1258218e-02 2.8286080e-04 4.8454076e-05]]
Age : (25-32), conf = 0.966
time : 0.092
Gender : Male, conf = 1.000
Age Output : [[5.3691198e-05 1.0698288e-03 7.8206818e-04 3.2522127e-03 9.8636627e-01
  8.3711492e-03 7.4529773e-05 3.0229628e-05]]
Age : (25-32), conf = 0.986
time : 0.105
Gender : Male, conf = 1.000
Age Output : [[4.6708054e-05 2.0979373e-03 7.1560028e-03 1.9757245e-03 9.7414637e-01
  1.4432230e-02 1.0492667e-04 4.0007948e-05]]
Age : (25-32), conf = 0.974
time : 0.119
Gender : Male, conf = 1.000
Age Output : [[3.3295919e-06 2.0083429e-04 6.5737905e-04 4.4838115e-04 9.9680138e-01
  1.8515544e-03 2.8034567e-05 9.0005533e-06]]
Age : (25-32), conf = 0.997
time : 0.117
Gender : Male, conf = 1.000
Age Output : [[3.0283754e-06 1.0843690e-04 7.5471108e-03 1.1541898e-03 9.7621107e-01
  1.4879805e-02 5.4435353e-05 4.1858530e-05]]
Age : (25-32), conf = 0.976
time : 0.116
Gender : Male, conf = 1.000
Age Output : [[9.1235434e-06 2.8468549e-04 5.2515161e-03 1.1759669e-03 9.8172873e-01
  1.1495099e-02 2.7832146e-05 2.6897054e-05]]
Age : (25-32), conf = 0.982
time : 0.115
Gender : Male, conf = 1.000
Age Output : [[1.4687674e-06 6.0676342e-05 1.3329980e-03 4.7796851e-04 9.9207264e-01
  6.0310937e-03 1.2897133e-05 1.0244262e-05]]
Age : (25-32), conf = 0.992
time : 0.101
Gender : Male, conf = 1.000
Age Output : [[2.9352306e-05 4.5803338e-04 2.2918798e-03 1.0151953e-03 9.8984820e-01
  6.2794127e-03 3.4842167e-05 4.3025317e-05]]
Age : (25-32), conf = 0.990
time : 0.084
Gender : Male, conf = 1.000
Age Output : [[3.76787975e-05 4.21234181e-05 1.49988380e-04 8.75907834e-04
  9.68426347e-01 3.02097313e-02 1.50373497e-04 1.07697306e-04]]
Age : (25-32), conf = 0.968
time : 0.084
No face Detected, Checking next frame
Gender : Male, conf = 0.880
Age Output : [[9.1051497e-06 1.2008248e-05 1.9336767e-05 2.2024485e-04 9.9770433e-01
  1.9688997e-03 3.5228190e-05 3.0981035e-05]]
Age : (25-32), conf = 0.998
time : 0.086
Gender : Female, conf = 0.938
Age Output : [[6.6708116e-04 8.1304909e-04 1.6154170e-04 9.0054155e-04 9.9408746e-01
  2.8115718e-03 3.9163916e-04 1.6716289e-04]]
Age : (25-32), conf = 0.994
time : 0.085
Gender : Female, conf = 0.967
Age Output : [[5.9074850e-04 1.0220280e-03 1.7962632e-04 1.0568723e-03 9.9504364e-01
  1.5941039e-03 3.7634798e-04 1.3652509e-04]]
Age : (25-32), conf = 0.995
time : 0.099
Gender : Female, conf = 0.980
Age Output : [[1.9927027e-04 8.5743133e-04 2.2042720e-04 1.2183542e-03 9.9615246e-01
  1.1668497e-03 1.3753367e-04 4.7793226e-05]]
Age : (25-32), conf = 0.996
time : 0.091
Gender : Female, conf = 0.910
Age Output : [[5.17515855e-06 3.14903373e-05 1.18448406e-04 3.70198279e-04
  9.98972178e-01 4.81413153e-04 1.02976073e-05 1.08727381e-05]]
Age : (25-32), conf = 0.999
time : 0.114
Gender : Female, conf = 0.874
Age Output : [[4.8296201e-06 3.1524836e-05 3.4132830e-05 5.1156152e-04 9.9917430e-01
  2.2853991e-04 6.4530823e-06 8.6106302e-06]]
Age : (25-32), conf = 0.999
time : 0.086
Gender : Female, conf = 0.669
Age Output : [[2.6330843e-06 1.5063728e-05 5.1734107e-05 5.2088225e-04 9.9916029e-01
  2.3815740e-04 4.2518218e-06 7.0056849e-06]]
Age : (25-32), conf = 0.999
time : 0.101
Gender : Female, conf = 0.876
Age Output : [[4.4165477e-06 1.5959398e-04 2.7423489e-03 2.3899132e-03 9.9417889e-01
  4.8184287e-04 2.3736031e-05 1.9274121e-05]]
Age : (25-32), conf = 0.994
time : 0.083
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Female, conf = 0.875
Age Output : [[8.0761754e-05 1.4297136e-03 2.1700202e-03 5.2999132e-03 9.9032182e-01
  6.4569240e-04 3.2249303e-05 1.9959018e-05]]
Age : (25-32), conf = 0.990
time : 0.102
Gender : Female, conf = 0.900
Age Output : [[6.1660999e-06 9.2109447e-05 1.2469166e-03 9.3930122e-04 9.9738151e-01
  3.1057012e-04 1.2028462e-05 1.1441532e-05]]
Age : (25-32), conf = 0.997
time : 0.082
Gender : Female, conf = 0.947
Age Output : [[2.6948296e-04 1.6920026e-03 1.1870738e-03 3.0669363e-03 9.9307775e-01
  6.5055932e-04 3.0171206e-05 2.6050388e-05]]
Age : (25-32), conf = 0.993
time : 0.097
Gender : Female, conf = 0.947
Age Output : [[2.6948296e-04 1.6920026e-03 1.1870738e-03 3.0669363e-03 9.9307775e-01
  6.5055932e-04 3.0171206e-05 2.6050388e-05]]
Age : (25-32), conf = 0.993
time : 0.092
Gender : Male, conf = 0.983
Age Output : [[3.6970039e-05 6.7237641e-05 7.5630634e-03 1.0540380e-02 9.6886873e-01
  1.2377680e-02 2.2301656e-04 3.2276780e-04]]
Age : (25-32), conf = 0.969
time : 0.096
Gender : Male, conf = 1.000
Age Output : [[1.9454936e-03 6.6448015e-04 2.2727996e-03 4.7109113e-03 9.5125228e-01
  3.6648188e-02 1.0947844e-03 1.4109605e-03]]
Age : (25-32), conf = 0.951
time : 0.088
Gender : Male, conf = 1.000
Age Output : [[8.7417699e-03 1.9418990e-03 4.2268811e-03 5.1264130e-03 9.4659418e-01
  2.7956029e-02 8.4690779e-04 4.5659617e-03]]
Age : (25-32), conf = 0.947
time : 0.098
Gender : Male, conf = 1.000
Age Output : [[0.00928202 0.00191067 0.00216704 0.00293153 0.950792   0.02723413
  0.00189629 0.0037862 ]]
Age : (25-32), conf = 0.951
time : 0.103
Gender : Male, conf = 1.000
Age Output : [[6.3431934e-03 2.1062458e-03 1.3437192e-03 4.7347574e-03 9.7500008e-01
  8.9148227e-03 7.1549427e-04 8.4170571e-04]]
Age : (25-32), conf = 0.975
time : 0.099
Gender : Male, conf = 1.000
Age Output : [[0.427543   0.10191213 0.01317192 0.01766661 0.38854352 0.03186196
  0.01005153 0.0092493 ]]
Age : (0-2), conf = 0.428
time : 0.085
Gender : Male, conf = 1.000
Age Output : [[0.00797308 0.00334805 0.0021208  0.00704459 0.96402985 0.01235749
  0.0012006  0.00192552]]
Age : (25-32), conf = 0.964
time : 0.098
Gender : Male, conf = 1.000
Age Output : [[5.3284765e-04 3.2401987e-04 1.3574300e-03 5.9283809e-03 9.6662861e-01
  2.0745184e-02 1.5180229e-03 2.9655136e-03]]
Age : (25-32), conf = 0.967
time : 0.090
Gender : Male, conf = 0.998
Age Output : [[8.0714824e-05 2.5838125e-04 7.0224062e-04 1.1850538e-02 9.8466241e-01
  2.3330674e-03 4.8901460e-05 6.3787375e-05]]
Age : (25-32), conf = 0.985
time : 0.096
Gender : Male, conf = 0.924
Age Output : [[7.5280559e-07 1.4777931e-05 2.6458403e-04 1.2393211e-03 9.9795157e-01
  5.0013891e-04 1.5212915e-05 1.3642089e-05]]
Age : (25-32), conf = 0.998
time : 0.091
Gender : Male, conf = 0.859
Age Output : [[3.5192897e-06 9.4963225e-06 6.4033666e-05 6.0643011e-04 9.9842739e-01
  8.5839425e-04 1.3070760e-05 1.7693763e-05]]
Age : (25-32), conf = 0.998
time : 0.101
Gender : Male, conf = 0.515
Age Output : [[7.4481338e-02 5.0648224e-01 6.6559450e-03 3.0819413e-03 4.0673414e-01
  1.7502154e-03 6.6298741e-04 1.5116454e-04]]
Age : (4-6), conf = 0.506
time : 0.084
Gender : Female, conf = 0.891
Age Output : [[1.2564197e-05 1.7317153e-04 2.1351548e-03 2.9917305e-02 9.6020156e-01
  7.4108313e-03 7.3298797e-05 7.6134063e-05]]
Age : (25-32), conf = 0.960
time : 0.098
Gender : Female, conf = 0.891
Age Output : [[1.2564197e-05 1.7317153e-04 2.1351548e-03 2.9917305e-02 9.6020156e-01
  7.4108313e-03 7.3298797e-05 7.6134063e-05]]
Age : (25-32), conf = 0.960
time : 0.091
Gender : Female, conf = 0.503
Age Output : [[9.7089537e-07 1.9405083e-05 3.3388275e-04 1.5083465e-03 9.9743408e-01
  6.8628864e-04 6.2331060e-06 1.0855676e-05]]
Age : (25-32), conf = 0.997
time : 0.098
Gender : Female, conf = 0.591
Age Output : [[1.5196523e-06 6.2046556e-06 6.0987088e-05 2.4536205e-04 9.9809915e-01
  1.5567607e-03 1.3825887e-05 1.6177253e-05]]
Age : (25-32), conf = 0.998
time : 0.090
Gender : Female, conf = 0.646
Age Output : [[1.1160038e-06 3.2732801e-06 4.9321159e-05 3.4894649e-04 9.9801815e-01
  1.5391978e-03 1.2078858e-05 2.8012364e-05]]
Age : (25-32), conf = 0.998
time : 0.100
Gender : Female, conf = 0.916
Age Output : [[8.4470059e-07 1.9329950e-06 2.4747811e-05 3.1492976e-04 9.9754435e-01
  2.0841439e-03 1.1122093e-05 1.7891636e-05]]
Age : (25-32), conf = 0.998
time : 0.084
Gender : Female, conf = 0.723
Age Output : [[1.2689236e-06 1.8510999e-06 1.9554936e-05 2.2223411e-04 9.9856037e-01
  1.1727138e-03 8.1653243e-06 1.3866259e-05]]
Age : (25-32), conf = 0.999
time : 0.101
Gender : Female, conf = 0.631
Age Output : [[2.2564919e-07 1.4343254e-06 2.5095709e-05 3.1886698e-04 9.9897516e-01
  6.6856924e-04 3.8166763e-06 6.8497166e-06]]
Age : (25-32), conf = 0.999
time : 0.089
Gender : Male, conf = 0.724
Age Output : [[2.6441609e-07 8.0169042e-07 1.6742664e-05 2.7614718e-04 9.9836737e-01
  1.3243832e-03 4.8705538e-06 9.4472271e-06]]
Age : (25-32), conf = 0.998
time : 0.100
Gender : Female, conf = 0.572
Age Output : [[9.5822223e-08 4.6066705e-07 2.0046347e-05 2.6643075e-04 9.9926132e-01
  4.4231018e-04 2.4611932e-06 6.7406886e-06]]
Age : (25-32), conf = 0.999
time : 0.089
Gender : Female, conf = 0.600
Age Output : [[1.9824736e-06 3.1987397e-06 2.6583268e-05 4.4988099e-04 9.9655765e-01
  2.9189808e-03 1.5527519e-05 2.6135116e-05]]
Age : (25-32), conf = 0.997
time : 0.099
Gender : Male, conf = 0.576
Age Output : [[5.8475808e-07 1.2209415e-06 1.7395336e-05 4.5873225e-04 9.9718326e-01
  2.3053421e-03 1.2353082e-05 2.1046473e-05]]
Age : (25-32), conf = 0.997
time : 0.085
Gender : Male, conf = 0.581
Age Output : [[3.2805556e-07 8.9369365e-07 2.4142772e-05 3.6743164e-04 9.9861181e-01
  9.8147616e-04 4.5619581e-06 9.2304581e-06]]
Age : (25-32), conf = 0.999
time : 0.100
Gender : Male, conf = 0.581
Age Output : [[3.2805556e-07 8.9369365e-07 2.4142772e-05 3.6743164e-04 9.9861181e-01
  9.8147616e-04 4.5619581e-06 9.2304581e-06]]
Age : (25-32), conf = 0.999
time : 0.090
Gender : Male, conf = 0.927
Age Output : [[1.8583531e-04 1.3212413e-04 2.1312421e-04 5.6857825e-03 9.7770065e-01
  1.5580454e-02 1.6493151e-04 3.3719616e-04]]
Age : (25-32), conf = 0.978
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[1.0059213e-02 4.6972660e-03 9.1339666e-03 2.5474688e-02 9.2216635e-01
  2.5405489e-02 7.7701482e-04 2.2861729e-03]]
Age : (25-32), conf = 0.922
time : 0.090
Gender : Male, conf = 1.000
Age Output : [[0.02377862 0.00722834 0.01433516 0.01101716 0.88111216 0.05689551
  0.00156726 0.00406584]]
Age : (25-32), conf = 0.881
time : 0.102
Gender : Male, conf = 1.000
Age Output : [[0.34036815 0.15283747 0.02190439 0.00658784 0.4465591  0.0265725
  0.00221106 0.00295945]]
Age : (25-32), conf = 0.447
time : 0.087
Gender : Male, conf = 1.000
Age Output : [[0.641755   0.18581346 0.00735508 0.0037144  0.15020148 0.00829623
  0.0012833  0.00158099]]
Age : (0-2), conf = 0.642
time : 0.103
Gender : Male, conf = 1.000
Age Output : [[0.4805247  0.08407319 0.00600607 0.00585743 0.39386123 0.02480771
  0.00255494 0.00231479]]
Age : (0-2), conf = 0.481
time : 0.086
Gender : Male, conf = 1.000
Age Output : [[0.4805247  0.08407319 0.00600607 0.00585743 0.39386123 0.02480771
  0.00255494 0.00231479]]
Age : (0-2), conf = 0.481
time : 0.101
Gender : Male, conf = 1.000
Age Output : [[0.4836529  0.10644435 0.00854674 0.00386079 0.36778253 0.02511143
  0.00216941 0.00243196]]
Age : (0-2), conf = 0.484
time : 0.081
Gender : Male, conf = 1.000
Age Output : [[0.44928136 0.08617856 0.01068065 0.01241786 0.39267054 0.04110799
  0.00352791 0.00413511]]
Age : (0-2), conf = 0.449
time : 0.100
Gender : Male, conf = 1.000
Age Output : [[0.24801478 0.081489   0.00871834 0.01495883 0.6033846  0.03694367
  0.00289702 0.00359371]]
Age : (25-32), conf = 0.603
time : 0.090
Gender : Male, conf = 1.000
Age Output : [[0.54715306 0.25190663 0.00934173 0.00401318 0.17445745 0.01054249
  0.00150336 0.00108198]]
Age : (0-2), conf = 0.547
time : 0.105
Gender : Male, conf = 1.000
Age Output : [[0.61300427 0.11015955 0.00777317 0.00582767 0.24383132 0.01585012
  0.00164878 0.00190507]]
Age : (0-2), conf = 0.613
time : 0.092
Gender : Male, conf = 1.000
Age Output : [[0.7977593  0.11288291 0.00442176 0.00339158 0.0726865  0.0066905
  0.00111045 0.00105693]]
Age : (0-2), conf = 0.798
time : 0.093
Gender : Male, conf = 1.000
Age Output : [[0.7112514  0.10418316 0.00876891 0.00788756 0.14485319 0.01791348
  0.00242583 0.00271655]]
Age : (0-2), conf = 0.711
time : 0.091
Gender : Male, conf = 1.000
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[0.4842275  0.05884366 0.00745049 0.01214039 0.38342363 0.04532547
  0.00387304 0.00471587]]
Age : (0-2), conf = 0.484
time : 0.102
Gender : Male, conf = 1.000
Age Output : [[0.41698673 0.04511188 0.00754609 0.00653886 0.45502228 0.05902462
  0.00387604 0.00589346]]
Age : (25-32), conf = 0.455
time : 0.081
Gender : Male, conf = 1.000
Age Output : [[0.619316   0.09178716 0.00918977 0.00729288 0.24492274 0.02234385
  0.00191447 0.00323313]]
Age : (0-2), conf = 0.619
time : 0.084
Gender : Male, conf = 1.000
Age Output : [[0.4126767  0.12257143 0.00958931 0.01702821 0.40735507 0.02569124
  0.00234198 0.00274605]]
Age : (0-2), conf = 0.413
time : 0.086
Gender : Male, conf = 1.000
Age Output : [[0.4126767  0.12257143 0.00958931 0.01702821 0.40735507 0.02569124
  0.00234198 0.00274605]]
Age : (0-2), conf = 0.413
time : 0.097
Gender : Male, conf = 1.000
Age Output : [[0.6296691  0.17332107 0.00821759 0.00175399 0.17854412 0.00633202
  0.00090146 0.00126065]]
Age : (0-2), conf = 0.630
time : 0.091
Gender : Male, conf = 1.000
Age Output : [[2.46712501e-04 5.32776234e-04 2.28093224e-04 5.01453469e-04
  9.90097165e-01 8.18420388e-03 1.07527936e-04 1.02074402e-04]]
Age : (25-32), conf = 0.990
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[7.27806139e-07 1.07410215e-05 1.16680400e-03 9.65724350e-04
  9.20422196e-01 7.73531795e-02 4.79750306e-05 3.27497801e-05]]
Age : (25-32), conf = 0.920
time : 0.088
Gender : Male, conf = 0.998
Age Output : [[1.4667934e-06 4.5335561e-05 2.5920165e-03 4.8604649e-03 9.1081631e-01
  8.1522457e-02 1.2051737e-04 4.1520445e-05]]
Age : (25-32), conf = 0.911
time : 0.099
Gender : Male, conf = 0.999
Age Output : [[5.2039759e-08 1.4910211e-06 1.6093811e-04 3.6027239e-04 9.9260181e-01
  6.8644523e-03 8.2776896e-06 2.7432159e-06]]
Age : (25-32), conf = 0.993
time : 0.081
Gender : Male, conf = 0.999
Age Output : [[2.3745118e-08 4.1563342e-07 2.6233980e-05 2.2777822e-04 9.9860889e-01
  1.1314726e-03 3.1242866e-06 2.1754033e-06]]
Age : (25-32), conf = 0.999
time : 0.093
Gender : Male, conf = 0.999
Age Output : [[2.3745118e-08 4.1563342e-07 2.6233980e-05 2.2777822e-04 9.9860889e-01
  1.1314726e-03 3.1242866e-06 2.1754033e-06]]
Age : (25-32), conf = 0.999
time : 0.102
Gender : Male, conf = 1.000
Age Output : [[7.3616455e-08 1.9753491e-06 1.3640629e-04 1.0529992e-03 9.9147183e-01
  7.3139700e-03 1.5976853e-05 6.7397950e-06]]
Age : (25-32), conf = 0.991
time : 0.098
Gender : Male, conf = 0.999
Age Output : [[1.5705220e-07 2.8788920e-06 8.9247995e-05 1.7997804e-03 9.7939759e-01
  1.8661646e-02 3.3691329e-05 1.4917252e-05]]
Age : (25-32), conf = 0.979
time : 0.077
Gender : Male, conf = 1.000
Age Output : [[3.1187208e-06 5.3672920e-05 5.1564863e-04 4.5919400e-03 9.0392596e-01
  9.0567499e-02 2.6732296e-04 7.4850599e-05]]
Age : (25-32), conf = 0.904
time : 0.097
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.983
Age Output : [[0.01664372 0.00260879 0.00300318 0.00120579 0.87243074 0.09759045
  0.00199909 0.00451828]]
Age : (25-32), conf = 0.872
time : 0.090
Gender : Male, conf = 0.981
Age Output : [[1.8241535e-03 5.6393247e-04 1.2410368e-03 2.5887694e-04 9.6751314e-01
  2.8079042e-02 1.5990998e-04 3.5997867e-04]]
Age : (25-32), conf = 0.968
time : 0.099
No face Detected, Checking next frame
Gender : Female, conf = 0.689
Age Output : [[0.7112458  0.155328   0.01160332 0.00081212 0.10888124 0.00354411
  0.00110791 0.00747766]]
Age : (0-2), conf = 0.711
time : 0.084
Gender : Male, conf = 0.982
Age Output : [[9.6464723e-01 1.6545676e-02 1.9373460e-03 1.6599869e-04 1.2945080e-02
  1.3655308e-03 3.1305820e-04 2.0800778e-03]]
Age : (0-2), conf = 0.965
time : 0.092
Gender : Male, conf = 0.957
Age Output : [[1.2989402e-02 8.6665982e-03 2.8064069e-03 3.9612263e-04 9.7135991e-01
  3.1746663e-03 3.1497073e-04 2.9186171e-04]]
Age : (25-32), conf = 0.971
time : 0.077
Gender : Male, conf = 0.957
Age Output : [[1.2989402e-02 8.6665982e-03 2.8064069e-03 3.9612263e-04 9.7135991e-01
  3.1746663e-03 3.1497073e-04 2.9186171e-04]]
Age : (25-32), conf = 0.971
time : 0.103
Gender : Male, conf = 0.995
Age Output : [[1.8074734e-05 1.9387208e-04 3.4159417e-03 5.5100041e-04 9.9374372e-01
  2.0297749e-03 1.4162607e-05 3.3366046e-05]]
Age : (25-32), conf = 0.994
time : 0.088
Gender : Male, conf = 0.995
Age Output : [[6.4027682e-07 1.4032443e-05 3.5506149e-04 2.3310607e-04 9.9745363e-01
  1.9301937e-03 5.6812469e-06 7.5697694e-06]]
Age : (25-32), conf = 0.997
time : 0.101
Gender : Male, conf = 0.996
Age Output : [[9.1285742e-08 1.1577479e-06 3.2733918e-05 4.1498624e-05 9.9915838e-01
  7.6053251e-04 3.0160143e-06 2.5823085e-06]]
Age : (25-32), conf = 0.999
time : 0.085
Gender : Male, conf = 0.994
Age Output : [[1.8647215e-07 4.9879773e-06 9.3413553e-05 7.6342832e-05 9.9929607e-01
  5.2534620e-04 1.7162055e-06 1.9811851e-06]]
Age : (25-32), conf = 0.999
time : 0.093
Gender : Male, conf = 0.997
Age Output : [[2.2012021e-08 4.5922272e-07 1.1781394e-05 5.6511817e-05 9.9976772e-01
  1.6125856e-04 9.1228014e-07 1.3031422e-06]]
Age : (25-32), conf = 1.000
time : 0.091
Gender : Male, conf = 0.998
Age Output : [[5.7450751e-07 1.8155621e-05 7.0489492e-05 1.5250538e-04 9.9926049e-01
  4.9071654e-04 4.2198853e-06 3.0201420e-06]]
Age : (25-32), conf = 0.999
time : 0.105
Gender : Male, conf = 0.999
Age Output : [[2.2635586e-06 9.0227346e-05 4.3722850e-04 3.0646869e-04 9.9647468e-01
  2.6704748e-03 1.1270972e-05 7.3870251e-06]]
Age : (25-32), conf = 0.996
time : 0.081
Gender : Male, conf = 0.999
Age Output : [[2.7512577e-05 1.8269183e-03 1.4123216e-03 5.7976594e-04 9.9186838e-01
  4.2286990e-03 3.6191857e-05 2.0205565e-05]]
Age : (25-32), conf = 0.992
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[1.12140133e-05 2.42908907e-04 2.15579421e-04 2.90958560e-04
  9.96733785e-01 2.46797875e-03 2.48650467e-05 1.26750665e-05]]
Age : (25-32), conf = 0.997
time : 0.093
Gender : Male, conf = 0.999
Age Output : [[1.3616938e-05 4.8701745e-04 4.2365619e-04 3.3493567e-04 9.9619544e-01
  2.5047027e-03 2.8551955e-05 1.2265470e-05]]
Age : (25-32), conf = 0.996
time : 0.100
Gender : Male, conf = 1.000
Age Output : [[2.9855889e-06 5.4528849e-05 7.6431330e-05 1.8682645e-04 9.9904436e-01
  6.1809714e-04 1.0147107e-05 6.6149109e-06]]
Age : (25-32), conf = 0.999
time : 0.082
Gender : Male, conf = 0.999
Age Output : [[1.3999110e-04 1.3828119e-03 2.4899794e-04 5.5641081e-04 9.9532288e-01
  2.2529233e-03 6.2686100e-05 3.3322889e-05]]
Age : (25-32), conf = 0.995
time : 0.080
Gender : Male, conf = 1.000
Age Output : [[2.3761424e-04 1.7356407e-03 3.0944348e-04 7.3328684e-04 9.9541664e-01
  1.4576503e-03 7.4182040e-05 3.5567453e-05]]
Age : (25-32), conf = 0.995
time : 0.091
Gender : Male, conf = 1.000
Age Output : [[2.6040577e-04 2.2139410e-03 3.6206451e-04 7.6169398e-04 9.9474263e-01
  1.5547234e-03 6.6170804e-05 3.8286900e-05]]
Age : (25-32), conf = 0.995
time : 0.100
Gender : Male, conf = 1.000
Age Output : [[2.8606558e-03 2.3284491e-02 1.7645261e-03 1.7986463e-03 9.6679026e-01
  3.2556604e-03 1.5786850e-04 8.7796616e-05]]
Age : (25-32), conf = 0.967
time : 0.085
Gender : Male, conf = 1.000
Age Output : [[2.0763453e-03 1.1912486e-02 9.3376829e-04 9.6904126e-04 9.8270470e-01
  1.2349769e-03 1.0783185e-04 6.0951272e-05]]
Age : (25-32), conf = 0.983
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[1.1832039e-03 9.0069175e-03 7.7313604e-04 1.1452583e-03 9.8632449e-01
  1.3576505e-03 1.3698825e-04 7.2361086e-05]]
Age : (25-32), conf = 0.986
time : 0.081
Gender : Male, conf = 0.999
Age Output : [[1.4301084e-03 5.6372327e-03 1.1507220e-03 5.2653381e-04 9.8886758e-01
  2.2570733e-03 8.0399041e-05 5.0338869e-05]]
Age : (25-32), conf = 0.989
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[9.7795445e-03 1.9712264e-02 1.8961612e-03 8.8007288e-04 9.6401644e-01
  3.2835966e-03 2.6093956e-04 1.7085015e-04]]
Age : (25-32), conf = 0.964
time : 0.083
Gender : Male, conf = 0.999
Age Output : [[7.4217841e-02 5.4277454e-02 3.1553388e-03 1.8140783e-03 8.6172175e-01
  4.0744971e-03 4.1597616e-04 3.2311282e-04]]
Age : (25-32), conf = 0.862
time : 0.099
Gender : Male, conf = 0.998
Age Output : [[8.8804848e-02 1.0374873e-01 4.6392651e-03 1.2692130e-03 7.9836059e-01
  2.6297299e-03 2.9292688e-04 2.5465660e-04]]
Age : (25-32), conf = 0.798
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[1.7620723e-03 8.6763017e-03 1.5422286e-03 4.6843116e-04 9.8646265e-01
  9.7529398e-04 5.7849073e-05 5.5176388e-05]]
Age : (25-32), conf = 0.986
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>time : 0.084
Gender : Male, conf = 0.999
Age Output : [[9.2545059e-04 2.2280111e-03 5.3284090e-04 2.8263719e-04 9.9379009e-01
  2.1203065e-03 6.5851469e-05 5.4720800e-05]]
Age : (25-32), conf = 0.994
time : 0.091
Gender : Male, conf = 1.000
Age Output : [[1.3393206e-03 2.9356186e-03 5.0466572e-04 3.5319928e-04 9.9325800e-01
  1.4769757e-03 7.3949486e-05 5.8304704e-05]]
Age : (25-32), conf = 0.993
time : 0.097
Gender : Male, conf = 1.000
Age Output : [[1.3393206e-03 2.9356186e-03 5.0466572e-04 3.5319928e-04 9.9325800e-01
  1.4769757e-03 7.3949486e-05 5.8304704e-05]]
Age : (25-32), conf = 0.993
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[2.8436407e-03 2.1483632e-02 1.7646103e-03 7.5249554e-04 9.7058487e-01
  2.3926625e-03 1.0710658e-04 7.0942282e-05]]
Age : (25-32), conf = 0.971
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[1.0443518e-02 1.7663045e-02 1.5678100e-03 1.0762871e-03 9.6597397e-01
  2.9420168e-03 1.8740632e-04 1.4588707e-04]]
Age : (25-32), conf = 0.966
time : 0.092
Gender : Male, conf = 1.000
Age Output : [[1.3457927e-01 2.8147742e-01 6.6228774e-03 2.7840743e-03 5.6832558e-01
  5.3609628e-03 5.5879320e-04 2.9107367e-04]]
Age : (25-32), conf = 0.568
time : 0.101
Gender : Male, conf = 1.000
Age Output : [[7.4734483e-03 2.5307212e-02 1.8797423e-03 1.0516479e-03 9.6032709e-01
  3.6403302e-03 2.2562339e-04 9.4916148e-05]]
Age : (25-32), conf = 0.960
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[9.4564827e-03 5.1989596e-02 3.2715960e-03 1.3293063e-03 9.3083811e-01
  2.8937384e-03 1.5122660e-04 6.9959249e-05]]
Age : (25-32), conf = 0.931
time : 0.098
Gender : Male, conf = 0.998
Age Output : [[1.2214425e-04 1.0576799e-03 3.1999432e-04 3.5316456e-04 9.9606091e-01
  2.0289479e-03 3.9256189e-05 1.7913721e-05]]
Age : (25-32), conf = 0.996
time : 0.075
Gender : Male, conf = 1.000
Age Output : [[2.1665059e-02 5.7013910e-02 3.2133099e-03 1.9246674e-03 9.1041923e-01
  5.3569353e-03 2.4196570e-04 1.6501668e-04]]
Age : (25-32), conf = 0.910
time : 0.098
Gender : Male, conf = 0.999
Age Output : [[6.2549509e-02 5.4766543e-02 2.5145733e-03 2.1841833e-03 8.7113738e-01
  5.9765736e-03 6.0243986e-04 2.6890071e-04]]
Age : (25-32), conf = 0.871
time : 0.088
Gender : Male, conf = 0.999
Age Output : [[0.47754452 0.18454081 0.0087743  0.0020039  0.32123291 0.00454355
  0.00060684 0.00075318]]
Age : (0-2), conf = 0.478
time : 0.112
Gender : Male, conf = 0.977
Age Output : [[9.4158721e-01 4.1958820e-02 1.2803550e-03 2.1734349e-04 1.4361228e-02
  3.9377765e-04 6.3337298e-05 1.3809768e-04]]
Age : (0-2), conf = 0.942
time : 0.113
Gender : Male, conf = 0.899
Age Output : [[9.1603810e-01 6.3233495e-02 2.4205027e-03 1.9112656e-04 1.7618271e-02
  3.0124374e-04 4.9707891e-05 1.4754520e-04]]
Age : (0-2), conf = 0.916
time : 0.122
Gender : Male, conf = 0.632
Age Output : [[9.9766040e-01 2.2276547e-03 7.0991795e-05 2.4119136e-06 2.4436034e-05
  5.2731248e-06 1.7598392e-06 7.1528771e-06]]
Age : (0-2), conf = 0.998
time : 0.116
Gender : Female, conf = 0.810
Age Output : [[9.8918533e-01 1.0008017e-02 5.0042366e-04 1.9608866e-05 1.5301890e-04
  5.4158023e-05 1.5964060e-05 6.3520725e-05]]
Age : (0-2), conf = 0.989
time : 0.122
Gender : Female, conf = 0.802
Age Output : [[9.0630728e-01 8.9688241e-02 2.8826511e-03 7.9735408e-05 6.8667531e-04
  1.8647965e-04 4.4250541e-05 1.2472639e-04]]
Age : (0-2), conf = 0.906
time : 0.116
Gender : Female, conf = 0.794
Age Output : [[9.6884906e-01 3.0177843e-02 4.9871951e-04 2.7215647e-05 3.6592307e-04
  3.8267761e-05 1.3610503e-05 2.9340457e-05]]
Age : (0-2), conf = 0.969
time : 0.118
Gender : Female, conf = 0.586
Age Output : [[9.6255720e-01 3.5995662e-02 6.5685809e-04 4.6782126e-05 5.7589391e-04
  7.1671355e-05 2.5204399e-05 7.0681563e-05]]
Age : (0-2), conf = 0.963
time : 0.114
Gender : Male, conf = 0.672
Age Output : [[9.8782015e-01 1.1753409e-02 1.7769862e-04 1.6198530e-05 1.9103772e-04
  1.6740883e-05 8.3367459e-06 1.6505704e-05]]
Age : (0-2), conf = 0.988
time : 0.122
Gender : Male, conf = 0.845
Age Output : [[8.2284230e-01 1.7155255e-01 3.3986066e-03 1.9320654e-04 1.6619880e-03
  1.4571901e-04 4.5840974e-05 1.5976012e-04]]
Age : (0-2), conf = 0.823
time : 0.116
Gender : Male, conf = 0.546
Age Output : [[9.8207963e-01 1.7536912e-02 2.1206585e-04 1.2423347e-05 1.2422346e-04
  1.6119086e-05 5.7769139e-06 1.2841050e-05]]
Age : (0-2), conf = 0.982
time : 0.135
Gender : Male, conf = 0.957
Age Output : [[8.8485008e-01 1.1316914e-01 1.5161571e-03 5.9424317e-05 3.0285725e-04
  5.1025887e-05 1.4288437e-05 3.7048878e-05]]
Age : (0-2), conf = 0.885
time : 0.116
Gender : Male, conf = 0.553
Age Output : [[9.8020077e-01 1.8860292e-02 4.8729259e-04 3.3421791e-05 2.9633756e-04
  6.8348942e-05 1.7090346e-05 3.6585319e-05]]
Age : (0-2), conf = 0.980
time : 0.118
Gender : Female, conf = 0.561
Age Output : [[9.8462188e-01 1.4647656e-02 4.1758377e-04 2.6491458e-05 1.9138373e-04
  5.5332759e-05 1.1757275e-05 2.7812925e-05]]
Age : (0-2), conf = 0.985
time : 0.113
Gender : Female, conf = 0.731
Age Output : [[9.8953897e-01 9.6893525e-03 2.8515694e-04 2.8052069e-05 3.4992467e-04
  4.8848291e-05 1.8610324e-05 4.1176503e-05]]
Age : (0-2), conf = 0.990
time : 0.116
Gender : Female, conf = 0.798
Age Output : [[9.7690499e-01 2.2877913e-02 1.3947909e-04 5.5538794e-06 5.7745943e-05
  5.7435059e-06 2.7660592e-06 5.6966469e-06]]
Age : (0-2), conf = 0.977
time : 0.116
Gender : Female, conf = 0.950
Age Output : [[9.9269885e-01 7.2365114e-03 4.6997116e-05 1.3136844e-06 1.1846534e-05
  1.6775475e-06 7.9357437e-07 2.0295927e-06]]
Age : (0-2), conf = 0.993
time : 0.122
Gender : Male, conf = 0.764
Age Output : [[9.8547345e-01 1.3557549e-02 7.3744665e-04 2.9760376e-05 1.2925468e-04
  3.6339450e-05 7.3547399e-06 2.9016690e-05]]
Age : (0-2), conf = 0.985
time : 0.116
Gender : Female, conf = 0.520
Age Output : [[9.6882558e-01 2.8953226e-02 1.7963023e-03 5.7059671e-05 2.0814192e-04
  7.0793023e-05 1.7768340e-05 7.1293107e-05]]
Age : (0-2), conf = 0.969
time : 0.119
Gender : Female, conf = 0.520
Age Output : [[9.6882558e-01 2.8953226e-02 1.7963023e-03 5.7059671e-05 2.0814192e-04
  7.0793023e-05 1.7768340e-05 7.1293107e-05]]
Age : (0-2), conf = 0.969
time : 0.103
Gender : Female, conf = 0.720
Age Output : [[9.8196536e-01 1.7326016e-02 4.4071334e-04 1.8447854e-05 1.8354767e-04
  3.2068492e-05 9.8395403e-06 2.3998387e-05]]
Age : (0-2), conf = 0.982
time : 0.117
Gender : Female, conf = 0.668
Age Output : [[9.9735534e-01 2.5673974e-03 5.0973107e-05 1.6705549e-06 1.6805910e-05
  3.9271208e-06 9.2499874e-07 2.9130888e-06]]
Age : (0-2), conf = 0.997
time : 0.098
Gender : Male, conf = 0.765
Age Output : [[9.5247364e-01 4.5891941e-02 1.3823062e-03 3.2516797e-05 1.4426498e-04
  4.4640306e-05 6.6403031e-06 2.4058245e-05]]
Age : (0-2), conf = 0.952
time : 0.106
Gender : Male, conf = 0.978
Age Output : [[9.2679799e-01 6.9793947e-02 2.2401877e-03 7.9257414e-05 8.6457940e-04
  1.5601289e-04 2.4698997e-05 4.3367367e-05]]
Age : (0-2), conf = 0.927
time : 0.097
Gender : Male, conf = 0.994
Age Output : [[9.7423971e-01 2.4594931e-02 7.2780269e-04 2.4301813e-05 3.0234017e-04
  7.2206196e-05 1.0557196e-05 2.8128936e-05]]
Age : (0-2), conf = 0.974
time : 0.104
Gender : Male, conf = 0.962
Age Output : [[9.8277456e-01 1.6295245e-02 3.8142627e-04 2.3995248e-05 4.7571346e-04
  2.5161145e-05 6.7294177e-06 1.7074492e-05]]
Age : (0-2), conf = 0.983
time : 0.092
Gender : Male, conf = 0.983
Age Output : [[9.8497218e-01 1.4254586e-02 3.3016590e-04 2.5153688e-05 3.5614165e-04
  3.6986683e-05 7.5972594e-06 1.7187729e-05]]
Age : (0-2), conf = 0.985
time : 0.108
Gender : Male, conf = 0.957
Age Output : [[9.32554066e-01 6.04859293e-02 2.64005596e-03 1.55784859e-04
  3.72802513e-03 2.89030519e-04 3.63933432e-05 1.10890316e-04]]
Age : (0-2), conf = 0.933
time : 0.120
Gender : Male, conf = 0.996
Age Output : [[9.9212486e-01 7.3084123e-03 2.2595936e-04 1.7710156e-05 2.7136621e-04
  2.5584572e-05 6.9104799e-06 1.9224981e-05]]
Age : (0-2), conf = 0.992
time : 0.117
Gender : Male, conf = 1.000
Age Output : [[9.9472332e-01 4.8095714e-03 1.9977443e-04 1.1687926e-05 2.0073695e-04
  2.8675686e-05 6.0263692e-06 2.0072119e-05]]
Age : (0-2), conf = 0.995
time : 0.105
Gender : Male, conf = 0.998
Age Output : [[9.8917192e-01 9.2481785e-03 6.0348766e-04 5.5213859e-05 7.1204582e-04
  1.1744667e-04 2.2055607e-05 6.9728732e-05]]
Age : (0-2), conf = 0.989
time : 0.134
Gender : Male, conf = 0.999
Age Output : [[9.9346775e-01 5.9353737e-03 2.3405200e-04 1.7056662e-05 2.8745402e-04
  3.0966530e-05 8.1893886e-06 1.9291474e-05]]
Age : (0-2), conf = 0.993
time : 0.098
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.992
Age Output : [[9.9042004e-01 9.0210075e-03 3.4354749e-04 1.5746520e-05 1.4867283e-04
  2.7840064e-05 5.9070021e-06 1.7190214e-05]]
Age : (0-2), conf = 0.990
time : 0.103
Gender : Male, conf = 0.997
Age Output : [[9.8917294e-01 1.0160405e-02 3.3464420e-04 2.3357341e-05 2.3870380e-04
  3.4940076e-05 8.7307217e-06 2.6310821e-05]]
Age : (0-2), conf = 0.989
time : 0.084
Gender : Male, conf = 0.983
Age Output : [[9.73049462e-01 2.49340981e-02 1.18318282e-03 6.52796152e-05
  5.75811835e-04 1.16770374e-04 1.73778972e-05 5.78829240e-05]]
Age : (0-2), conf = 0.973
time : 0.099
Gender : Male, conf = 0.908
Age Output : [[9.7657436e-01 2.0906657e-02 1.3759512e-03 9.4089075e-05 7.3028851e-04
  1.8550479e-04 2.7158292e-05 1.0606458e-04]]
Age : (0-2), conf = 0.977
time : 0.085
Gender : Male, conf = 0.998
Age Output : [[9.9166250e-01 7.7806492e-03 2.6742477e-04 1.4550860e-05 2.2604823e-04
  2.4298581e-05 7.2114599e-06 1.7260338e-05]]
Age : (0-2), conf = 0.992
time : 0.098
Gender : Female, conf = 0.597
Age Output : [[9.8955524e-01 1.0223985e-02 1.4326184e-04 5.9957279e-06 5.5876706e-05
  6.9757052e-06 2.5713707e-06 6.0809944e-06]]
Age : (0-2), conf = 0.990
time : 0.079
Gender : Male, conf = 0.575
Age Output : [[9.4986808e-01 4.9116049e-02 6.5677566e-04 2.5502595e-05 2.7548586e-04
  3.2670494e-05 1.0215645e-05 1.5203047e-05]]
Age : (0-2), conf = 0.950
time : 0.098
No face Detected, Checking next frame
Gender : Female, conf = 0.910
Age Output : [[9.8430581e-02 9.0017813e-01 1.1959636e-03 3.6557572e-05 1.3635115e-04
  1.4266798e-05 5.2291125e-06 2.7578801e-06]]
Age : (4-6), conf = 0.900
time : 0.100
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.934
Age Output : [[1.3252407e-02 9.8157942e-01 1.1557214e-03 4.7458266e-04 3.4720828e-03
  2.2220185e-05 3.2951171e-05 1.0584729e-05]]
Age : (4-6), conf = 0.982
time : 0.092
Gender : Female, conf = 0.999
Age Output : [[9.8865557e-06 2.0570236e-03 9.2076184e-03 2.0375568e-03 9.8431349e-01
  2.3318483e-03 3.2410182e-05 1.0180816e-05]]
Age : (25-32), conf = 0.984
time : 0.128
Gender : Female, conf = 0.780
Age Output : [[9.2678107e-08 1.4946964e-06 1.9903123e-04 9.8032258e-05 9.9953485e-01
  1.6348850e-04 1.6618438e-06 1.3704913e-06]]
Age : (25-32), conf = 1.000
time : 0.111
Gender : Female, conf = 0.961
Age Output : [[2.4151530e-05 1.4570836e-04 6.9356494e-04 3.7919404e-04 9.9849033e-01
  2.4898929e-04 4.9129371e-06 1.3134328e-05]]
Age : (25-32), conf = 0.998
time : 0.085
Gender : Female, conf = 0.503
Age Output : [[3.8342788e-03 1.4350112e-01 4.1007899e-02 1.7451910e-02 7.9092979e-01
  2.7302043e-03 1.1963817e-04 4.2507396e-04]]
Age : (25-32), conf = 0.791
time : 0.119
Gender : Female, conf = 0.503
Age Output : [[3.8342788e-03 1.4350112e-01 4.1007899e-02 1.7451910e-02 7.9092979e-01
  2.7302043e-03 1.1963817e-04 4.2507396e-04]]
Age : (25-32), conf = 0.791
time : 0.090
Gender : Male, conf = 0.979
Age Output : [[6.8863918e-04 4.3899808e-03 2.2934640e-03 1.2505266e-03 9.8814911e-01
  2.7612466e-03 3.4185421e-05 4.3289101e-04]]
Age : (25-32), conf = 0.988
time : 0.100
Gender : Male, conf = 0.829
Age Output : [[4.0218249e-05 6.4408220e-03 2.2804621e-03 1.2236208e-03 9.8969299e-01
  2.8042647e-04 9.9549134e-06 3.1458298e-05]]
Age : (25-32), conf = 0.990
time : 0.084
Gender : Male, conf = 0.924
Age Output : [[1.0344914e-06 6.7739580e-05 5.3618709e-03 1.7577426e-03 9.9236780e-01
  4.2122864e-04 8.2799143e-06 1.4351366e-05]]
Age : (25-32), conf = 0.992
time : 0.084
Gender : Female, conf = 0.764
Age Output : [[7.4385866e-06 2.8867149e-03 3.2700785e-02 2.2746053e-02 9.4084626e-01
  7.1605848e-04 1.9919109e-05 7.6732686e-05]]
Age : (25-32), conf = 0.941
time : 0.092
Gender : Female, conf = 0.764
Age Output : [[7.4385866e-06 2.8867149e-03 3.2700785e-02 2.2746053e-02 9.4084626e-01
  7.1605848e-04 1.9919109e-05 7.6732686e-05]]
Age : (25-32), conf = 0.941
time : 0.110
Gender : Male, conf = 0.546
Age Output : [[7.2757616e-06 1.2349773e-03 5.6763301e-03 2.5587785e-03 9.9018759e-01
  3.0585588e-04 1.0002247e-05 1.9065579e-05]]
Age : (25-32), conf = 0.990
time : 0.078
Gender : Male, conf = 0.976
Age Output : [[2.1122332e-06 4.3424804e-04 1.2189723e-02 3.2068766e-03 9.8360449e-01
  5.4690149e-04 6.9669113e-06 8.8353599e-06]]
Age : (25-32), conf = 0.984
time : 0.099
Gender : Female, conf = 0.920
Age Output : [[2.9166362e-05 1.8218531e-03 8.2115168e-03 3.8729759e-03 9.8201603e-01
  4.0156161e-03 1.4139565e-05 1.8765426e-05]]
Age : (25-32), conf = 0.982
time : 0.089
Gender : Male, conf = 0.821
Age Output : [[0.48412544 0.3191519  0.02386817 0.00704233 0.14701316 0.01690866
  0.00121643 0.00067384]]
Age : (0-2), conf = 0.484
time : 0.100
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.962
Age Output : [[0.00740583 0.00658178 0.00432135 0.37720215 0.32958    0.2666802
  0.00319303 0.00503561]]
Age : (15-20), conf = 0.377
time : 0.081
No face Detected, Checking next frame
No face Detected, Checking next frame
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.966
Age Output : [[0.00754532 0.00690814 0.00339414 0.20585142 0.7228115  0.0513054
  0.00102567 0.00115842]]
Age : (25-32), conf = 0.723
time : 0.082
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.973
Age Output : [[0.08552981 0.13460359 0.02057277 0.45430288 0.2399675  0.06168251
  0.00167913 0.00166185]]
Age : (15-20), conf = 0.454
time : 0.101
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.982
Age Output : [[5.1554567e-03 1.7024696e-02 8.0908192e-03 7.0362592e-01 2.1410578e-01
  5.0619867e-02 6.6305575e-04 7.1434624e-04]]
Age : (15-20), conf = 0.704
time : 0.118
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.710
Age Output : [[1.4704879e-03 3.1041391e-03 8.3559874e-04 1.2279199e-03 9.9173766e-01
  1.5240180e-03 6.5419699e-05 3.4729728e-05]]
Age : (25-32), conf = 0.992
time : 0.130
Gender : Female, conf = 0.847
Age Output : [[5.4535199e-06 2.4481151e-05 4.2450858e-05 3.6126046e-04 9.9930501e-01
  2.5388060e-04 4.6449327e-06 2.8944457e-06]]
Age : (25-32), conf = 0.999
time : 0.106
Gender : Female, conf = 0.562
Age Output : [[3.8861592e-05 3.9968989e-04 3.7555344e-04 2.1482527e-03 9.9589133e-01
  1.1150448e-03 1.9810264e-05 1.1447164e-05]]
Age : (25-32), conf = 0.996
time : 0.126
Gender : Male, conf = 0.784
Age Output : [[8.0906670e-05 7.3145627e-04 4.1840179e-04 1.0331336e-03 9.9725062e-01
  4.5846755e-04 1.5566851e-05 1.1360262e-05]]
Age : (25-32), conf = 0.997
time : 0.105
Gender : Male, conf = 0.540
Age Output : [[2.5172159e-03 1.8788192e-02 1.3611139e-02 2.9826357e-03 9.5666468e-01
  5.0664227e-03 2.3393967e-04 1.3581393e-04]]
Age : (25-32), conf = 0.957
time : 0.122
Gender : Female, conf = 0.975
Age Output : [[1.3198168e-04 2.3495140e-04 1.7497176e-04 4.0217972e-04 9.9755836e-01
  1.4372206e-03 3.2348096e-05 2.7930651e-05]]
Age : (25-32), conf = 0.998
time : 0.116
Gender : Female, conf = 0.945
Age Output : [[1.5012747e-01 4.8385125e-02 2.2636790e-02 1.1914971e-03 7.7178204e-01
  5.2412571e-03 2.7343293e-04 3.6243466e-04]]
Age : (25-32), conf = 0.772
time : 0.116
Gender : Female, conf = 0.986
Age Output : [[1.1854619e-04 3.8682349e-04 2.3328543e-03 7.9506222e-05 9.9642628e-01
  6.1494304e-04 2.2368922e-05 1.8774539e-05]]
Age : (25-32), conf = 0.996
time : 0.084
Gender : Female, conf = 0.939
Age Output : [[6.7950954e-05 6.8501867e-03 1.8901648e-03 4.2644513e-04 9.9019802e-01
  5.3947419e-04 1.7912194e-05 9.7504862e-06]]
Age : (25-32), conf = 0.990
time : 0.093
Gender : Female, conf = 0.678
Age Output : [[1.5011548e-04 8.2430746e-03 2.6907099e-03 2.0992632e-03 9.8573744e-01
  1.0024285e-03 5.1184605e-05 2.5764151e-05]]
Age : (25-32), conf = 0.986
time : 0.080
Gender : Female, conf = 0.717
Age Output : [[4.6339948e-03 1.7773722e-01 1.6372997e-02 5.6732446e-03 7.9215235e-01
  3.0642461e-03 2.2518418e-04 1.4084064e-04]]
Age : (25-32), conf = 0.792
time : 0.104
Gender : Female, conf = 0.933
Age Output : [[1.3075004e-02 2.0893054e-01 6.6509925e-02 2.4385268e-02 6.7104578e-01
  1.5386599e-02 3.3724317e-04 3.2956779e-04]]
Age : (25-32), conf = 0.671
time : 0.114
Gender : Female, conf = 0.569
Age Output : [[2.4209209e-02 2.0738696e-01 6.8894595e-02 2.0645792e-02 6.4111209e-01
  3.6644083e-02 5.3866417e-04 5.6859641e-04]]
Age : (25-32), conf = 0.641
time : 0.112
Gender : Female, conf = 0.641
Age Output : [[0.02799669 0.34680232 0.16712275 0.01727998 0.40440938 0.03538499
  0.00045853 0.00054537]]
Age : (25-32), conf = 0.404
Gender : Male, conf = 0.959
Age Output : [[6.5716172e-06 2.8014005e-05 7.6339897e-03 1.5422729e-01 7.7691376e-01
  6.0054652e-02 5.0996483e-04 6.2579266e-04]]
Age : (25-32), conf = 0.777
time : 0.203
Gender : Male, conf = 0.889
Age Output : [[2.7601572e-04 2.7319433e-03 1.6812813e-02 8.8366771e-01 7.8902997e-02
  1.6254378e-02 7.1486656e-04 6.3934585e-04]]
Age : (15-20), conf = 0.884
Gender : Male, conf = 0.569
Age Output : [[6.0565220e-03 6.3430101e-02 5.4815147e-02 1.9232571e-02 8.3396685e-01
  2.2200309e-02 1.0322007e-04 1.9533090e-04]]
Age : (25-32), conf = 0.834
time : 0.190
Gender : Male, conf = 0.664
Age Output : [[1.8218788e-03 3.3811707e-02 4.4650789e-02 3.6019627e-02 8.7706184e-01
  6.4077377e-03 8.5651911e-05 1.4085192e-04]]
Age : (25-32), conf = 0.877
Gender : Male, conf = 0.941
Age Output : [[1.0688781e-04 2.9525680e-03 7.3489703e-02 7.5949377e-01 1.4892125e-01
  1.4228684e-02 3.4886150e-04 4.5834226e-04]]
Age : (15-20), conf = 0.759
time : 0.126
Gender : Female, conf = 0.619
Age Output : [[3.3280766e-04 1.3361170e-02 3.0828850e-02 3.5342909e-02 9.1646653e-01
  3.5409317e-03 4.5033783e-05 8.1766972e-05]]
Age : (25-32), conf = 0.916
Gender : Male, conf = 0.946
Age Output : [[4.3255102e-04 2.2865348e-02 5.6885209e-02 8.8883358e-01 2.0392409e-02
  1.0060515e-02 2.5882581e-04 2.7144302e-04]]
Age : (15-20), conf = 0.889
time : 0.127
Gender : Male, conf = 0.773
Age Output : [[2.8927127e-04 1.5069078e-02 3.4595340e-02 2.2071270e-02 9.2026484e-01
  7.6306020e-03 3.4042754e-05 4.5649169e-05]]
Age : (25-32), conf = 0.920
Gender : Male, conf = 0.963
Age Output : [[2.7617920e-04 1.2345047e-02 4.8206139e-02 4.4551134e-01 3.4668580e-01
  1.4317130e-01 1.5755398e-03 2.2286649e-03]]
Age : (15-20), conf = 0.446
time : 0.127
Gender : Male, conf = 0.961
Age Output : [[6.3330855e-04 2.5588673e-02 4.2905819e-02 5.6982592e-02 8.6655438e-01
  7.1726991e-03 6.2892861e-05 9.9567005e-05]]
Age : (25-32), conf = 0.867
Gender : Male, conf = 0.987
Age Output : [[2.2272227e-02 6.5995771e-01 1.1475277e-01 1.7411566e-01 1.4011602e-02
  1.3320964e-02 5.7704106e-04 9.9210651e-04]]
Age : (4-6), conf = 0.660
time : 0.123
Gender : Male, conf = 0.598
Age Output : [[8.5297093e-04 2.6060894e-02 3.2182559e-02 5.0197188e-02 8.8178325e-01
  8.7661156e-03 6.2574196e-05 9.4544877e-05]]
Age : (25-32), conf = 0.882
Gender : Male, conf = 0.914
Age Output : [[0.0943229  0.52435917 0.03597167 0.18016201 0.05635787 0.09635033
  0.00636785 0.00610812]]
Age : (4-6), conf = 0.524
time : 0.145
Gender : Male, conf = 0.825
Age Output : [[8.0188276e-04 2.0445008e-02 2.6690492e-02 6.3481010e-02 8.8335460e-01
  5.0776037e-03 5.8169964e-05 9.1335460e-05]]
Age : (25-32), conf = 0.883
Gender : Male, conf = 0.891
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[0.04408142 0.09195632 0.03033783 0.23615026 0.08016987 0.47479153
  0.01055998 0.03195272]]
Age : (38-43), conf = 0.475
time : 0.150
Gender : Male, conf = 0.661
Age Output : [[3.3027157e-03 9.4510876e-02 6.9711335e-02 2.2093536e-02 8.0598164e-01
  4.2539095e-03 6.0982453e-05 8.4949708e-05]]
Age : (25-32), conf = 0.806
time : 0.095
Gender : Male, conf = 0.719
Age Output : [[1.9411437e-04 6.2014614e-03 6.4972267e-02 5.5706860e-03 9.2164469e-01
  1.3679267e-03 2.3701345e-05 2.5058760e-05]]
Age : (25-32), conf = 0.922
Gender : Male, conf = 0.931
Age Output : [[0.01199715 0.01257299 0.00556546 0.0856571  0.2540495  0.6149881
  0.00940883 0.00576087]]
Age : (38-43), conf = 0.615
time : 0.138
Gender : Female, conf = 0.746
Age Output : [[1.1151211e-04 3.3532111e-03 1.3397568e-02 5.2722514e-02 9.2766148e-01
  2.7128800e-03 1.4938662e-05 2.5881376e-05]]
Age : (25-32), conf = 0.928
Gender : Male, conf = 0.988
Age Output : [[1.5702490e-03 2.1949636e-02 4.6297103e-02 6.3501632e-01 9.5232733e-02
  1.9854167e-01 3.2990237e-04 1.0623425e-03]]
Age : (15-20), conf = 0.635
time : 0.132
Gender : Male, conf = 0.759
Age Output : [[5.9594773e-04 2.3842538e-02 3.7550036e-02 1.5415219e-02 9.2049497e-01
  2.0223085e-03 3.2452026e-05 4.6401976e-05]]
Age : (25-32), conf = 0.920
Gender : Male, conf = 0.979
Age Output : [[0.00205712 0.02003793 0.01932697 0.52059805 0.22309412 0.21089038
  0.00167437 0.00232107]]
Age : (15-20), conf = 0.521
time : 0.124
Gender : Female, conf = 0.702
Age Output : [[4.1683562e-04 1.0597073e-02 3.6965977e-02 5.3169206e-02 8.8902259e-01
  9.7490167e-03 3.2326807e-05 4.7042493e-05]]
Age : (25-32), conf = 0.889
Gender : Male, conf = 0.976
Age Output : [[0.00279917 0.05763402 0.02802813 0.4265994  0.28656507 0.19525485
  0.00176455 0.00135474]]
Age : (15-20), conf = 0.427
time : 0.130
Gender : Male, conf = 0.965
Age Output : [[2.4095179e-04 4.8192157e-03 2.0960236e-02 9.2075728e-03 9.6315444e-01
  1.5492931e-03 3.1191488e-05 3.7024914e-05]]
Age : (25-32), conf = 0.963
Gender : Male, conf = 0.961
Age Output : [[0.00242772 0.08206902 0.05256529 0.4118209  0.25200817 0.19603533
  0.00151891 0.00155467]]
Age : (15-20), conf = 0.412
time : 0.124
Gender : Male, conf = 0.772
Age Output : [[2.4565976e-04 6.5545789e-03 1.7186325e-02 2.3638261e-02 9.5008451e-01
  2.2370615e-03 2.0766391e-05 3.2837106e-05]]
Age : (25-32), conf = 0.950
Gender : Male, conf = 0.941
Age Output : [[0.02029003 0.13508822 0.04574728 0.30270413 0.13759884 0.34940332
  0.00510643 0.00406165]]
Age : (38-43), conf = 0.349
time : 0.138
Gender : Male, conf = 0.719
Age Output : [[1.5262711e-04 3.6997243e-03 2.0353865e-02 1.1882032e-02 9.6186936e-01
  1.9863441e-03 2.4971208e-05 3.1093805e-05]]
Age : (25-32), conf = 0.962
Gender : Male, conf = 0.937
Age Output : [[0.00821476 0.11577842 0.0364012  0.31192225 0.2693799  0.2504906
  0.00479063 0.00302219]]
Age : (15-20), conf = 0.312
time : 0.138
Gender : Male, conf = 0.788
Age Output : [[1.1796001e-04 2.3828975e-03 8.6774854e-03 1.2822706e-02 9.7451270e-01
  1.4522474e-03 1.4483676e-05 1.9478472e-05]]
Age : (25-32), conf = 0.975
Gender : Male, conf = 0.982
Age Output : [[0.05059829 0.17409484 0.04651777 0.3781814  0.09448177 0.24245985
  0.00673431 0.00693179]]
Age : (15-20), conf = 0.378
time : 0.138
Gender : Male, conf = 0.773
Age Output : [[1.6927060e-04 3.0156176e-03 3.2647948e-03 6.3755256e-03 9.8654115e-01
  6.0995424e-04 1.1039421e-05 1.2742309e-05]]
Age : (25-32), conf = 0.987
Gender : Male, conf = 0.956
Age Output : [[0.00082921 0.00756355 0.01371237 0.29939693 0.31468773 0.36064982
  0.00160544 0.00155493]]
Age : (38-43), conf = 0.361
time : 0.124
Gender : Female, conf = 0.679
Age Output : [[5.5780506e-04 1.4625689e-02 4.9704462e-02 1.8950332e-02 9.1215283e-01
  3.9024658e-03 4.5466473e-05 6.0974988e-05]]
Age : (25-32), conf = 0.912
Gender : Male, conf = 0.988
Age Output : [[0.0243963  0.0935247  0.06153945 0.43104088 0.10801253 0.2772241
  0.00159363 0.00266852]]
Age : (15-20), conf = 0.431
time : 0.128
Gender : Male, conf = 0.747
Age Output : [[1.2333575e-04 2.9874449e-03 1.9741731e-02 9.9726627e-03 9.6539426e-01
  1.7481939e-03 1.4043984e-05 1.8305702e-05]]
Age : (25-32), conf = 0.965
Gender : Male, conf = 0.968
Age Output : [[0.07219432 0.12311332 0.05274634 0.22495337 0.15525001 0.3582588
  0.00627297 0.00721082]]
Age : (38-43), conf = 0.358
time : 0.126
Gender : Male, conf = 0.984
Age Output : [[0.00251095 0.01263986 0.01456963 0.25234106 0.20920111 0.5037339
  0.00225667 0.00274685]]
Age : (38-43), conf = 0.504
Gender : Female, conf = 0.697
Age Output : [[5.0668452e-05 7.9835078e-04 6.2427339e-03 2.9973499e-03 9.8822081e-01
  1.6700726e-03 9.1515094e-06 1.0893586e-05]]
Age : (25-32), conf = 0.988
time : 0.122
Gender : Female, conf = 0.669
Age Output : [[1.47561223e-04 3.44408746e-03 1.92774367e-02 1.08094132e-02
  9.64095235e-01 2.19355058e-03 1.42903355e-05 1.84881137e-05]]
Age : (25-32), conf = 0.964
Gender : Male, conf = 0.983
Age Output : [[0.02037611 0.01322656 0.00837589 0.04907789 0.27022508 0.6190746
  0.01103899 0.00860483]]
Age : (38-43), conf = 0.619
time : 0.137
Gender : Male, conf = 0.954
Age Output : [[0.02211822 0.02417    0.01133927 0.16384183 0.24758662 0.5019311
  0.0174454  0.01156759]]
Age : (38-43), conf = 0.502
Gender : Female, conf = 0.700
Age Output : [[9.5658834e-05 2.2181091e-03 1.3602269e-02 7.7382973e-03 9.7505277e-01
  1.2645520e-03 1.1590389e-05 1.6745129e-05]]
Age : (25-32), conf = 0.975
time : 0.142
Gender : Male, conf = 0.981
Age Output : [[0.02833172 0.05234721 0.01660482 0.08570166 0.14810416 0.64097893
  0.01601292 0.01191852]]
Age : (38-43), conf = 0.641
Gender : Female, conf = 0.650
Age Output : [[1.8965797e-03 3.8660545e-02 5.6320477e-02 6.0774041e-03 8.9355409e-01
  3.4226601e-03 3.1083084e-05 3.7074511e-05]]
Age : (25-32), conf = 0.894
time : 0.124
Gender : Male, conf = 0.990
Age Output : [[0.20851345 0.19787396 0.03684573 0.15012321 0.07563204 0.30524367
  0.01246747 0.01330047]]
Age : (38-43), conf = 0.305
Gender : Female, conf = 0.760
Age Output : [[8.8356661e-05 2.4436319e-03 8.2350038e-03 1.3072122e-02 9.7505945e-01
  1.0749702e-03 1.1050140e-05 1.5489242e-05]]
Age : (25-32), conf = 0.975
time : 0.137
Gender : Male, conf = 0.951
Age Output : [[0.49030754 0.1362684  0.01807531 0.05216737 0.07555848 0.19628444
  0.01491524 0.01642331]]
Age : (0-2), conf = 0.490
Gender : Female, conf = 0.852
Age Output : [[5.50558150e-04 9.02205613e-03 1.00494936e-01 2.26648152e-02
  8.59896123e-01 7.27134617e-03 4.32428205e-05 5.69098993e-05]]
Age : (25-32), conf = 0.860
time : 0.143
Gender : Male, conf = 0.988
Age Output : [[0.04207636 0.05771947 0.02105362 0.34312853 0.17423058 0.33810934
  0.01171738 0.0119647 ]]
Age : (15-20), conf = 0.343
Gender : Female, conf = 0.878
Age Output : [[4.9965912e-03 8.1733689e-02 7.0578806e-02 2.1174146e-02 8.1723654e-01
  4.1633938e-03 5.2019186e-05 6.4780812e-05]]
Age : (25-32), conf = 0.817
time : 0.127
Gender : Male, conf = 0.993
Age Output : [[0.5745731  0.16140385 0.02025929 0.03108888 0.0336289  0.16560206
  0.00487837 0.00856552]]
Age : (0-2), conf = 0.575
Gender : Female, conf = 0.755
Age Output : [[1.6817439e-03 2.2872556e-02 3.0051934e-02 2.1615136e-02 9.2008173e-01
  3.6170525e-03 3.5402150e-05 4.4267294e-05]]
Age : (25-32), conf = 0.920
time : 0.136
Gender : Male, conf = 0.992
Age Output : [[0.4549256  0.1574535  0.02448412 0.10948974 0.04396859 0.19214492
  0.00338222 0.01415135]]
Age : (0-2), conf = 0.455
Gender : Female, conf = 0.724
Age Output : [[2.0096579e-03 3.5874218e-02 5.2128803e-02 2.2593781e-02 8.8023800e-01
  7.0312633e-03 5.3308941e-05 7.1003225e-05]]
Age : (25-32), conf = 0.880
time : 0.133
Gender : Male, conf = 0.885
Age Output : [[0.0057497  0.01273943 0.01140053 0.6717387  0.08763868 0.20622334
  0.00088453 0.00362517]]
Age : (15-20), conf = 0.672
Gender : Female, conf = 0.572
Age Output : [[1.5934377e-03 3.0644245e-02 9.1098681e-02 2.6178991e-02 8.4018141e-01
  1.0199349e-02 4.4820947e-05 5.8965092e-05]]
Age : (25-32), conf = 0.840
time : 0.122
Gender : Male, conf = 0.980
Age Output : [[0.04253228 0.0242301  0.01219941 0.24180916 0.13302715 0.5235726
  0.00350311 0.01912619]]
Age : (38-43), conf = 0.524
Gender : Female, conf = 0.919
Age Output : [[1.3837481e-03 3.8465813e-02 6.1727934e-02 2.0968240e-02 8.6868024e-01
  8.6384322e-03 6.4985608e-05 7.0560593e-05]]
Age : (25-32), conf = 0.869
time : 0.138
Gender : Male, conf = 0.955
Age Output : [[0.00724621 0.00858038 0.00780924 0.48314005 0.15310016 0.33116823
  0.00156341 0.00739243]]
Age : (15-20), conf = 0.483
Gender : Female, conf = 0.540
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[1.6968610e-03 1.7847603e-02 2.1178868e-02 1.1830205e-02 9.4351459e-01
  3.8260908e-03 5.3477877e-05 5.2431318e-05]]
Age : (25-32), conf = 0.944
time : 0.131
Gender : Male, conf = 0.911
Age Output : [[0.06262733 0.04065499 0.01383117 0.22961727 0.19122897 0.4322545
  0.00498949 0.02479621]]
Age : (38-43), conf = 0.432
Gender : Female, conf = 0.908
Age Output : [[1.8684295e-04 4.4774320e-03 1.0170695e-02 1.1002121e-02 9.7079766e-01
  3.3267848e-03 1.6877622e-05 2.1472220e-05]]
Age : (25-32), conf = 0.971
time : 0.131
Gender : Female, conf = 0.826
Age Output : [[1.5432631e-04 3.5880588e-03 7.0548132e-03 1.7373916e-03 9.8646551e-01
  9.7620831e-04 1.2918735e-05 1.0834259e-05]]
Age : (25-32), conf = 0.986
Gender : Male, conf = 0.901
Age Output : [[0.00565507 0.01165075 0.00745605 0.5670507  0.19299817 0.2088666
  0.00100031 0.00532245]]
Age : (15-20), conf = 0.567
time : 0.133
Gender : Female, conf = 0.857
Age Output : [[7.2097675e-05 1.9397526e-03 5.7623964e-03 2.0374015e-03 9.8945320e-01
  7.1051327e-04 1.2568704e-05 1.1988510e-05]]
Age : (25-32), conf = 0.989
Gender : Male, conf = 0.936
Age Output : [[0.03278289 0.05857084 0.02256458 0.5319856  0.1288154  0.21872087
  0.00130155 0.00525832]]
Age : (15-20), conf = 0.532
time : 0.135
Gender : Female, conf = 0.914
Age Output : [[1.8608558e-04 3.9306185e-03 4.9301190e-03 2.6145526e-03 9.8745281e-01
  8.5450424e-04 1.5877515e-05 1.5426720e-05]]
Age : (25-32), conf = 0.987
Gender : Male, conf = 0.934
Age Output : [[0.01227656 0.02457619 0.01891502 0.33382472 0.10761797 0.49193653
  0.0015202  0.00933286]]
Age : (38-43), conf = 0.492
time : 0.132
Gender : Male, conf = 0.981
Age Output : [[0.1981276  0.10451289 0.02668516 0.24798523 0.08517642 0.31369498
  0.00455304 0.01926464]]
Age : (38-43), conf = 0.314
Gender : Female, conf = 0.766
Age Output : [[2.6068245e-03 3.6021814e-02 2.0980582e-02 9.6052950e-03 9.2741871e-01
  3.2656018e-03 4.9179635e-05 5.1923147e-05]]
Age : (25-32), conf = 0.927
time : 0.137
Gender : Male, conf = 0.916
Age Output : [[0.22708842 0.14846471 0.0223275  0.3008995  0.06172711 0.21518856
  0.00762891 0.01667528]]
Age : (15-20), conf = 0.301
Gender : Female, conf = 0.941
Age Output : [[4.6232872e-04 1.0030079e-02 6.2258565e-03 1.9301781e-03 9.8048913e-01
  8.2186004e-04 1.9877982e-05 2.0821693e-05]]
Age : (25-32), conf = 0.980
time : 0.140
Gender : Male, conf = 0.979
Age Output : [[0.38871005 0.28790227 0.03509457 0.16304709 0.027016   0.09042968
  0.00209178 0.0057085 ]]
Age : (0-2), conf = 0.389
Gender : Male, conf = 0.532
Age Output : [[1.4107419e-03 1.8031452e-02 2.6457191e-02 1.4410365e-02 9.3328249e-01
  6.2026572e-03 8.9509791e-05 1.1556768e-04]]
Age : (25-32), conf = 0.933
time : 0.132
Gender : Male, conf = 0.980
Age Output : [[0.5192363  0.15221596 0.02660657 0.10696306 0.02586105 0.14916748
  0.00414516 0.01580435]]
Age : (0-2), conf = 0.519
Gender : Female, conf = 0.956
Age Output : [[8.2556289e-03 8.7191410e-02 3.2590002e-02 1.1064664e-02 8.5701609e-01
  3.6704578e-03 1.0850137e-04 1.0324738e-04]]
Age : (25-32), conf = 0.857
time : 0.138
Gender : Male, conf = 0.991
Age Output : [[0.33989745 0.27678522 0.02816768 0.14481096 0.04182852 0.15417646
  0.0043298  0.01000388]]
Age : (0-2), conf = 0.340
Gender : Female, conf = 0.821
Age Output : [[2.7314676e-03 5.6299366e-02 1.2549114e-02 7.8462940e-03 9.1840196e-01
  2.0380046e-03 6.5366861e-05 6.8397610e-05]]
Age : (25-32), conf = 0.918
time : 0.116
Gender : Female, conf = 0.770
Age Output : [[1.6340122e-03 2.5864733e-02 1.1432262e-02 1.2246884e-02 9.4693881e-01
  1.7810974e-03 4.6747489e-05 5.5403580e-05]]
Age : (25-32), conf = 0.947
Gender : Male, conf = 0.952
Age Output : [[0.20879556 0.14981766 0.03083821 0.399076   0.06135166 0.13814747
  0.0023805  0.00959299]]
Age : (15-20), conf = 0.399
time : 0.135
Gender : Female, conf = 0.593
Age Output : [[4.0987850e-04 6.5559270e-03 2.2223471e-03 3.0362720e-03 9.8699236e-01
  7.3532679e-04 2.4658362e-05 2.3168986e-05]]
Age : (25-32), conf = 0.987
Gender : Male, conf = 0.970
Age Output : [[0.21241073 0.24328853 0.0298822  0.38635486 0.04063895 0.0772758
  0.00155892 0.00859004]]
Age : (15-20), conf = 0.386
time : 0.132
Gender : Female, conf = 0.587
Age Output : [[2.3761822e-02 1.2590243e-01 1.0295233e-02 5.9600794e-03 8.3242840e-01
  1.4877146e-03 8.6484077e-05 7.7843149e-05]]
Age : (25-32), conf = 0.832
Gender : Male, conf = 0.891
Age Output : [[0.22050919 0.17665009 0.03453412 0.3607538  0.04500733 0.14163414
  0.00331641 0.01759492]]
Age : (15-20), conf = 0.361
time : 0.139
No face Detected, Checking next frame
Gender : Male, conf = 0.971
Age Output : [[0.05984336 0.12434097 0.03294411 0.51311934 0.0647639  0.18909039
  0.00365124 0.01224669]]
Age : (15-20), conf = 0.513
time : 0.095
Gender : Male, conf = 0.665
Age Output : [[2.7309195e-03 1.3887580e-02 2.2259557e-03 4.1277260e-03 9.7562921e-01
  1.2948217e-03 5.5343429e-05 4.8556922e-05]]
Age : (25-32), conf = 0.976
Gender : Male, conf = 0.971
Age Output : [[0.0424362  0.11287227 0.02971318 0.2991219  0.23208688 0.27362415
  0.00299849 0.00714699]]
Age : (15-20), conf = 0.299
time : 0.125
Gender : Male, conf = 0.583
Age Output : [[4.8684063e-03 3.3193622e-02 6.7274631e-03 6.2008454e-03 9.4700509e-01
  1.8997627e-03 5.2794232e-05 5.2012179e-05]]
Age : (25-32), conf = 0.947
time : 0.100
Gender : Male, conf = 0.704
Age Output : [[3.0746323e-04 6.6783377e-03 6.2139020e-03 9.4483467e-03 9.7558957e-01
  1.7171104e-03 2.0172096e-05 2.5154039e-05]]
Age : (25-32), conf = 0.976
Gender : Male, conf = 0.934
Age Output : [[0.17155083 0.41382805 0.0410384  0.26768455 0.03420106 0.06590036
  0.00194346 0.00385329]]
Age : (4-6), conf = 0.414
time : 0.129
Gender : Female, conf = 0.563
Age Output : [[1.15883872e-02 5.43747023e-02 6.07002154e-03 6.59020944e-03
  9.17667747e-01 3.51748266e-03 1.05774605e-04 8.56085826e-05]]
Age : (25-32), conf = 0.918
time : 0.098
Gender : Male, conf = 0.660
Age Output : [[1.50722265e-02 1.12379216e-01 1.68579873e-02 1.67445373e-02
  8.33967328e-01 4.69125621e-03 1.43143043e-04 1.44299018e-04]]
Age : (25-32), conf = 0.834
time : 0.087
Gender : Male, conf = 0.660
Age Output : [[1.50722265e-02 1.12379216e-01 1.68579873e-02 1.67445373e-02
  8.33967328e-01 4.69125621e-03 1.43143043e-04 1.44299018e-04]]
Age : (25-32), conf = 0.834
time : 0.100
Gender : Male, conf = 0.688
Age Output : [[3.0583492e-03 1.1237624e-02 1.8049553e-03 1.8331520e-03 9.8072398e-01
  1.2600890e-03 4.6158802e-05 3.5686007e-05]]
Age : (25-32), conf = 0.981
time : 0.088
No face Detected, Checking next frame
Gender : Female, conf = 0.536
Age Output : [[6.2321760e-02 1.1292015e-01 9.2332345e-03 1.1735325e-02 7.9849887e-01
  4.8005222e-03 2.6019401e-04 2.3001489e-04]]
Age : (25-32), conf = 0.798
time : 0.096
Gender : Male, conf = 0.615
Age Output : [[6.1505516e-03 3.7021745e-02 5.1906938e-03 6.9402680e-03 9.4303429e-01
  1.5522426e-03 5.5412271e-05 5.4774275e-05]]
Age : (25-32), conf = 0.943
Gender : Male, conf = 0.991
Age Output : [[0.10104267 0.1717583  0.05185167 0.19539757 0.06896135 0.36657616
  0.00919993 0.03521236]]
Age : (38-43), conf = 0.367
time : 0.131
Gender : Male, conf = 0.924
Age Output : [[4.1760760e-03 3.6360439e-02 5.1805065e-03 1.0255429e-02 9.4141161e-01
  2.4792971e-03 6.2858104e-05 7.3882089e-05]]
Age : (25-32), conf = 0.941
time : 0.083
Gender : Male, conf = 0.513
Age Output : [[9.9234223e-02 2.4499303e-01 1.3897473e-02 7.5827893e-03 6.2999827e-01
  3.9179455e-03 2.0647433e-04 1.6983204e-04]]
Age : (25-32), conf = 0.630
Gender : Male, conf = 0.954
Age Output : [[0.01503101 0.03729349 0.05077133 0.44004285 0.05973165 0.37380904
  0.00391507 0.01940562]]
Age : (15-20), conf = 0.440
time : 0.123
Gender : Male, conf = 0.904
Age Output : [[1.3045798e-02 1.6120942e-01 1.5939249e-02 2.4744183e-02 7.8186017e-01
  2.9366319e-03 1.3172648e-04 1.3287387e-04]]
Age : (25-32), conf = 0.782
time : 0.096
Gender : Male, conf = 0.750
Age Output : [[4.1954680e-03 1.6135413e-02 2.0367177e-03 6.0924101e-03 9.7001159e-01
  1.4174535e-03 5.2820553e-05 5.8062786e-05]]
Age : (25-32), conf = 0.970
time : 0.088
Gender : Male, conf = 0.750
Age Output : [[4.1954680e-03 1.6135413e-02 2.0367177e-03 6.0924101e-03 9.7001159e-01
  1.4174535e-03 5.2820553e-05 5.8062786e-05]]
Age : (25-32), conf = 0.970
time : 0.099
No face Detected, Checking next frame
Gender : Female, conf = 0.559
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[1.1566600e-03 1.3815507e-02 4.8976005e-03 1.3404317e-02 9.6570480e-01
  9.6418813e-04 2.5704116e-05 3.1289292e-05]]
Age : (25-32), conf = 0.966
time : 0.102
Gender : Male, conf = 0.945
Age Output : [[5.1268332e-02 1.5089577e-01 1.0011120e-02 1.0491183e-02 7.7485096e-01
  2.2263883e-03 1.3786653e-04 1.1832193e-04]]
Age : (25-32), conf = 0.775
Gender : Male, conf = 0.966
Age Output : [[1.06269438e-02 2.51376573e-02 1.97217707e-02 7.93637633e-01
  1.13403045e-01 3.42375897e-02 6.92894682e-04 2.54243077e-03]]
Age : (15-20), conf = 0.794
time : 0.129
Gender : Male, conf = 0.521
Age Output : [[0.00459418 0.01543776 0.02979805 0.70945305 0.17715631 0.05624181
  0.00131437 0.00600451]]
Age : (15-20), conf = 0.709
time : 0.099
Gender : Male, conf = 0.845
Age Output : [[7.3507597e-04 6.6971686e-03 2.4905319e-03 5.5595501e-03 9.8353899e-01
  9.2368235e-04 2.4983307e-05 3.0045914e-05]]
Age : (25-32), conf = 0.984
time : 0.086
Gender : Male, conf = 0.931
Age Output : [[0.00532496 0.00633175 0.00628579 0.55831176 0.29432482 0.11731058
  0.0018707  0.01023964]]
Age : (15-20), conf = 0.558
Gender : Male, conf = 0.732
Age Output : [[1.65883806e-02 4.56525348e-02 6.78096153e-03 6.07927470e-03
  9.21939015e-01 2.73679127e-03 1.21205303e-04 1.01744976e-04]]
Age : (25-32), conf = 0.922
time : 0.132
Gender : Male, conf = 0.841
Age Output : [[2.3273099e-03 9.7901737e-03 1.9115133e-03 1.5511198e-03 9.8342574e-01
  9.3883259e-04 3.2336728e-05 2.3017203e-05]]
Age : (25-32), conf = 0.983
Gender : Male, conf = 0.849
Age Output : [[0.03478291 0.0177594  0.00896076 0.15259945 0.5735719  0.19356455
  0.0043163  0.01444465]]
Age : (25-32), conf = 0.574
time : 0.152
Gender : Male, conf = 0.641
Age Output : [[0.13564496 0.08798583 0.0189165  0.3957798  0.21621804 0.13101949
  0.0034993  0.01093612]]
Age : (15-20), conf = 0.396
Gender : Male, conf = 0.760
Age Output : [[3.2739699e-02 8.9147501e-02 6.6278432e-03 4.5068478e-03 8.6410820e-01
  2.6521652e-03 1.2222026e-04 9.5500203e-05]]
Age : (25-32), conf = 0.864
time : 0.127
Gender : Male, conf = 0.911
Age Output : [[6.1506800e-02 1.1671741e-01 7.9821404e-03 6.4582922e-03 8.0326551e-01
  3.7944317e-03 1.4752561e-04 1.2782555e-04]]
Age : (25-32), conf = 0.803
time : 0.097
Gender : Male, conf = 0.980
Age Output : [[0.02832817 0.06521807 0.02105441 0.4770187  0.34458563 0.05855818
  0.00138023 0.00385657]]
Age : (15-20), conf = 0.477
time : 0.087
Gender : Male, conf = 0.994
Age Output : [[1.9566046e-02 7.4946016e-02 3.1824257e-02 7.6560825e-01 6.9862165e-02
  3.5184115e-02 6.7361922e-04 2.3355288e-03]]
Age : (15-20), conf = 0.766
Gender : Female, conf = 0.521
Age Output : [[1.6084570e-01 2.1209307e-01 9.8493677e-03 5.7634828e-03 6.0745186e-01
  3.6311324e-03 2.0996433e-04 1.5536163e-04]]
Age : (25-32), conf = 0.607
time : 0.138
Gender : Male, conf = 0.991
Age Output : [[0.00215337 0.00288938 0.00585775 0.23410761 0.49269098 0.25402775
  0.00103847 0.00723467]]
Age : (25-32), conf = 0.493
Gender : Male, conf = 0.868
Age Output : [[4.9704354e-02 2.8853911e-01 2.3957284e-02 1.7911360e-02 6.1455852e-01
  5.0001717e-03 1.5542658e-04 1.7374278e-04]]
Age : (25-32), conf = 0.615
time : 0.131
Gender : Male, conf = 0.990
Age Output : [[0.16843922 0.30052674 0.02765487 0.31824082 0.10648367 0.06770439
  0.00378007 0.00717031]]
Age : (15-20), conf = 0.318
Gender : Male, conf = 0.604
Age Output : [[8.0118058e-03 1.9129828e-01 4.3081012e-02 2.9787395e-02 7.2229594e-01
  5.3563970e-03 7.2443436e-05 9.6738797e-05]]
Age : (25-32), conf = 0.722
time : 0.124
Gender : Male, conf = 0.947
Age Output : [[0.00125726 0.003167   0.00713185 0.1383679  0.37030128 0.47277796
  0.00093903 0.00605773]]
Age : (38-43), conf = 0.473
Gender : Male, conf = 0.827
Age Output : [[6.3010375e-03 5.2544780e-02 9.3204211e-03 7.1978369e-03 9.2293024e-01
  1.6312085e-03 3.9676637e-05 3.4758232e-05]]
Age : (25-32), conf = 0.923
time : 0.138
Gender : Male, conf = 0.960
Age Output : [[0.00257641 0.00780181 0.01314284 0.3567654  0.13200319 0.4811318
  0.00138884 0.00518976]]
Age : (38-43), conf = 0.481
Gender : Male, conf = 0.881
Age Output : [[2.1134458e-02 2.0708442e-01 3.6438577e-02 2.0880124e-02 7.0851159e-01
  5.7845395e-03 7.3717252e-05 9.2514718e-05]]
Age : (25-32), conf = 0.709
time : 0.140
Gender : Male, conf = 0.725
Age Output : [[2.8922834e-04 2.1078081e-03 1.8846149e-03 3.6972493e-02 9.5558208e-01
  3.0997151e-03 2.4984965e-05 3.9072424e-05]]
Age : (25-32), conf = 0.956
Gender : Male, conf = 0.955
Age Output : [[0.00647918 0.00930706 0.00782426 0.1570171  0.24056236 0.5598071
  0.00386584 0.01513714]]
Age : (38-43), conf = 0.560
time : 0.130
Gender : Male, conf = 0.943
Age Output : [[0.01070693 0.00849189 0.0056567  0.07023484 0.4098339  0.47116846
  0.01069419 0.01321305]]
Age : (38-43), conf = 0.471
Gender : Male, conf = 0.714
Age Output : [[6.8745941e-02 3.6818179e-01 3.1145580e-02 1.4195618e-02 5.1137507e-01
  5.9982003e-03 1.8153261e-04 1.7623366e-04]]
Age : (25-32), conf = 0.511
time : 0.128
Gender : Male, conf = 0.957
Age Output : [[0.01411816 0.03683177 0.02963548 0.5006207  0.1982742  0.21012674
  0.00197661 0.00841626]]
Age : (15-20), conf = 0.501
Gender : Male, conf = 0.557
Age Output : [[5.6017088e-03 9.3582176e-02 5.6933753e-02 4.9070746e-02 7.8979814e-01
  4.8457240e-03 6.7758760e-05 9.9987425e-05]]
Age : (25-32), conf = 0.790
time : 0.126
Gender : Male, conf = 0.977
Age Output : [[0.00443437 0.00319197 0.00601169 0.03386379 0.42818975 0.5118774
  0.00399815 0.00843295]]
Age : (38-43), conf = 0.512
time : 0.085
Gender : Male, conf = 0.858
Age Output : [[0.00599275 0.0070112  0.01176313 0.04897219 0.5792056  0.330318
  0.00498571 0.01175144]]
Age : (25-32), conf = 0.579
Gender : Male, conf = 0.908
Age Output : [[7.7039830e-04 1.0485542e-02 6.5176911e-03 3.3389982e-02 9.4670743e-01
  2.0588662e-03 2.9965498e-05 4.0118692e-05]]
Age : (25-32), conf = 0.947
time : 0.143
Gender : Male, conf = 0.815
Age Output : [[0.05833597 0.05516713 0.01513024 0.10393012 0.4990899  0.24761471
  0.00974949 0.01098249]]
Age : (25-32), conf = 0.499
time : 0.086
Gender : Male, conf = 0.874
Age Output : [[0.1442756  0.05792614 0.01278702 0.03845101 0.42033598 0.2977638
  0.0133068  0.01515367]]
Age : (25-32), conf = 0.420
Gender : Female, conf = 0.559
Age Output : [[3.5138819e-02 1.9302922e-01 2.1119149e-02 1.2217470e-02 7.3132879e-01
  6.8565663e-03 1.4976411e-04 1.6027338e-04]]
Age : (25-32), conf = 0.731
time : 0.133
Gender : Female, conf = 0.562
Age Output : [[3.6641255e-03 3.4687210e-02 2.9424125e-02 5.7423068e-03 9.1857630e-01
  7.7946922e-03 5.4238448e-05 5.6889454e-05]]
Age : (25-32), conf = 0.919
Gender : Male, conf = 0.692
Age Output : [[0.06312565 0.06324945 0.0152197  0.11873648 0.52025396 0.19628973
  0.00582793 0.01729707]]
Age : (25-32), conf = 0.520
time : 0.143
Gender : Male, conf = 0.920
Age Output : [[0.01726853 0.02771595 0.01342677 0.16866906 0.36724356 0.37220848
  0.01671204 0.01675565]]
Age : (38-43), conf = 0.372
Gender : Male, conf = 0.782
Age Output : [[4.4951480e-06 8.4193214e-04 9.7275032e-03 2.3469147e-03 9.8584890e-01
  1.2115543e-03 7.6202537e-06 1.1052123e-05]]
Age : (25-32), conf = 0.986
time : 0.119
Gender : Male, conf = 0.939
Age Output : [[0.03602611 0.0243845  0.00907009 0.08131097 0.44882149 0.36527276
  0.01884976 0.01626429]]
Age : (25-32), conf = 0.449
Gender : Female, conf = 0.911
Age Output : [[2.1984772e-07 6.4082269e-05 9.1530666e-02 1.0843806e-01 7.9117161e-01
  8.7591652e-03 7.4258182e-06 2.8806839e-05]]
Age : (25-32), conf = 0.791
time : 0.140
Gender : Male, conf = 0.940
Age Output : [[7.8572702e-01 2.0561422e-01 5.5593485e-03 1.7706629e-04 2.5480676e-03
  2.2320605e-04 8.1426530e-05 6.9659967e-05]]
Age : (0-2), conf = 0.786
time : 0.085
Gender : Male, conf = 0.940
Age Output : [[7.8572702e-01 2.0561422e-01 5.5593485e-03 1.7706629e-04 2.5480676e-03
  2.2320605e-04 8.1426530e-05 6.9659967e-05]]
Age : (0-2), conf = 0.786
time : 0.084
Gender : Male, conf = 1.000
Age Output : [[5.7268041e-01 4.2506179e-01 1.4256189e-03 9.6782169e-05 4.8927893e-04
  6.1973726e-05 1.2434757e-04 5.9883736e-05]]
Age : (0-2), conf = 0.573
time : 0.085
Gender : Male, conf = 0.965
Age Output : [[0.6168144  0.30305654 0.00776338 0.00302193 0.06144949 0.00355567
  0.0034506  0.00088794]]
Age : (0-2), conf = 0.617
time : 0.110
Gender : Male, conf = 0.607
Age Output : [[0.5262284  0.03305997 0.0170934  0.00245484 0.37122557 0.02213166
  0.00863916 0.0191669 ]]
Age : (0-2), conf = 0.526
time : 0.129
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.576
Age Output : [[8.5648292e-01 5.0418276e-02 2.5237387e-03 1.0036149e-03 8.6615272e-02
  1.4994487e-03 1.0350510e-03 4.2153421e-04]]
Age : (0-2), conf = 0.856
time : 0.122
Gender : Male, conf = 0.986
Age Output : [[8.3831245e-01 1.0437654e-01 7.4509373e-03 6.9787446e-04 4.7778469e-02
  1.0185097e-03 2.3060307e-04 1.3462022e-04]]
Age : (0-2), conf = 0.838
time : 0.116
Gender : Male, conf = 0.711
Age Output : [[9.4686514e-01 4.7372058e-02 1.4305222e-03 1.5550424e-04 3.9054463e-03
  1.5104868e-04 8.9519497e-05 3.0721218e-05]]
Age : (0-2), conf = 0.947
time : 0.135
Gender : Male, conf = 0.987
Age Output : [[6.1142474e-01 3.5548958e-01 4.9231509e-03 1.3282566e-03 2.5314597e-02
  5.9452787e-04 7.8514067e-04 1.4004488e-04]]
Age : (0-2), conf = 0.611
time : 0.114
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.811
Age Output : [[4.9197143e-01 4.9354240e-01 3.8563241e-03 6.7582616e-04 8.8365749e-03
  7.7147741e-04 1.6096038e-04 1.8517842e-04]]
Age : (4-6), conf = 0.494
time : 0.130
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.626
Age Output : [[7.8703886e-01 2.0603052e-01 3.1380896e-03 7.4089714e-04 1.7445481e-03
  7.2904408e-04 2.3814861e-04 3.4003850e-04]]
Age : (0-2), conf = 0.787
time : 0.116
Gender : Female, conf = 0.878
Age Output : [[6.6513604e-01 3.0535108e-01 1.5538603e-02 4.9469760e-03 5.3131417e-03
  2.4858832e-03 3.3234034e-04 8.9584442e-04]]
Age : (0-2), conf = 0.665
time : 0.108
Gender : Male, conf = 0.607
Age Output : [[0.67364717 0.2542909  0.01179527 0.01164882 0.02952021 0.01442459
  0.0020717  0.00260132]]
Age : (0-2), conf = 0.674
time : 0.101
Gender : Male, conf = 0.718
Age Output : [[8.22559536e-01 1.66547224e-01 5.30682318e-03 1.78915018e-03
  2.51900731e-03 9.29047761e-04 1.06852916e-04 2.42299400e-04]]
Age : (0-2), conf = 0.823
time : 0.097
Gender : Female, conf = 0.847
Age Output : [[0.6968878  0.22105032 0.02930717 0.01062524 0.0249627  0.01315136
  0.00116681 0.00284857]]
Age : (0-2), conf = 0.697
time : 0.105
Gender : Female, conf = 0.916
Age Output : [[0.6574347  0.13903773 0.03643888 0.024932   0.09033319 0.04462336
  0.00166322 0.00553683]]
Age : (0-2), conf = 0.657
time : 0.119
Gender : Male, conf = 0.532
Age Output : [[8.8935310e-01 1.0548266e-01 2.4238583e-03 3.5277862e-04 1.4378310e-03
  4.3569802e-04 1.3716327e-04 3.7688561e-04]]
Age : (0-2), conf = 0.889
time : 0.115
Gender : Female, conf = 0.932
Age Output : [[0.4260986  0.3693861  0.05763951 0.02544273 0.07887793 0.03375126
  0.0013054  0.00749843]]
Age : (0-2), conf = 0.426
time : 0.101
Gender : Female, conf = 0.969
Age Output : [[7.7919215e-01 1.7920849e-01 2.6274670e-02 4.1477168e-03 4.6275170e-03
  3.8530326e-03 2.3364363e-04 2.4628523e-03]]
Age : (0-2), conf = 0.779
time : 0.137
Gender : Female, conf = 0.698
Age Output : [[6.2128818e-01 3.3351383e-01 2.3850206e-02 6.4346301e-03 9.3010049e-03
  3.6115905e-03 5.0371460e-04 1.4968119e-03]]
Age : (0-2), conf = 0.621
time : 0.147
Gender : Female, conf = 0.990
Age Output : [[0.56651115 0.12051275 0.0359805  0.01925991 0.14298461 0.0895826
  0.00641443 0.018754  ]]
Age : (0-2), conf = 0.567
time : 0.105
Gender : Female, conf = 0.745
Age Output : [[4.3535420e-01 5.4290438e-01 1.2435071e-02 3.0107263e-03 3.8484540e-03
  1.8069140e-03 2.0765427e-04 4.3259366e-04]]
Age : (4-6), conf = 0.543
time : 0.100
Gender : Female, conf = 0.724
Age Output : [[3.9749214e-01 5.8484107e-01 8.6139310e-03 2.6384592e-03 4.8188344e-03
  9.5292338e-04 2.4905332e-04 3.9366260e-04]]
Age : (4-6), conf = 0.585
time : 0.085
Gender : Female, conf = 0.724
Age Output : [[3.9749214e-01 5.8484107e-01 8.6139310e-03 2.6384592e-03 4.8188344e-03
  9.5292338e-04 2.4905332e-04 3.9366260e-04]]
Age : (4-6), conf = 0.585
time : 0.103
Gender : Female, conf = 0.914
Age Output : [[4.9949822e-01 4.8419446e-01 9.9476157e-03 2.1977208e-03 1.7651680e-03
  1.4148109e-03 2.2284180e-04 7.5917057e-04]]
Age : (0-2), conf = 0.499
time : 0.085
Gender : Female, conf = 0.683
Age Output : [[4.7176594e-01 5.2063096e-01 4.3584136e-03 8.5003825e-04 1.5376949e-03
  5.0960726e-04 1.4395149e-04 2.0341871e-04]]
Age : (4-6), conf = 0.521
time : 0.098
Gender : Female, conf = 0.842
Age Output : [[7.9746956e-01 1.9700494e-01 3.2415765e-03 2.9362290e-04 1.0882681e-03
  3.6785085e-04 1.3356745e-04 4.0058637e-04]]
Age : (0-2), conf = 0.797
time : 0.087
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.686
Age Output : [[2.6552732e-06 6.5081044e-06 5.7808645e-03 2.0178866e-02 2.9168999e-01
  6.8195605e-01 2.2530911e-04 1.5972220e-04]]
Age : (38-43), conf = 0.682
time : 0.102
Gender : Female, conf = 0.881
Age Output : [[9.3574476e-05 3.8718885e-05 6.4351452e-03 1.6516602e-02 7.8548595e-02
  8.9702237e-01 6.1631948e-04 7.2864199e-04]]
Age : (38-43), conf = 0.897
time : 0.088
Gender : Male, conf = 0.964
Age Output : [[1.0280681e-03 3.2109043e-03 9.9302687e-02 6.8336171e-01 4.2144667e-02
  1.6998777e-01 3.3662919e-04 6.2758417e-04]]
Age : (15-20), conf = 0.683
time : 0.102
Gender : Male, conf = 0.804
Age Output : [[2.2468060e-04 1.2391272e-04 1.1314816e-02 5.2637905e-02 5.0578732e-02
  8.8378847e-01 2.7988607e-04 1.0515299e-03]]
Age : (38-43), conf = 0.884
time : 0.081
Gender : Male, conf = 0.689
Age Output : [[0.00493277 0.00313733 0.06556511 0.02406845 0.05439361 0.84319645
  0.00124293 0.00346339]]
Age : (38-43), conf = 0.843
time : 0.098
Gender : Male, conf = 0.568
Age Output : [[0.02871628 0.10240839 0.4354769  0.04938547 0.04624934 0.3339502
  0.00110172 0.00271172]]
Age : (8-12), conf = 0.435
time : 0.090
Gender : Male, conf = 0.568
Age Output : [[0.02871628 0.10240839 0.4354769  0.04938547 0.04624934 0.3339502
  0.00110172 0.00271172]]
Age : (8-12), conf = 0.435
time : 0.102
Gender : Male, conf = 0.884
Age Output : [[0.00779336 0.00206548 0.00972729 0.01282562 0.03861095 0.92310023
  0.00149437 0.00438266]]
Age : (38-43), conf = 0.923
time : 0.090
Gender : Male, conf = 0.761
Age Output : [[0.00555094 0.01377395 0.2630842  0.03973324 0.05172308 0.62239856
  0.00096501 0.00277103]]
Age : (38-43), conf = 0.622
time : 0.102
Gender : Male, conf = 0.879
Age Output : [[0.04511919 0.0586962  0.28220528 0.06311104 0.100089   0.44373378
  0.00118155 0.00586396]]
Age : (38-43), conf = 0.444
time : 0.086
Gender : Male, conf = 0.986
Age Output : [[1.3630751e-03 9.4199437e-04 3.8020514e-02 4.0297866e-02 3.0796023e-02
  8.8678938e-01 3.4247106e-04 1.4485980e-03]]
Age : (38-43), conf = 0.887
time : 0.100
Gender : Male, conf = 0.951
Age Output : [[0.02475415 0.09928051 0.32170978 0.20403051 0.08403556 0.26371554
  0.00047327 0.00200063]]
Age : (8-12), conf = 0.322
time : 0.088
Gender : Male, conf = 0.952
Age Output : [[0.5963057  0.11218023 0.05652773 0.03740935 0.01792088 0.17213723
  0.00190125 0.00561759]]
Age : (0-2), conf = 0.596
time : 0.104
Gender : Male, conf = 0.993
Age Output : [[0.03299356 0.07683862 0.31924155 0.32338956 0.0428322  0.20091136
  0.00056355 0.00322965]]
Age : (15-20), conf = 0.323
time : 0.092
Gender : Male, conf = 0.951
Age Output : [[0.4340449  0.09591015 0.08268078 0.05855464 0.0271672  0.2939734
  0.0011347  0.00653419]]
Age : (0-2), conf = 0.434
time : 0.109
Gender : Male, conf = 0.951
Age Output : [[0.4340449  0.09591015 0.08268078 0.05855464 0.0271672  0.2939734
  0.0011347  0.00653419]]
Age : (0-2), conf = 0.434
time : 0.108
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.976
Age Output : [[0.45921993 0.07478537 0.10553626 0.02510148 0.02023116 0.3035214
  0.00152552 0.01007891]]
Age : (0-2), conf = 0.459
time : 0.099
Gender : Male, conf = 0.979
Age Output : [[0.22171147 0.33306104 0.28991246 0.07449998 0.00784772 0.06913539
  0.00047247 0.00335944]]
Age : (4-6), conf = 0.333
time : 0.085
Gender : Male, conf = 0.953
Age Output : [[7.88173601e-02 2.89932013e-01 4.81792182e-01 1.02156706e-01
  7.12878397e-03 3.88369150e-02 2.07161182e-04 1.12894573e-03]]
Age : (8-12), conf = 0.482
time : 0.099
Gender : Male, conf = 0.898
Age Output : [[0.56086695 0.10561757 0.1040363  0.03329887 0.01452226 0.17452928
  0.00080061 0.0063282 ]]
Age : (0-2), conf = 0.561
time : 0.083
Gender : Male, conf = 0.991
Age Output : [[3.2948413e-01 2.2308816e-01 3.4796792e-01 3.6267646e-02 6.7383009e-03
  5.3346246e-02 3.3556102e-04 2.7719305e-03]]
Age : (8-12), conf = 0.348
time : 0.085
Gender : Male, conf = 0.988
Age Output : [[0.31221193 0.17015937 0.1422057  0.14449583 0.02967668 0.19398619
  0.00087131 0.00639296]]
Age : (0-2), conf = 0.312
time : 0.100
Gender : Male, conf = 0.929
Age Output : [[0.11413499 0.0637807  0.17995307 0.11161564 0.03289115 0.48807144
  0.00131721 0.0082358 ]]
Age : (38-43), conf = 0.488
time : 0.098
Gender : Male, conf = 0.987
Age Output : [[0.6079913  0.05204305 0.0457815  0.01495667 0.01943485 0.24961416
  0.00170431 0.00847422]]
Age : (0-2), conf = 0.608
time : 0.089
Gender : Male, conf = 0.987
Age Output : [[0.6079913  0.05204305 0.0457815  0.01495667 0.01943485 0.24961416
  0.00170431 0.00847422]]
Age : (0-2), conf = 0.608
time : 0.098
Gender : Male, conf = 0.964
Age Output : [[0.6951076  0.12040551 0.06976873 0.01520136 0.00826909 0.0855759
  0.00095714 0.00471475]]
Age : (0-2), conf = 0.695
time : 0.090
Gender : Male, conf = 0.967
Age Output : [[0.4170435  0.06483618 0.10131136 0.0546477  0.03819391 0.308432
  0.00305496 0.01248045]]
Age : (0-2), conf = 0.417
time : 0.098
Gender : Male, conf = 0.954
Age Output : [[6.4363426e-01 2.3612751e-01 7.3388323e-02 1.3082616e-02 5.5206628e-03
  2.5816346e-02 4.7957263e-04 1.9507870e-03]]
Age : (0-2), conf = 0.644
time : 0.089
Gender : Male, conf = 0.980
Age Output : [[0.6674675  0.13305545 0.08713411 0.02262313 0.00723281 0.07507029
  0.00102784 0.00638883]]
Age : (0-2), conf = 0.667
time : 0.107
Gender : Male, conf = 0.964
Age Output : [[0.20730425 0.06880593 0.1865071  0.0989099  0.03248945 0.39215302
  0.00219896 0.0116314 ]]
Age : (38-43), conf = 0.392
time : 0.105
Gender : Male, conf = 0.935
Age Output : [[0.07355245 0.02713705 0.14753796 0.11804079 0.0716115  0.54675287
  0.00270989 0.01265748]]
Age : (38-43), conf = 0.547
time : 0.118
Gender : Male, conf = 0.906
Age Output : [[0.34933507 0.05725015 0.21304244 0.04387271 0.02641494 0.29914597
  0.00093649 0.0100022 ]]
Age : (0-2), conf = 0.349
time : 0.111
Gender : Male, conf = 0.896
Age Output : [[0.04711989 0.01649393 0.19347817 0.13897273 0.04415917 0.5496523
  0.0010534  0.00907043]]
Age : (38-43), conf = 0.550
time : 0.102
Gender : Male, conf = 0.951
Age Output : [[0.17948915 0.12257318 0.36724603 0.12765293 0.02201099 0.17042068
  0.00094105 0.00966597]]
Age : (8-12), conf = 0.367
time : 0.096
Gender : Male, conf = 0.951
Age Output : [[0.17948915 0.12257318 0.36724603 0.12765293 0.02201099 0.17042068
  0.00094105 0.00966597]]
Age : (8-12), conf = 0.367
time : 0.110
Gender : Male, conf = 0.904
Age Output : [[5.8732456e-01 2.1124375e-01 1.4767183e-01 1.4710989e-02 4.8098410e-03
  2.8259519e-02 3.7367726e-04 5.6058560e-03]]
Age : (0-2), conf = 0.587
time : 0.100
Gender : Male, conf = 0.868
Age Output : [[0.27248785 0.11997142 0.39378667 0.03437888 0.02239346 0.14601097
  0.00085442 0.0101163 ]]
Age : (8-12), conf = 0.394
time : 0.108
Gender : Male, conf = 0.856
Age Output : [[2.5280300e-01 2.2958614e-01 3.8396403e-01 6.2526390e-02 9.5349327e-03
  5.5688649e-02 3.1789122e-04 5.5789230e-03]]
Age : (8-12), conf = 0.384
time : 0.125
Gender : Male, conf = 0.531
Age Output : [[0.0800916  0.13466437 0.1304899  0.42660278 0.09094111 0.1313857
  0.00069002 0.00513461]]
Age : (15-20), conf = 0.427
time : 0.107
Gender : Male, conf = 0.933
Age Output : [[0.37908667 0.18402027 0.27849418 0.05847084 0.01498179 0.07702401
  0.00042585 0.00749644]]
Age : (0-2), conf = 0.379
time : 0.098
Gender : Female, conf = 0.501
Age Output : [[0.2291537  0.08468778 0.18007202 0.12304369 0.06625923 0.30208898
  0.0016113  0.01308331]]
Age : (38-43), conf = 0.302
time : 0.103
Gender : Female, conf = 0.700
Age Output : [[0.44040218 0.1409368  0.13455956 0.11949668 0.05460555 0.09605613
  0.00082871 0.01311437]]
Age : (0-2), conf = 0.440
time : 0.081
Gender : Female, conf = 0.700
Age Output : [[0.44040218 0.1409368  0.13455956 0.11949668 0.05460555 0.09605613
  0.00082871 0.01311437]]
Age : (0-2), conf = 0.440
time : 0.100
Gender : Female, conf = 0.903
Age Output : [[6.20575726e-01 2.73897707e-01 7.24153966e-02 1.38187725e-02
  2.92118895e-03 1.27050132e-02 4.95224434e-04 3.17091821e-03]]
Age : (0-2), conf = 0.621
time : 0.090
Gender : Female, conf = 0.558
Age Output : [[0.4130081  0.26613182 0.1421308  0.06152466 0.01906695 0.08897731
  0.00159126 0.00756923]]
Age : (0-2), conf = 0.413
time : 0.100
Gender : Male, conf = 0.589
Age Output : [[0.24369228 0.28552702 0.24637307 0.12442197 0.02350532 0.06985025
  0.00109167 0.00553844]]
Age : (4-6), conf = 0.286
time : 0.091
Gender : Female, conf = 0.598
Age Output : [[8.4812778e-01 1.2883887e-01 1.0387956e-02 5.7427343e-03 2.0433904e-03
  3.5415424e-03 2.2013363e-04 1.0976024e-03]]
Age : (0-2), conf = 0.848
time : 0.100
Gender : Female, conf = 0.624
Age Output : [[0.4563005  0.09619757 0.08015738 0.17457022 0.06758996 0.10552341
  0.00070076 0.01896025]]
Age : (0-2), conf = 0.456
time : 0.086
Gender : Male, conf = 0.825
Age Output : [[4.3001431e-01 2.7233687e-01 7.6003529e-02 1.4203513e-01 5.5209164e-02
  1.8801248e-02 3.7424546e-04 5.2255434e-03]]
Age : (0-2), conf = 0.430
time : 0.100
Gender : Male, conf = 0.825
Age Output : [[4.3001431e-01 2.7233687e-01 7.6003529e-02 1.4203513e-01 5.5209164e-02
  1.8801248e-02 3.7424546e-04 5.2255434e-03]]
Age : (0-2), conf = 0.430
time : 0.086
Gender : Male, conf = 0.516
Age Output : [[0.7668917  0.13486725 0.02497737 0.03226326 0.00655938 0.02397539
  0.00124011 0.00922551]]
Age : (0-2), conf = 0.767
time : 0.098
Gender : Male, conf = 0.583
Age Output : [[5.9066379e-01 3.5551548e-01 2.2517389e-02 2.3113813e-02 1.6880160e-03
  3.7560775e-03 4.3199302e-04 2.3135026e-03]]
Age : (0-2), conf = 0.591
time : 0.089
Gender : Female, conf = 0.797
Age Output : [[6.1664993e-01 3.4820944e-01 1.3382517e-02 1.5876902e-02 3.1395117e-03
  1.7937084e-03 1.6459731e-04 7.8339345e-04]]
Age : (0-2), conf = 0.617
time : 0.101
Gender : Female, conf = 0.638
Age Output : [[7.1704209e-01 2.6137763e-01 9.1056619e-03 9.0616550e-03 1.5048003e-03
  1.1787321e-03 1.4563320e-04 5.8384397e-04]]
Age : (0-2), conf = 0.717
time : 0.086
Gender : Female, conf = 0.918
Age Output : [[0.7851486  0.15646568 0.01070639 0.00578581 0.02287205 0.01209717
  0.00266584 0.00425852]]
Age : (0-2), conf = 0.785
time : 0.100
Gender : Female, conf = 0.771
Age Output : [[0.6930885  0.25226623 0.00749826 0.02220863 0.01823409 0.00426537
  0.00076232 0.00167666]]
Age : (0-2), conf = 0.693
time : 0.085
Gender : Female, conf = 0.717
Age Output : [[7.7416021e-01 1.6465349e-01 8.1329802e-03 3.0648729e-02 1.4592500e-02
  5.0557535e-03 5.7882856e-04 2.1775342e-03]]
Age : (0-2), conf = 0.774
time : 0.101
Gender : Female, conf = 0.895
Age Output : [[0.4344624  0.09656473 0.01896817 0.04626464 0.35326234 0.03413676
  0.00323158 0.01310929]]
Age : (0-2), conf = 0.434
time : 0.105
Gender : Female, conf = 0.894
Age Output : [[0.79232466 0.15561628 0.01017793 0.01774985 0.01038132 0.00843406
  0.00106306 0.00425278]]
Age : (0-2), conf = 0.792
time : 0.102
Gender : Female, conf = 0.639
Age Output : [[0.2972776  0.11041084 0.02246235 0.22901812 0.28357923 0.04573044
  0.00289007 0.00863136]]
Age : (0-2), conf = 0.297
time : 0.078
Gender : Female, conf = 0.865
Age Output : [[0.5152154  0.2595944  0.02962839 0.11059026 0.05676955 0.01932835
  0.00197641 0.00689724]]
Age : (0-2), conf = 0.515
time : 0.092
Gender : Female, conf = 0.882
Age Output : [[0.61774915 0.14149383 0.03724284 0.06703728 0.10126285 0.02317926
  0.00200107 0.0100337 ]]
Age : (0-2), conf = 0.618
time : 0.081
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Female, conf = 0.812
Age Output : [[0.43497318 0.16849452 0.01390138 0.12397978 0.2280215  0.0238029
  0.00215045 0.00467634]]
Age : (0-2), conf = 0.435
time : 0.100
Gender : Female, conf = 0.905
Age Output : [[0.6672558  0.17646138 0.01212287 0.02242149 0.10525772 0.01187485
  0.00192099 0.00268491]]
Age : (0-2), conf = 0.667
time : 0.085
Gender : Female, conf = 0.761
Age Output : [[8.2963318e-01 1.3133025e-01 9.0281675e-03 8.8851871e-03 1.4306927e-02
  4.5818016e-03 5.1013677e-04 1.7242067e-03]]
Age : (0-2), conf = 0.830
time : 0.099
Gender : Female, conf = 0.921
Age Output : [[0.06525592 0.05421891 0.04788255 0.09320135 0.69944936 0.03432041
  0.00181042 0.0038611 ]]
Age : (25-32), conf = 0.699
time : 0.080
Gender : Female, conf = 0.703
Age Output : [[0.64176697 0.23853539 0.02668085 0.04554068 0.02882621 0.0093458
  0.00137077 0.00793331]]
Age : (0-2), conf = 0.642
time : 0.100
Gender : Female, conf = 0.894
Age Output : [[0.36309388 0.19786929 0.0473186  0.22695401 0.13846128 0.02143974
  0.00098643 0.00387669]]
Age : (0-2), conf = 0.363
time : 0.089
Gender : Female, conf = 0.715
Age Output : [[8.3973926e-01 1.2920940e-01 9.4525823e-03 9.4119906e-03 5.7389447e-03
  4.2712577e-03 4.3349812e-04 1.7432087e-03]]
Age : (0-2), conf = 0.840
time : 0.103
Gender : Female, conf = 0.837
Age Output : [[0.15086338 0.11236062 0.04446692 0.47218722 0.13689284 0.07459576
  0.00259273 0.00604057]]
Age : (15-20), conf = 0.472
time : 0.085
Gender : Male, conf = 0.575
Age Output : [[0.6685326  0.21066537 0.0227724  0.0625539  0.02199865 0.01034341
  0.00067141 0.00246229]]
Age : (0-2), conf = 0.669
time : 0.085
Gender : Male, conf = 0.834
Age Output : [[0.36483467 0.44207448 0.02501014 0.1345742  0.02522613 0.00555848
  0.00076302 0.00195889]]
Age : (4-6), conf = 0.442
time : 0.104
Gender : Male, conf = 0.549
Age Output : [[0.29140607 0.36524034 0.06186499 0.1133084  0.15528393 0.00727679
  0.00250317 0.00311636]]
Age : (4-6), conf = 0.365
time : 0.084
Gender : Female, conf = 0.787
Age Output : [[0.13507056 0.21434258 0.1157771  0.13729915 0.37584177 0.01388047
  0.00410871 0.00367967]]
Age : (25-32), conf = 0.376
time : 0.084
Gender : Male, conf = 0.680
Age Output : [[0.44380885 0.22199075 0.04979362 0.02743356 0.23669125 0.01120294
  0.00376358 0.0053154 ]]
Age : (0-2), conf = 0.444
time : 0.100
Gender : Male, conf = 0.787
Age Output : [[8.4376985e-01 1.0011260e-01 1.2235547e-02 1.7560943e-03 3.8608126e-02
  1.8643482e-03 5.3422700e-04 1.1191089e-03]]
Age : (0-2), conf = 0.844
time : 0.088
Gender : Male, conf = 0.787
Age Output : [[8.4376985e-01 1.0011260e-01 1.2235547e-02 1.7560943e-03 3.8608126e-02
  1.8643482e-03 5.3422700e-04 1.1191089e-03]]
Age : (0-2), conf = 0.844
time : 0.099
No face Detected, Checking next frame
Gender : Male, conf = 0.878
Age Output : [[8.7764913e-01 6.8490565e-02 8.1841936e-03 3.3717940e-03 3.7529714e-02
  2.6331858e-03 6.4070808e-04 1.5005872e-03]]
Age : (0-2), conf = 0.878
time : 0.083
Gender : Male, conf = 0.924
Age Output : [[0.31298193 0.03981748 0.02266568 0.03244641 0.54906    0.02735381
  0.00331213 0.01236256]]
Age : (25-32), conf = 0.549
time : 0.085
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.901
Age Output : [[0.6255554  0.04519663 0.01407008 0.0075607  0.26710573 0.01879765
  0.00575685 0.01595696]]
Age : (0-2), conf = 0.626
time : 0.084
Gender : Male, conf = 0.901
Age Output : [[0.6255554  0.04519663 0.01407008 0.0075607  0.26710573 0.01879765
  0.00575685 0.01595696]]
Age : (0-2), conf = 0.626
time : 0.084
Gender : Male, conf = 0.518
Age Output : [[0.58541214 0.09759979 0.01031632 0.00741039 0.2799234  0.01264771
  0.00353036 0.00315989]]
Age : (0-2), conf = 0.585
time : 0.101
Gender : Male, conf = 0.809
Age Output : [[0.80103254 0.06216241 0.00630614 0.00556538 0.10565993 0.01061161
  0.00368949 0.00497257]]
Age : (0-2), conf = 0.801
time : 0.085
Gender : Male, conf = 0.745
Age Output : [[0.03895767 0.00358622 0.00104223 0.00271204 0.91856396 0.02908317
  0.00294325 0.0031115 ]]
Age : (25-32), conf = 0.919
time : 0.098
Gender : Male, conf = 0.941
Age Output : [[0.47919843 0.08872484 0.01566451 0.00893985 0.35406733 0.03964605
  0.0068042  0.00695486]]
Age : (0-2), conf = 0.479
time : 0.090
Gender : Male, conf = 0.984
Age Output : [[0.10428306 0.02213786 0.00911695 0.0105244  0.8199495  0.02603217
  0.00389487 0.00406112]]
Age : (25-32), conf = 0.820
time : 0.128
Gender : Male, conf = 0.961
Age Output : [[0.37968886 0.09260057 0.01657134 0.02524969 0.44782203 0.03039749
  0.00272295 0.00494701]]
Age : (25-32), conf = 0.448
time : 0.123
Gender : Male, conf = 0.994
Age Output : [[0.64472765 0.09052876 0.01542523 0.01079301 0.19354542 0.03241265
  0.00404392 0.00852337]]
Age : (0-2), conf = 0.645
time : 0.116
Gender : Male, conf = 0.992
Age Output : [[0.30303076 0.17209221 0.0390472  0.03149692 0.41563228 0.03124906
  0.00264078 0.00481085]]
Age : (25-32), conf = 0.416
time : 0.116
Gender : Male, conf = 0.970
Age Output : [[0.18070225 0.07115193 0.01455971 0.02497563 0.66646355 0.03489025
  0.00306305 0.00419364]]
Age : (25-32), conf = 0.666
time : 0.122
Gender : Male, conf = 0.896
Age Output : [[0.22947681 0.04779561 0.01111889 0.01904565 0.6045079  0.07433628
  0.00531277 0.00840608]]
Age : (25-32), conf = 0.605
time : 0.116
Gender : Male, conf = 0.975
Age Output : [[0.6897753  0.1246358  0.01387425 0.01219339 0.13853885 0.01232861
  0.00286656 0.00578733]]
Age : (0-2), conf = 0.690
time : 0.113
Gender : Male, conf = 0.954
Age Output : [[0.22155373 0.072698   0.01723748 0.037544   0.5929924  0.04076378
  0.00661476 0.01059585]]
Age : (25-32), conf = 0.593
time : 0.124
Gender : Male, conf = 0.736
Age Output : [[0.56260353 0.0299076  0.00488434 0.00372957 0.35458285 0.03040481
  0.00594424 0.00794298]]
Age : (0-2), conf = 0.563
time : 0.114
Gender : Male, conf = 0.892
Age Output : [[0.67344373 0.08170623 0.01067585 0.00923874 0.19410057 0.02153683
  0.00361066 0.00568748]]
Age : (0-2), conf = 0.673
time : 0.118
Gender : Male, conf = 0.691
Age Output : [[0.5507541  0.03795165 0.00460915 0.0051158  0.37411582 0.02028554
  0.00239192 0.00477598]]
Age : (0-2), conf = 0.551
time : 0.122
Gender : Male, conf = 0.891
Age Output : [[0.3669043  0.05357154 0.01074039 0.01546981 0.5075579  0.03563201
  0.0037336  0.00639044]]
Age : (25-32), conf = 0.508
time : 0.116
Gender : Male, conf = 0.787
Age Output : [[0.5961497  0.04391164 0.00662771 0.00677694 0.3254419  0.01593595
  0.00166269 0.00349346]]
Age : (0-2), conf = 0.596
time : 0.115
Gender : Male, conf = 0.815
Age Output : [[0.496042   0.04388862 0.00617848 0.00609542 0.41915795 0.01913808
  0.00362996 0.00586958]]
Age : (0-2), conf = 0.496
time : 0.116
Gender : Male, conf = 0.919
Age Output : [[0.52664727 0.03204378 0.00537499 0.00618214 0.391923   0.0259196
  0.00454536 0.00736379]]
Age : (0-2), conf = 0.527
time : 0.132
Gender : Male, conf = 0.839
Age Output : [[0.51350075 0.04231054 0.00405635 0.00399939 0.41893867 0.01175436
  0.00221732 0.00322263]]
Age : (0-2), conf = 0.514
time : 0.106
Gender : Male, conf = 0.714
Age Output : [[0.16605198 0.01497782 0.00292125 0.00378678 0.7810926  0.02388693
  0.00254076 0.0047418 ]]
Age : (25-32), conf = 0.781
time : 0.116
Gender : Male, conf = 0.756
Age Output : [[0.7095787  0.09413038 0.0085952  0.00720267 0.16301401 0.01260098
  0.0019937  0.00288436]]
Age : (0-2), conf = 0.710
time : 0.115
Gender : Male, conf = 0.614
Age Output : [[0.83732337 0.04382266 0.00238236 0.00223982 0.10859051 0.00328848
  0.00103785 0.00131499]]
Age : (0-2), conf = 0.837
time : 0.116
Gender : Male, conf = 0.847
Age Output : [[0.7295602  0.06865221 0.00435194 0.00311553 0.18052681 0.00857351
  0.00245422 0.00276554]]
Age : (0-2), conf = 0.730
time : 0.113
Gender : Female, conf = 0.516
Age Output : [[0.78485936 0.03876564 0.00355589 0.0034199  0.15802282 0.00663626
  0.00148304 0.00325704]]
Age : (0-2), conf = 0.785
time : 0.103
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Female, conf = 0.657
Age Output : [[0.24558656 0.01277135 0.00281812 0.00356821 0.70733064 0.02008495
  0.00213769 0.00570251]]
Age : (25-32), conf = 0.707
time : 0.095
Gender : Male, conf = 0.915
Age Output : [[0.56686175 0.037204   0.00531787 0.00539291 0.36383966 0.01587191
  0.00178494 0.00372695]]
Age : (0-2), conf = 0.567
time : 0.091
Gender : Male, conf = 0.962
Age Output : [[9.0662074e-01 3.6666766e-02 2.1927617e-03 1.3735078e-03 4.8426773e-02
  2.6120939e-03 8.2713802e-04 1.2802195e-03]]
Age : (0-2), conf = 0.907
time : 0.101
Gender : Male, conf = 0.889
Age Output : [[0.8774955  0.02419322 0.00326436 0.00162577 0.08271281 0.00638228
  0.00160927 0.00271685]]
Age : (0-2), conf = 0.877
time : 0.089
Gender : Male, conf = 0.964
Age Output : [[0.3539249  0.04398105 0.00707301 0.00908584 0.55973566 0.01876995
  0.00270789 0.00472177]]
Age : (25-32), conf = 0.560
time : 0.125
Gender : Female, conf = 0.972
Age Output : [[9.1186726e-01 6.6797346e-02 1.6393553e-03 2.6812889e-03 1.5973408e-02
  6.5724197e-04 1.4573056e-04 2.3841609e-04]]
Age : (0-2), conf = 0.912
time : 0.112
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.855
Age Output : [[1.37495637e-09 1.21146435e-08 5.48359480e-07 5.82697567e-06
  9.99956489e-01 3.57253048e-05 1.02000649e-06 1.79097242e-07]]
Age : (25-32), conf = 1.000
time : 0.110
Gender : Male, conf = 0.953
Age Output : [[3.6044401e-08 4.7934327e-07 1.7876238e-05 6.4663756e-05 9.9928039e-01
  6.1860762e-04 1.6473859e-05 1.5046248e-06]]
Age : (25-32), conf = 0.999
time : 0.105
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.765
Age Output : [[1.4692029e-03 7.4492084e-05 5.8891549e-04 7.9070270e-04 2.8539822e-02
  9.5557284e-01 2.7654320e-03 1.0198490e-02]]
Age : (38-43), conf = 0.956
time : 0.102
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.837
Age Output : [[8.6911279e-01 1.2850228e-01 4.7460222e-04 2.4951269e-05 1.8197276e-03
  3.0705811e-05 2.1550219e-05 1.3337671e-05]]
Age : (0-2), conf = 0.869
time : 0.091
Gender : Male, conf = 0.540
Age Output : [[1.16111204e-01 8.64533663e-01 1.19790910e-02 1.60823707e-04
  7.01399753e-03 9.73069182e-05 5.04016389e-05 5.35582039e-05]]
Age : (4-6), conf = 0.865
time : 0.146
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.994
Age Output : [[9.7920632e-01 1.9202465e-02 4.6672631e-04 1.6070342e-04 4.3816603e-04
  2.8826675e-04 6.5698172e-05 1.7142259e-04]]
Age : (0-2), conf = 0.979
time : 0.153
No face Detected, Checking next frame
Gender : Male, conf = 0.566
Age Output : [[0.7936078  0.1322704  0.00831147 0.01615397 0.02836165 0.01594998
  0.00214861 0.00319614]]
Age : (0-2), conf = 0.794
time : 0.159
Gender : Male, conf = 0.659
Age Output : [[0.5217234  0.08244461 0.01272754 0.03255507 0.26418272 0.0750256
  0.00576886 0.00557216]]
Age : (0-2), conf = 0.522
time : 0.178
Gender : Male, conf = 0.992
Age Output : [[8.1147587e-01 1.0020998e-01 7.0015355e-03 1.6992159e-02 5.5262633e-02
  7.0735393e-03 7.3963188e-04 1.2445810e-03]]
Age : (0-2), conf = 0.811
time : 0.161
Gender : Male, conf = 0.974
Age Output : [[8.9435816e-01 8.5065477e-02 2.6022666e-03 2.6463638e-03 1.2678001e-02
  1.7345200e-03 5.4191914e-04 3.7337752e-04]]
Age : (0-2), conf = 0.894
time : 0.161
Gender : Male, conf = 0.993
Age Output : [[0.5263005  0.13397591 0.01979427 0.02327435 0.2638189  0.02700398
  0.00285467 0.00297741]]
Age : (0-2), conf = 0.526
time : 0.135
Gender : Male, conf = 0.996
Age Output : [[0.07760339 0.0412076  0.01027275 0.03472171 0.7832981  0.04494713
  0.00445812 0.00349118]]
Age : (25-32), conf = 0.783
time : 0.139
Gender : Male, conf = 0.997
Age Output : [[0.48591903 0.12494896 0.01420678 0.02398234 0.3088281  0.03417081
  0.00432072 0.00362331]]
Age : (0-2), conf = 0.486
time : 0.173
Gender : Male, conf = 0.976
Age Output : [[0.06976434 0.02241356 0.01208086 0.03460377 0.7571013  0.09500828
  0.00423407 0.00479379]]
Age : (25-32), conf = 0.757
time : 0.131
Gender : Male, conf = 0.993
Age Output : [[5.8412412e-03 5.2114665e-03 9.7288778e-03 1.7037349e-02 9.4147116e-01
  1.8745581e-02 1.2432855e-03 7.2100852e-04]]
Age : (25-32), conf = 0.941
Gender : Male, conf = 0.846
Age Output : [[0.00159283 0.00806486 0.01112436 0.00686683 0.7135542  0.24195887
  0.013451   0.003387  ]]
Age : (25-32), conf = 0.714
time : 0.185
Gender : Male, conf = 0.989
Age Output : [[4.65747356e-01 4.55465049e-01 1.33698955e-02 6.72650896e-03
  5.69002777e-02 1.38359889e-03 2.24180301e-04 1.83144773e-04]]
Age : (0-2), conf = 0.466
time : 0.136
Gender : Male, conf = 0.996
Age Output : [[8.2900459e-01 1.3915417e-01 1.7104645e-03 8.3842390e-04 2.8636960e-02
  4.1888541e-04 1.4819166e-04 8.8238063e-05]]
Age : (0-2), conf = 0.829
Gender : Male, conf = 0.941
Age Output : [[0.00417042 0.01318403 0.00462424 0.28439695 0.17726256 0.5036471
  0.00519241 0.00752235]]
Age : (38-43), conf = 0.504
time : 0.160
Gender : Male, conf = 0.968
Age Output : [[7.6615179e-01 4.8805013e-02 3.3718308e-03 3.4258361e-03 1.7328691e-01
  3.9002111e-03 4.6904516e-04 5.8934267e-04]]
Age : (0-2), conf = 0.766
time : 0.104
Gender : Male, conf = 0.996
Age Output : [[2.6318999e-03 4.0818434e-03 1.3959598e-03 3.8724591e-03 9.8463523e-01
  3.0218784e-03 1.8506827e-04 1.7561123e-04]]
Age : (25-32), conf = 0.985
time : 0.112
Gender : Male, conf = 0.989
Age Output : [[1.9153044e-02 8.8491850e-03 1.9127250e-03 7.1650515e-03 9.5490444e-01
  7.0163254e-03 4.4087047e-04 5.5833306e-04]]
Age : (25-32), conf = 0.955
time : 0.122
Gender : Male, conf = 0.991
Age Output : [[0.04803361 0.02171869 0.00291129 0.01047736 0.9034235  0.0113295
  0.00104964 0.00105652]]
Age : (25-32), conf = 0.903
time : 0.101
Gender : Male, conf = 0.981
Age Output : [[0.05823662 0.02198511 0.00367237 0.01360081 0.87769914 0.02090983
  0.00178247 0.00211361]]
Age : (25-32), conf = 0.878
Gender : Male, conf = 0.930
Age Output : [[0.00157789 0.00184104 0.00397881 0.08365192 0.28109205 0.62297547
  0.00201417 0.00286865]]
Age : (38-43), conf = 0.623
time : 0.160
Gender : Male, conf = 0.927
Age Output : [[0.03461922 0.01281233 0.00272835 0.01165355 0.92255795 0.01252925
  0.0013724  0.00172686]]
Age : (25-32), conf = 0.923
Gender : Male, conf = 0.857
Age Output : [[0.00204131 0.00200547 0.00279224 0.07562701 0.33767155 0.5729174
  0.00255741 0.00438766]]
Age : (38-43), conf = 0.573
time : 0.194
Gender : Male, conf = 0.964
Age Output : [[5.0292868e-04 5.4276403e-04 1.1663871e-03 5.5132978e-02 5.6286389e-01
  3.7582263e-01 1.6392361e-03 2.3291630e-03]]
Age : (25-32), conf = 0.563
time : 0.132
Gender : Male, conf = 0.932
Age Output : [[2.3033457e-04 2.8568375e-04 6.7435391e-04 3.7937600e-02 5.0784838e-01
  4.4933030e-01 1.4667015e-03 2.2266703e-03]]
Age : (25-32), conf = 0.508
time : 0.140
Gender : Male, conf = 0.975
Age Output : [[0.03144338 0.01457132 0.00762031 0.05024424 0.38480705 0.49442428
  0.009522   0.00736732]]
Age : (38-43), conf = 0.494
time : 0.133
Gender : Male, conf = 0.966
Age Output : [[0.05074973 0.01920797 0.00849797 0.04548613 0.37717578 0.47344106
  0.01521063 0.01023071]]
Age : (38-43), conf = 0.473
time : 0.110
Gender : Male, conf = 0.980
Age Output : [[0.02272418 0.008737   0.00772187 0.04023284 0.18420811 0.72651136
  0.00387926 0.00598539]]
Age : (38-43), conf = 0.727
time : 0.117
Gender : Male, conf = 0.972
Age Output : [[0.11303672 0.02718358 0.01279294 0.04913173 0.25917083 0.5178047
  0.01056319 0.01031636]]
Age : (38-43), conf = 0.518
time : 0.108
Gender : Male, conf = 0.960
Age Output : [[0.04260722 0.01794805 0.01008292 0.04596464 0.26682997 0.6012099
  0.00797846 0.00737889]]
Age : (38-43), conf = 0.601
time : 0.100
Gender : Male, conf = 0.960
Age Output : [[0.04260722 0.01794805 0.01008292 0.04596464 0.26682997 0.6012099
  0.00797846 0.00737889]]
Age : (38-43), conf = 0.601
time : 0.100
Gender : Male, conf = 0.957
Age Output : [[0.07056287 0.02524928 0.01521427 0.05234375 0.20799227 0.60819393
  0.0105658  0.00987788]]
Age : (38-43), conf = 0.608
time : 0.100
Gender : Male, conf = 0.963
Age Output : [[0.12956378 0.0357285  0.01537575 0.04503781 0.1720508  0.57041675
  0.01747245 0.01435408]]
Age : (38-43), conf = 0.570
time : 0.106
Gender : Male, conf = 0.962
Age Output : [[0.09853453 0.04541266 0.01906754 0.06023366 0.17481662 0.5778748
  0.01220305 0.01185722]]
Age : (38-43), conf = 0.578
time : 0.097
Gender : Male, conf = 0.958
Age Output : [[0.06725898 0.03636106 0.02431382 0.11573831 0.11698464 0.6215893
  0.00720675 0.01054714]]
Age : (38-43), conf = 0.622
time : 0.094
Gender : Male, conf = 0.955
Age Output : [[0.07531761 0.02939059 0.01920247 0.06529728 0.14161283 0.63967884
  0.01334633 0.01615404]]
Age : (38-43), conf = 0.640
time : 0.100
Gender : Male, conf = 0.839
Age Output : [[0.21499696 0.03947074 0.01763915 0.0368262  0.15197639 0.5158172
  0.01163319 0.01164014]]
Age : (38-43), conf = 0.516
time : 0.090
Gender : Male, conf = 0.965
Age Output : [[0.12742071 0.05642245 0.02674515 0.07708198 0.13343717 0.5607667
  0.00883105 0.00929483]]
Age : (38-43), conf = 0.561
time : 0.109
Gender : Male, conf = 0.947
Age Output : [[0.05678042 0.01993879 0.01385622 0.05447748 0.15196443 0.67514247
  0.01274287 0.01509738]]
Age : (38-43), conf = 0.675
time : 0.091
Gender : Male, conf = 0.945
Age Output : [[0.06481904 0.02738461 0.01626887 0.06112056 0.14831544 0.66119796
  0.01065863 0.01023489]]
Age : (38-43), conf = 0.661
time : 0.101
Gender : Male, conf = 0.945
Age Output : [[0.06481904 0.02738461 0.01626887 0.06112056 0.14831544 0.66119796
  0.01065863 0.01023489]]
Age : (38-43), conf = 0.661
time : 0.085
Gender : Male, conf = 0.933
Age Output : [[0.17257883 0.08004396 0.03250029 0.09214727 0.10451695 0.48621297
  0.01486494 0.01713484]]
Age : (38-43), conf = 0.486
time : 0.102
Gender : Male, conf = 0.932
Age Output : [[0.05215583 0.03298028 0.02657592 0.11820676 0.07335169 0.6780838
  0.0070074  0.01163837]]
Age : (38-43), conf = 0.678
time : 0.105
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.953
Age Output : [[0.11274538 0.03716625 0.02443405 0.05299933 0.07806689 0.67316103
  0.00808586 0.01334122]]
Age : (38-43), conf = 0.673
time : 0.107
Gender : Male, conf = 0.884
Age Output : [[0.18135585 0.06922532 0.0323281  0.09704067 0.12154193 0.4658148
  0.01339803 0.01929534]]
Age : (38-43), conf = 0.466
time : 0.093
Gender : Male, conf = 0.919
Age Output : [[0.12902737 0.03377737 0.02015672 0.05860363 0.12290389 0.60308677
  0.01132082 0.0211235 ]]
Age : (38-43), conf = 0.603
time : 0.099
Gender : Male, conf = 0.850
Age Output : [[0.02448028 0.01225597 0.01242525 0.0646107  0.23470184 0.6233852
  0.01086294 0.01727786]]
Age : (38-43), conf = 0.623
time : 0.090
Gender : Male, conf = 0.907
Age Output : [[0.02284038 0.00796569 0.00947528 0.03500735 0.1776466  0.7187868
  0.01080926 0.01746862]]
Age : (38-43), conf = 0.719
time : 0.100
Gender : Male, conf = 0.949
Age Output : [[0.0355207  0.0057227  0.00730177 0.01420065 0.0719585  0.8457017
  0.00521468 0.01437928]]
Age : (38-43), conf = 0.846
time : 0.091
Gender : Male, conf = 0.945
Age Output : [[0.07700439 0.03358356 0.01169592 0.07345196 0.2613542  0.5098197
  0.01911683 0.01397351]]
Age : (38-43), conf = 0.510
time : 0.099
Gender : Male, conf = 0.945
Age Output : [[0.07700439 0.03358356 0.01169592 0.07345196 0.2613542  0.5098197
  0.01911683 0.01397351]]
Age : (38-43), conf = 0.510
time : 0.082
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.753
Age Output : [[2.6501743e-07 1.0693507e-07 1.0887906e-05 1.7530094e-04 7.2037768e-01
  2.7904043e-01 2.6463912e-04 1.3068038e-04]]
Age : (25-32), conf = 0.720
time : 0.095
Gender : Male, conf = 0.980
Age Output : [[2.8835493e-07 1.8950095e-07 1.3117470e-04 7.8791712e-04 9.0688848e-01
  9.1790371e-02 1.6872653e-04 2.3280438e-04]]
Age : (25-32), conf = 0.907
time : 0.104
Gender : Male, conf = 0.948
Age Output : [[1.0534000e-05 5.4579564e-06 2.6042221e-04 1.5618337e-03 7.9957724e-01
  1.9774398e-01 4.1399707e-04 4.2652592e-04]]
Age : (25-32), conf = 0.800
time : 0.091
Gender : Female, conf = 0.571
Age Output : [[2.2039815e-07 1.9498131e-07 6.6967237e-05 5.2598468e-04 9.5426959e-01
  4.4981260e-02 9.5097341e-05 6.0621027e-05]]
Age : (25-32), conf = 0.954
time : 0.093
Gender : Male, conf = 0.994
Age Output : [[7.6341976e-06 2.6184957e-06 9.2545619e-05 5.0634000e-04 7.2556949e-01
  2.7226406e-01 1.0713389e-03 4.8600533e-04]]
Age : (25-32), conf = 0.726
time : 0.105
Gender : Male, conf = 0.857
Age Output : [[5.0005667e-08 1.1662736e-07 3.3614397e-05 2.1348412e-04 9.8588806e-01
  1.3786109e-02 4.6738682e-05 3.1780615e-05]]
Age : (25-32), conf = 0.986
time : 0.098
Gender : Male, conf = 0.997
Age Output : [[5.3428784e-07 4.8453359e-07 4.2283911e-05 7.2145020e-04 8.6899078e-01
  1.3002129e-01 1.1790005e-04 1.0538500e-04]]
Age : (25-32), conf = 0.869
time : 0.082
Gender : Male, conf = 0.968
Age Output : [[2.3478444e-06 1.9528445e-06 7.6772179e-05 1.8374297e-03 7.5638199e-01
  2.4117149e-01 2.0992341e-04 3.1811307e-04]]
Age : (25-32), conf = 0.756
time : 0.100
Gender : Male, conf = 0.992
Age Output : [[4.7896046e-05 5.6195277e-05 3.0722788e-03 7.2412677e-03 6.8569797e-01
  3.0310160e-01 2.1219264e-04 5.7052757e-04]]
Age : (25-32), conf = 0.686
time : 0.084
Gender : Male, conf = 0.940
Age Output : [[5.5287842e-06 7.1543409e-06 3.1771901e-04 3.9610220e-03 6.6223198e-01
  3.3300325e-01 1.6986894e-04 3.0345641e-04]]
Age : (25-32), conf = 0.662
time : 0.102
Gender : Male, conf = 0.995
Age Output : [[2.2503686e-04 2.8227488e-04 4.0292940e-03 1.0808708e-02 6.9148231e-01
  2.9202807e-01 3.5212326e-04 7.9224631e-04]]
Age : (25-32), conf = 0.691
time : 0.099
Gender : Male, conf = 0.995
Age Output : [[2.2503686e-04 2.8227488e-04 4.0292940e-03 1.0808708e-02 6.9148231e-01
  2.9202807e-01 3.5212326e-04 7.9224631e-04]]
Age : (25-32), conf = 0.691
time : 0.106
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.966
Age Output : [[0.4586748  0.1780952  0.0157974  0.02021839 0.28992376 0.02539371
  0.00213024 0.00976649]]
Age : (0-2), conf = 0.459
time : 0.084
Gender : Female, conf = 0.966
Age Output : [[0.4586748  0.1780952  0.0157974  0.02021839 0.28992376 0.02539371
  0.00213024 0.00976649]]
Age : (0-2), conf = 0.459
time : 0.084
Gender : Male, conf = 0.817
Age Output : [[0.0135605  0.02614926 0.02403481 0.03162637 0.7622137  0.12735392
  0.00216087 0.01290052]]
Age : (25-32), conf = 0.762
time : 0.085
Gender : Male, conf = 0.819
Age Output : [[2.0542737e-02 6.4267330e-02 3.7971336e-02 4.0474270e-02 7.3310781e-01
  9.2796236e-02 5.2215048e-04 1.0318047e-02]]
Age : (25-32), conf = 0.733
time : 0.099
Gender : Male, conf = 0.887
Age Output : [[1.9469502e-04 9.8912865e-03 1.2696554e-01 7.2119430e-02 6.9150144e-01
  9.7299814e-02 3.4055088e-04 1.6872309e-03]]
Age : (25-32), conf = 0.692
time : 0.083
Gender : Male, conf = 0.960
Age Output : [[0.00163269 0.13613504 0.4866053  0.07710009 0.19933324 0.09589417
  0.0006055  0.0026939 ]]
Age : (8-12), conf = 0.487
time : 0.102
Gender : Male, conf = 0.906
Age Output : [[0.0061966  0.0652142  0.17864385 0.12973876 0.42399988 0.18651275
  0.00153725 0.00815674]]
Age : (25-32), conf = 0.424
time : 0.083
Gender : Male, conf = 0.987
Age Output : [[0.02063891 0.3112851  0.13501418 0.22647797 0.20770621 0.09362041
  0.00074228 0.00451484]]
Age : (4-6), conf = 0.311
time : 0.099
Gender : Male, conf = 0.987
Age Output : [[0.02063891 0.3112851  0.13501418 0.22647797 0.20770621 0.09362041
  0.00074228 0.00451484]]
Age : (4-6), conf = 0.311
time : 0.086
Gender : Male, conf = 0.949
Age Output : [[2.3608499e-03 2.2370899e-02 4.0865224e-02 1.1223628e-01 5.5827332e-01
  2.5995567e-01 4.0149418e-04 3.5363019e-03]]
Age : (25-32), conf = 0.558
time : 0.102
Gender : Male, conf = 0.909
Age Output : [[0.01144943 0.10797857 0.11024889 0.2616091  0.27118364 0.2313757
  0.00059904 0.00555562]]
Age : (25-32), conf = 0.271
time : 0.084
Gender : Male, conf = 0.980
Age Output : [[1.4028599e-02 2.2653337e-01 5.5818025e-02 5.2651167e-01 1.0587704e-01
  6.9295429e-02 2.5611464e-04 1.6797361e-03]]
Age : (15-20), conf = 0.527
time : 0.103
Gender : Male, conf = 0.891
Age Output : [[0.02300209 0.05485276 0.03987646 0.280306   0.4221696  0.17552818
  0.00046782 0.00379703]]
Age : (25-32), conf = 0.422
time : 0.089
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.931
Age Output : [[0.00750746 0.02453334 0.02738231 0.38868424 0.2275909  0.32056323
  0.00055156 0.00318699]]
Age : (15-20), conf = 0.389
time : 0.100
Gender : Male, conf = 0.766
Age Output : [[1.16136819e-02 9.98029709e-02 6.72217831e-02 4.51384991e-01
  1.00836195e-01 2.66441107e-01 2.41101865e-04 2.45823199e-03]]
Age : (15-20), conf = 0.451
time : 0.085
Gender : Male, conf = 0.973
Age Output : [[0.07722842 0.31046173 0.04789867 0.15659142 0.0736863  0.32862025
  0.00154252 0.00397066]]
Age : (38-43), conf = 0.329
time : 0.098
Gender : Male, conf = 0.973
Age Output : [[0.07722842 0.31046173 0.04789867 0.15659142 0.0736863  0.32862025
  0.00154252 0.00397066]]
Age : (38-43), conf = 0.329
time : 0.094
Gender : Male, conf = 0.974
Age Output : [[0.01259828 0.11616476 0.07887568 0.17332679 0.17377841 0.43687084
  0.00083668 0.0075486 ]]
Age : (38-43), conf = 0.437
time : 0.098
Gender : Male, conf = 0.896
Age Output : [[6.9706589e-03 6.8087548e-01 1.5080941e-01 1.0663795e-01 2.1102382e-02
  3.2700874e-02 1.3097259e-04 7.7229593e-04]]
Age : (4-6), conf = 0.681
time : 0.092
Gender : Male, conf = 0.818
Age Output : [[3.8917188e-03 2.3066728e-01 2.8989184e-01 3.1743357e-01 5.7320271e-02
  9.8357208e-02 2.1358156e-04 2.2245087e-03]]
Age : (15-20), conf = 0.317
time : 0.101
Gender : Male, conf = 0.931
Age Output : [[3.6938072e-03 2.0620233e-01 2.2233464e-01 3.6580390e-01 5.2218452e-02
  1.4807795e-01 1.8162047e-04 1.4873347e-03]]
Age : (15-20), conf = 0.366
time : 0.083
Gender : Male, conf = 0.817
Age Output : [[7.9356479e-03 2.9761624e-01 1.6118437e-01 3.9106068e-01 4.2478804e-02
  9.7179703e-02 2.4272050e-04 2.3017200e-03]]
Age : (15-20), conf = 0.391
time : 0.098
Gender : Male, conf = 0.760
Age Output : [[0.01625248 0.23677468 0.09281188 0.3820639  0.06484985 0.20122597
  0.00070125 0.00531997]]
Age : (15-20), conf = 0.382
time : 0.090
Gender : Male, conf = 0.743
Age Output : [[3.58746643e-03 1.21538695e-02 1.95905995e-02 1.97621793e-01
  8.47135782e-02 6.78154826e-01 6.62806211e-04 3.51501838e-03]]
Age : (38-43), conf = 0.678
time : 0.108
Gender : Male, conf = 0.743
Age Output : [[3.58746643e-03 1.21538695e-02 1.95905995e-02 1.97621793e-01
  8.47135782e-02 6.78154826e-01 6.62806211e-04 3.51501838e-03]]
Age : (38-43), conf = 0.678
time : 0.090
Gender : Male, conf = 0.895
Age Output : [[1.6147060e-03 1.6797466e-02 2.0882877e-02 5.6710410e-01 1.4069419e-01
  2.5048152e-01 3.4459541e-04 2.0805509e-03]]
Age : (15-20), conf = 0.567
time : 0.100
Gender : Male, conf = 0.829
Age Output : [[2.8527508e-04 1.5040076e-03 1.1298882e-02 2.8351974e-01 5.7865971e-01
  1.2331054e-01 1.9212595e-04 1.2296452e-03]]
Age : (25-32), conf = 0.579
time : 0.086
Gender : Male, conf = 0.684
Age Output : [[1.2670220e-03 2.4378283e-02 5.0474696e-02 2.8447118e-01 4.3665758e-01
  2.0096360e-01 1.6879011e-04 1.6188172e-03]]
Age : (25-32), conf = 0.437
time : 0.103
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.998
Age Output : [[6.4506882e-01 3.4014595e-01 3.8527087e-03 3.2124369e-04 1.0097793e-02
  2.6836985e-04 1.0122993e-04 1.4390526e-04]]
Age : (0-2), conf = 0.645
time : 0.125
Gender : Male, conf = 0.961
Age Output : [[2.4823120e-01 4.7938690e-01 9.6321963e-03 5.5271368e-03 2.5449440e-01
  1.9896324e-03 4.5195332e-04 2.8669275e-04]]
Age : (4-6), conf = 0.479
time : 0.126
Gender : Male, conf = 0.909
Age Output : [[5.2880410e-02 2.9742934e-02 3.1479532e-03 2.0518913e-03 9.0507591e-01
  6.0136458e-03 4.3277859e-04 6.5451121e-04]]
Age : (25-32), conf = 0.905
time : 0.122
Gender : Male, conf = 0.654
Age Output : [[4.2662259e-06 2.5400144e-05 4.2229000e-05 5.0384318e-04 9.9849200e-01
  8.9229288e-04 1.4856013e-05 2.5149515e-05]]
Age : (25-32), conf = 0.998
time : 0.131
Gender : Male, conf = 0.808
Age Output : [[1.4773645e-05 3.3491096e-04 2.3581542e-04 8.8006124e-04 9.9804175e-01
  4.7826479e-04 5.8836267e-06 8.5694637e-06]]
Age : (25-32), conf = 0.998
time : 0.116
Gender : Male, conf = 0.997
Age Output : [[1.8145753e-05 3.1646321e-04 4.0349166e-04 3.2208147e-03 9.8958719e-01
  6.2332205e-03 8.6486434e-05 1.3422276e-04]]
Age : (25-32), conf = 0.990
time : 0.122
Gender : Male, conf = 1.000
Age Output : [[7.93255253e-07 9.87694511e-06 3.10893411e-05 8.09549529e-04
  9.97307897e-01 1.79357198e-03 1.43886145e-05 3.28590977e-05]]
Age : (25-32), conf = 0.997
time : 0.116
Gender : Male, conf = 0.984
Age Output : [[3.03387424e-06 6.13288939e-05 1.04869185e-04 1.41934119e-03
  9.96360958e-01 1.97022152e-03 2.80683453e-05 5.21033835e-05]]
Age : (25-32), conf = 0.996
time : 0.127
Gender : Male, conf = 0.996
Age Output : [[5.9583643e-04 4.3864166e-03 1.6381071e-03 1.1269794e-02 8.9963388e-01
  7.8042671e-02 3.1700481e-03 1.2633323e-03]]
Age : (25-32), conf = 0.900
time : 0.116
Gender : Male, conf = 0.994
Age Output : [[2.2191593e-05 2.8692881e-04 6.5252429e-04 3.7423999e-03 9.7392005e-01
  2.0999761e-02 1.7610405e-04 1.9999285e-04]]
Age : (25-32), conf = 0.974
time : 0.125
Gender : Male, conf = 0.999
Age Output : [[6.8173767e-06 1.8854220e-04 1.8058576e-03 9.9808322e-03 7.3790550e-01
  2.4996565e-01 6.2039813e-05 8.4731189e-05]]
Age : (25-32), conf = 0.738
time : 0.113
Gender : Male, conf = 0.999
Age Output : [[1.10058645e-04 1.20146843e-02 1.50953997e-02 1.94849938e-01
  4.28969353e-01 3.48286092e-01 3.77200224e-04 2.97347957e-04]]
Age : (25-32), conf = 0.429
time : 0.109
Gender : Male, conf = 1.000
Age Output : [[5.63224312e-05 1.30792884e-02 2.66491100e-02 1.24678075e-01
  5.43335259e-01 2.91768998e-01 2.49615579e-04 1.83300363e-04]]
Age : (25-32), conf = 0.543
time : 0.123
Gender : Male, conf = 0.999
Age Output : [[6.6416673e-05 8.1383465e-03 7.5751343e-03 3.0368032e-02 7.8312933e-01
  1.7031443e-01 2.4298082e-04 1.6535405e-04]]
Age : (25-32), conf = 0.783
time : 0.122
Gender : Male, conf = 1.000
Age Output : [[1.5430946e-03 3.3871186e-01 6.2467571e-02 4.7744758e-02 3.3570206e-01
  2.1299243e-01 5.6161243e-04 2.7657984e-04]]
Age : (4-6), conf = 0.339
time : 0.116
Gender : Male, conf = 0.998
Age Output : [[3.3527627e-04 7.7068023e-02 8.3092831e-02 4.5163088e-02 6.0958052e-01
  1.8416134e-01 3.2453847e-04 2.7440616e-04]]
Age : (25-32), conf = 0.610
time : 0.125
Gender : Male, conf = 0.999
Age Output : [[1.5193592e-03 1.7128693e-01 3.5649739e-02 1.2410184e-02 6.9753826e-01
  8.0964588e-02 4.0451670e-04 2.2642264e-04]]
Age : (25-32), conf = 0.698
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[1.5193592e-03 1.7128693e-01 3.5649739e-02 1.2410184e-02 6.9753826e-01
  8.0964588e-02 4.0451670e-04 2.2642264e-04]]
Age : (25-32), conf = 0.698
time : 0.129
Gender : Male, conf = 1.000
Age Output : [[1.2810314e-02 6.6367579e-01 2.2223448e-02 8.3789174e-03 2.4725933e-01
  4.4520386e-02 8.2088227e-04 3.1090967e-04]]
Age : (4-6), conf = 0.664
time : 0.109
Gender : Male, conf = 0.999
Age Output : [[2.4145462e-01 6.6812247e-01 9.8323887e-03 4.6158535e-03 5.7107057e-02
  1.6288871e-02 2.0293486e-03 5.4944621e-04]]
Age : (4-6), conf = 0.668
time : 0.110
Gender : Male, conf = 0.999
Age Output : [[2.1727614e-01 7.4065697e-01 7.3927906e-03 2.7529832e-03 2.3169287e-02
  7.4380194e-03 1.0067684e-03 3.0704320e-04]]
Age : (4-6), conf = 0.741
time : 0.094
Gender : Male, conf = 0.999
Age Output : [[0.14454007 0.59589314 0.01262725 0.01258431 0.20642005 0.02553402
  0.0016027  0.00079843]]
Age : (4-6), conf = 0.596
time : 0.104
Gender : Male, conf = 0.999
Age Output : [[0.14454007 0.59589314 0.01262725 0.01258431 0.20642005 0.02553402
  0.0016027  0.00079843]]
Age : (4-6), conf = 0.596
time : 0.090
Gender : Male, conf = 1.000
Age Output : [[7.1909338e-02 8.0321223e-01 1.0157287e-02 9.5130596e-03 9.1850623e-02
  1.2391869e-02 5.8526179e-04 3.8023136e-04]]
Age : (4-6), conf = 0.803
time : 0.103
Gender : Male, conf = 1.000
Age Output : [[3.4013789e-02 6.0902572e-01 1.8485321e-02 1.9463383e-02 2.9629365e-01
  2.1488799e-02 6.9018389e-04 5.3924404e-04]]
Age : (4-6), conf = 0.609
time : 0.112
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 1.000
Age Output : [[0.01203771 0.28922766 0.01681784 0.04424455 0.578742   0.05646299
  0.00148297 0.00098423]]
Age : (25-32), conf = 0.579
time : 0.125
Gender : Male, conf = 0.999
Age Output : [[2.3070244e-02 6.3188243e-01 3.8472418e-02 2.5060626e-02 2.4855711e-01
  3.1784210e-02 6.5851753e-04 5.1436998e-04]]
Age : (4-6), conf = 0.632
time : 0.131
Gender : Male, conf = 0.999
Age Output : [[6.9492154e-02 8.1651491e-01 1.2968883e-02 1.0713966e-02 7.9986505e-02
  9.5354449e-03 5.1301194e-04 2.7504066e-04]]
Age : (4-6), conf = 0.817
time : 0.122
Gender : Male, conf = 0.997
Age Output : [[6.5698801e-03 9.6209365e-01 2.0898970e-02 1.5642896e-03 6.5146699e-03
  2.3165625e-03 2.4827747e-05 1.7254159e-05]]
Age : (4-6), conf = 0.962
time : 0.107
Gender : Male, conf = 0.999
Age Output : [[8.19375925e-03 8.85975659e-01 3.30268629e-02 1.20450845e-02
  5.67194484e-02 3.94683098e-03 3.98419179e-05 5.27185730e-05]]
Age : (4-6), conf = 0.886
time : 0.094
Gender : Male, conf = 0.999
Age Output : [[5.2076592e-03 8.4795702e-01 1.0383695e-01 5.7077818e-03 3.2734506e-02
  4.4694315e-03 3.2357686e-05 5.4223197e-05]]
Age : (4-6), conf = 0.848
time : 0.097
Gender : Male, conf = 0.999
Age Output : [[2.8105592e-02 9.4949138e-01 7.3147016e-03 3.1214328e-03 1.1164907e-02
  7.1470323e-04 4.3921766e-05 4.3443863e-05]]
Age : (4-6), conf = 0.949
time : 0.079
Gender : Male, conf = 1.000
Age Output : [[2.3686159e-02 9.6027112e-01 7.3048277e-03 7.8056229e-04 7.4968291e-03
  4.2210118e-04 1.8247463e-05 2.0112526e-05]]
Age : (4-6), conf = 0.960
time : 0.101
Gender : Male, conf = 1.000
Age Output : [[1.8860063e-02 9.5220554e-01 1.6192950e-02 2.2291609e-03 9.4182044e-03
  1.0458509e-03 2.1116768e-05 2.7155766e-05]]
Age : (4-6), conf = 0.952
time : 0.085
Gender : Male, conf = 1.000
Age Output : [[1.8860063e-02 9.5220554e-01 1.6192950e-02 2.2291609e-03 9.4182044e-03
  1.0458509e-03 2.1116768e-05 2.7155766e-05]]
Age : (4-6), conf = 0.952
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[1.9785736e-03 2.0534915e-01 7.9155996e-02 1.4327110e-02 6.8321973e-01
  1.5695849e-02 1.2221620e-04 1.5143180e-04]]
Age : (25-32), conf = 0.683
time : 0.087
Gender : Male, conf = 1.000
Age Output : [[1.10034635e-02 5.67415953e-01 8.35429206e-02 1.94372647e-02
  2.91657805e-01 2.65336167e-02 2.33865707e-04 1.75103065e-04]]
Age : (4-6), conf = 0.567
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[1.21874427e-02 8.70925963e-01 3.27611864e-02 2.08109953e-02
  5.79144023e-02 5.16961422e-03 1.19782795e-04 1.10701141e-04]]
Age : (4-6), conf = 0.871
time : 0.091
Gender : Male, conf = 1.000
Age Output : [[1.30784735e-02 8.00687790e-01 3.59121002e-02 2.67158058e-02
  1.08722351e-01 1.45645747e-02 1.85921133e-04 1.33031994e-04]]
Age : (4-6), conf = 0.801
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[1.6693473e-02 8.9203489e-01 1.6154066e-02 1.4369923e-02 5.4799967e-02
  5.6053023e-03 1.9734341e-04 1.4499441e-04]]
Age : (4-6), conf = 0.892
time : 0.089
Gender : Male, conf = 1.000
Age Output : [[0.01070402 0.30667368 0.04612673 0.06430938 0.5292666  0.0417731
  0.00059594 0.00055057]]
Age : (25-32), conf = 0.529
time : 0.099
Gender : Male, conf = 1.000
Age Output : [[0.01070402 0.30667368 0.04612673 0.06430938 0.5292666  0.0417731
  0.00059594 0.00055057]]
Age : (25-32), conf = 0.529
time : 0.079
Gender : Male, conf = 1.000
Age Output : [[2.7666194e-02 8.4332061e-01 1.9070299e-02 1.5866365e-02 8.3348669e-02
  1.0253409e-02 2.9786164e-04 1.7654727e-04]]
Age : (4-6), conf = 0.843
time : 0.101
Gender : Male, conf = 1.000
Age Output : [[2.1873137e-02 8.8805926e-01 2.2456694e-02 9.8435348e-03 5.0462194e-02
  7.0025185e-03 1.7697853e-04 1.2557319e-04]]
Age : (4-6), conf = 0.888
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[1.47018405e-02 9.48375285e-01 1.49930026e-02 3.08144372e-03
  1.39075667e-02 4.75884043e-03 1.30839573e-04 5.11734943e-05]]
Age : (4-6), conf = 0.948
time : 0.084
Gender : Male, conf = 1.000
Age Output : [[1.9133283e-02 9.4974464e-01 1.1592988e-02 2.5918777e-03 1.2699282e-02
  4.0603764e-03 1.2679760e-04 5.0821323e-05]]
Age : (4-6), conf = 0.950
time : 0.085
Gender : Male, conf = 1.000
Age Output : [[1.7668467e-02 8.7370896e-01 3.2764882e-02 6.7503336e-03 5.3482611e-02
  1.5257354e-02 2.5337454e-04 1.1409426e-04]]
Age : (4-6), conf = 0.874
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[1.38534475e-02 7.38079906e-01 5.16622998e-02 2.00481322e-02
  1.35756627e-01 3.98959108e-02 4.56767331e-04 2.46886862e-04]]
Age : (4-6), conf = 0.738
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[1.1628640e-02 7.7472019e-01 4.7494829e-02 1.9875819e-02 1.2905674e-01
  1.6769225e-02 3.0292058e-04 1.5167963e-04]]
Age : (4-6), conf = 0.775
time : 0.095
Gender : Male, conf = 0.999
Age Output : [[1.1628640e-02 7.7472019e-01 4.7494829e-02 1.9875819e-02 1.2905674e-01
  1.6769225e-02 3.0292058e-04 1.5167963e-04]]
Age : (4-6), conf = 0.775
time : 0.081
Gender : Male, conf = 1.000
Age Output : [[1.2929589e-02 8.1755406e-01 3.4495417e-02 1.5559923e-02 1.0580218e-01
  1.3252107e-02 2.7253540e-04 1.3424690e-04]]
Age : (4-6), conf = 0.818
time : 0.103
Gender : Male, conf = 1.000
Age Output : [[1.1147326e-02 1.8307602e-01 1.5693130e-02 4.1922484e-02 7.0297503e-01
  4.3610327e-02 9.5038739e-04 6.2536495e-04]]
Age : (25-32), conf = 0.703
time : 0.094
Gender : Male, conf = 1.000
Age Output : [[1.1419791e-02 7.1124190e-01 5.2878048e-02 2.5743265e-02 1.7698433e-01
  2.1320917e-02 2.5532593e-04 1.5643357e-04]]
Age : (4-6), conf = 0.711
time : 0.101
Gender : Male, conf = 1.000
Age Output : [[0.0195891  0.49271253 0.02814629 0.03048788 0.4079658  0.02002563
  0.00057207 0.00050064]]
Age : (4-6), conf = 0.493
time : 0.080
Gender : Male, conf = 0.999
Age Output : [[6.1291703e-03 2.7628911e-01 2.6713239e-02 2.7841311e-02 6.4626986e-01
  1.6071100e-02 3.7958383e-04 3.0665423e-04]]
Age : (25-32), conf = 0.646
time : 0.104
Gender : Male, conf = 0.999
Age Output : [[4.5321267e-03 1.5964311e-01 2.3155751e-02 2.5289033e-02 7.6909339e-01
  1.7714430e-02 2.6856130e-04 3.0356678e-04]]
Age : (25-32), conf = 0.769
time : 0.087
Gender : Male, conf = 0.999
Age Output : [[1.0623820e-03 4.5601945e-02 1.8920219e-02 1.8387010e-02 8.9943302e-01
  1.6067924e-02 2.6410152e-04 2.6342561e-04]]
Age : (25-32), conf = 0.899
time : 0.118
Gender : Male, conf = 0.999
Age Output : [[1.0623820e-03 4.5601945e-02 1.8920219e-02 1.8387010e-02 8.9943302e-01
  1.6067924e-02 2.6410152e-04 2.6342561e-04]]
Age : (25-32), conf = 0.899
time : 0.079
Gender : Male, conf = 0.999
Age Output : [[1.5228517e-02 8.3872122e-01 1.6655579e-02 1.4713130e-02 1.1080235e-01
  3.6024884e-03 1.4347096e-04 1.3307028e-04]]
Age : (4-6), conf = 0.839
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[1.7382405e-03 5.2085053e-02 1.2076912e-02 2.7705019e-02 8.8943231e-01
  1.6524589e-02 2.4085633e-04 1.9701906e-04]]
Age : (25-32), conf = 0.889
time : 0.088
Gender : Male, conf = 0.999
Age Output : [[8.21162830e-04 2.40176655e-02 7.37164682e-03 2.72589605e-02
  9.26062942e-01 1.40694305e-02 1.97558169e-04 2.00598646e-04]]
Age : (25-32), conf = 0.926
time : 0.081
Gender : Male, conf = 0.998
Age Output : [[1.37245492e-03 8.86455551e-02 1.71443596e-02 2.66810674e-02
  8.52354348e-01 1.34915365e-02 1.67700186e-04 1.43011988e-04]]
Age : (25-32), conf = 0.852
time : 0.102
Gender : Male, conf = 1.000
Age Output : [[3.5695907e-02 8.9540738e-01 1.1317482e-02 2.8950903e-03 4.5356248e-02
  8.8838385e-03 3.2894019e-04 1.1503903e-04]]
Age : (4-6), conf = 0.895
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[1.2847062e-02 6.8345600e-01 2.0337058e-02 1.9014390e-02 2.5397751e-01
  9.9153807e-03 2.6282039e-04 1.8984832e-04]]
Age : (4-6), conf = 0.683
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[1.2847062e-02 6.8345600e-01 2.0337058e-02 1.9014390e-02 2.5397751e-01
  9.9153807e-03 2.6282039e-04 1.8984832e-04]]
Age : (4-6), conf = 0.683
time : 0.087
Gender : Male, conf = 0.999
Age Output : [[2.2029817e-02 8.8794833e-01 1.8518209e-02 8.4986528e-03 5.6903694e-02
  5.7858415e-03 1.7951525e-04 1.3593781e-04]]
Age : (4-6), conf = 0.888
time : 0.088
Gender : Male, conf = 1.000
Age Output : [[1.1077492e-02 5.1585275e-01 2.7403368e-02 3.4634158e-02 3.9234057e-01
  1.7725991e-02 4.2977987e-04 5.3583470e-04]]
Age : (4-6), conf = 0.516
time : 0.081
Gender : Male, conf = 0.999
Age Output : [[3.1275339e-02 8.7606335e-01 1.4797618e-02 8.5090045e-03 6.2777571e-02
  6.2071732e-03 1.9880806e-04 1.7105881e-04]]
Age : (4-6), conf = 0.876
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>time : 0.083
Gender : Male, conf = 0.999
Age Output : [[7.6593868e-03 2.3877271e-01 2.6774110e-02 4.5234144e-02 6.6263586e-01
  1.8216543e-02 3.6383988e-04 3.4346271e-04]]
Age : (25-32), conf = 0.663
time : 0.103
Gender : Male, conf = 1.000
Age Output : [[4.1288161e-03 2.8115061e-01 9.4846040e-02 5.0614957e-02 5.3721732e-01
  3.1241396e-02 4.6745469e-04 3.3343461e-04]]
Age : (25-32), conf = 0.537
time : 0.097
Gender : Male, conf = 1.000
Age Output : [[4.1288161e-03 2.8115061e-01 9.4846040e-02 5.0614957e-02 5.3721732e-01
  3.1241396e-02 4.6745469e-04 3.3343461e-04]]
Age : (25-32), conf = 0.537
time : 0.092
Gender : Male, conf = 0.999
Age Output : [[7.4311709e-03 8.8733059e-01 4.1785065e-02 1.5921148e-02 4.3490887e-02
  3.8819222e-03 8.2263221e-05 7.6873301e-05]]
Age : (4-6), conf = 0.887
time : 0.101
Gender : Male, conf = 1.000
Age Output : [[3.1930674e-02 7.8988349e-01 2.1899533e-02 2.0559566e-02 1.2562339e-01
  9.3521057e-03 3.4434701e-04 4.0680773e-04]]
Age : (4-6), conf = 0.790
time : 0.088
Gender : Male, conf = 1.000
Age Output : [[1.2026926e-02 6.8563932e-01 2.8801983e-02 1.8995248e-02 2.4331748e-01
  1.0626025e-02 3.0453157e-04 2.8854626e-04]]
Age : (4-6), conf = 0.686
time : 0.096
Gender : Male, conf = 0.999
Age Output : [[7.4484348e-03 5.8404011e-01 5.1615402e-02 3.1609226e-02 3.1175914e-01
  1.2984529e-02 2.7757962e-04 2.6559175e-04]]
Age : (4-6), conf = 0.584
time : 0.079
Gender : Male, conf = 0.999
Age Output : [[7.3398259e-03 4.2033577e-01 3.7509132e-02 3.3996511e-02 4.8085585e-01
  1.9382307e-02 3.0500573e-04 2.7565745e-04]]
Age : (25-32), conf = 0.481
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[0.02473614 0.48311523 0.02942949 0.05019195 0.3901837  0.02128844
  0.0004917  0.00056336]]
Age : (4-6), conf = 0.483
time : 0.087
Gender : Male, conf = 0.999
Age Output : [[2.1774236e-03 4.3516108e-01 1.2114382e-01 7.5796239e-02 3.5840967e-01
  6.9743758e-03 1.7109700e-04 1.6617043e-04]]
Age : (4-6), conf = 0.435
time : 0.098
Gender : Male, conf = 0.999
Age Output : [[2.1774236e-03 4.3516108e-01 1.2114382e-01 7.5796239e-02 3.5840967e-01
  6.9743758e-03 1.7109700e-04 1.6617043e-04]]
Age : (4-6), conf = 0.435
time : 0.090
Gender : Male, conf = 0.999
Age Output : [[1.06348125e-02 6.64576650e-01 3.85600887e-02 1.69842392e-02
  2.58488894e-01 1.01062218e-02 3.61351762e-04 2.87733244e-04]]
Age : (4-6), conf = 0.665
time : 0.099
Gender : Male, conf = 0.999
Age Output : [[0.0304192  0.55466026 0.03125332 0.02218897 0.3233389  0.03678699
  0.00076226 0.0005901 ]]
Age : (4-6), conf = 0.555
time : 0.089
Gender : Male, conf = 0.999
Age Output : [[1.7617863e-02 8.9432842e-01 2.0865023e-02 1.1239385e-02 4.9487922e-02
  6.2132431e-03 1.4695314e-04 1.0129274e-04]]
Age : (4-6), conf = 0.894
time : 0.099
Gender : Male, conf = 0.999
Age Output : [[3.8230959e-03 3.1549570e-01 3.9308716e-02 2.9182758e-02 5.9735084e-01
  1.4450378e-02 1.9277021e-04 1.9574484e-04]]
Age : (25-32), conf = 0.597
time : 0.089
Gender : Male, conf = 0.999
Age Output : [[1.4938061e-02 4.7812933e-01 3.3608325e-02 3.4819745e-02 4.1698158e-01
  2.0602418e-02 4.9386924e-04 4.2666029e-04]]
Age : (4-6), conf = 0.478
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[6.5210350e-03 5.8274543e-01 5.9890565e-02 1.9748023e-02 3.1268778e-01
  1.7936995e-02 2.2423094e-04 2.4600941e-04]]
Age : (4-6), conf = 0.583
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[5.2496899e-02 8.6016279e-01 9.5031885e-03 7.0658089e-03 6.5651231e-02
  4.5700748e-03 3.1349962e-04 2.3655388e-04]]
Age : (4-6), conf = 0.860
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[5.2496899e-02 8.6016279e-01 9.5031885e-03 7.0658089e-03 6.5651231e-02
  4.5700748e-03 3.1349962e-04 2.3655388e-04]]
Age : (4-6), conf = 0.860
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[9.8894245e-04 8.1501856e-02 2.0614609e-02 1.0128163e-02 8.7334281e-01
  1.2918227e-02 2.1303147e-04 2.9232918e-04]]
Age : (25-32), conf = 0.873
time : 0.102
Gender : Male, conf = 1.000
Age Output : [[7.7159476e-04 3.2548644e-02 1.1088705e-02 7.3125060e-03 9.1597402e-01
  3.1761095e-02 2.7255531e-04 2.7091234e-04]]
Age : (25-32), conf = 0.916
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[5.0580670e-04 2.6158309e-02 9.9142008e-03 4.5863106e-03 9.3268490e-01
  2.5576176e-02 2.9219891e-04 2.8223876e-04]]
Age : (25-32), conf = 0.933
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[4.4034579e-04 1.0835209e-02 3.8009067e-03 2.9082040e-03 9.4643688e-01
  3.4856871e-02 3.6474908e-04 3.5669695e-04]]
Age : (25-32), conf = 0.946
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[7.8617007e-04 1.7364692e-02 7.1220435e-03 4.5881397e-03 8.8729447e-01
  8.2136162e-02 4.0663665e-04 3.0163559e-04]]
Age : (25-32), conf = 0.887
time : 0.099
Gender : Male, conf = 0.999
Age Output : [[2.5709770e-03 6.4426720e-02 1.0340402e-02 4.0007932e-03 8.7863564e-01
  3.9090179e-02 4.9671775e-04 4.3858105e-04]]
Age : (25-32), conf = 0.879
time : 0.098
Gender : Male, conf = 0.999
Age Output : [[4.0409748e-05 9.4929630e-05 2.2428532e-04 5.1301392e-04 9.8594356e-01
  1.3025455e-02 6.4126834e-05 9.4091854e-05]]
Age : (25-32), conf = 0.986
time : 0.108
Gender : Male, conf = 1.000
Age Output : [[2.7122855e-06 1.8046356e-05 6.9170041e-05 1.1834418e-04 9.9831784e-01
  1.4445116e-03 1.5806951e-05 1.3526385e-05]]
Age : (25-32), conf = 0.998
time : 0.100
Gender : Male, conf = 0.997
Age Output : [[8.89814018e-08 1.16678234e-06 1.44418245e-05 1.66633967e-04
  9.99566972e-01 2.46827229e-04 1.98251246e-06 1.89871764e-06]]
Age : (25-32), conf = 1.000
time : 0.110
Gender : Male, conf = 0.997
Age Output : [[8.89814018e-08 1.16678234e-06 1.44418245e-05 1.66633967e-04
  9.99566972e-01 2.46827229e-04 1.98251246e-06 1.89871764e-06]]
Age : (25-32), conf = 1.000
time : 0.099
Gender : Male, conf = 0.971
Age Output : [[1.6675912e-06 1.6988371e-05 1.2786817e-04 7.1660959e-04 9.9700063e-01
  2.1124030e-03 1.0615520e-05 1.3366919e-05]]
Age : (25-32), conf = 0.997
time : 0.101
Gender : Male, conf = 0.995
Age Output : [[0.06038556 0.07082369 0.01201374 0.02212519 0.7136263  0.11282299
  0.00459358 0.00360897]]
Age : (25-32), conf = 0.714
time : 0.101
Gender : Male, conf = 0.867
Age Output : [[1.3119321e-03 1.1913691e-03 1.3467042e-03 3.0534838e-03 9.2645806e-01
  6.5746240e-02 2.4521325e-04 6.4702512e-04]]
Age : (25-32), conf = 0.926
time : 0.106
Gender : Male, conf = 0.910
Age Output : [[8.7584723e-03 2.0532025e-02 7.2449003e-03 1.6814465e-02 8.5376221e-01
  9.0961732e-02 5.4527813e-04 1.3808942e-03]]
Age : (25-32), conf = 0.854
time : 0.085
Gender : Male, conf = 0.949
Age Output : [[0.149743   0.11519462 0.01151629 0.01746054 0.6290003  0.07309954
  0.00152358 0.0024621 ]]
Age : (25-32), conf = 0.629
time : 0.100
Gender : Male, conf = 0.967
Age Output : [[7.7361971e-02 3.5469733e-02 5.9307879e-03 1.9051401e-02 8.0967534e-01
  5.0296038e-02 6.7780021e-04 1.5370124e-03]]
Age : (25-32), conf = 0.810
time : 0.092
Gender : Male, conf = 0.879
Age Output : [[0.11676646 0.08418521 0.00714273 0.01457966 0.72672755 0.04786943
  0.0012142  0.00151477]]
Age : (25-32), conf = 0.727
time : 0.101
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.983
Age Output : [[8.1740242e-01 1.6833593e-01 2.6775775e-03 7.1445177e-04 8.5791154e-03
  1.9425863e-03 1.7745068e-04 1.7038709e-04]]
Age : (0-2), conf = 0.817
time : 0.098
Gender : Male, conf = 0.999
Age Output : [[1.3229309e-02 5.2684087e-01 5.0260890e-02 1.4651067e-02 3.8805130e-01
  6.4112549e-03 2.4948776e-04 3.0582910e-04]]
Age : (4-6), conf = 0.527
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[1.4679472e-02 5.9153533e-01 9.3022719e-02 1.6219825e-02 2.7553877e-01
  8.4070824e-03 1.8825236e-04 4.0855963e-04]]
Age : (4-6), conf = 0.592
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[7.3676989e-03 2.2261986e-01 1.1797702e-01 1.1162907e-02 6.1702961e-01
  2.2878842e-02 3.0698185e-04 6.5706071e-04]]
Age : (25-32), conf = 0.617
time : 0.101
Gender : Male, conf = 1.000
Age Output : [[3.9744791e-02 5.6658733e-01 5.1007427e-02 7.0430636e-03 3.2097125e-01
  1.3833793e-02 2.5703691e-04 5.5530964e-04]]
Age : (4-6), conf = 0.567
time : 0.088
Gender : Male, conf = 1.000
Age Output : [[5.6397831e-03 1.1919029e-01 5.4934952e-02 4.6361103e-03 8.0222523e-01
  1.2838167e-02 1.3525995e-04 4.0022991e-04]]
Age : (25-32), conf = 0.802
time : 0.102
Gender : Male, conf = 1.000
Age Output : [[1.2824297e-01 4.7729194e-01 3.1856444e-02 1.1945261e-02 3.2888201e-01
  2.0382142e-02 4.3109222e-04 9.6824358e-04]]
Age : (4-6), conf = 0.477
time : 0.090
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 1.000
Age Output : [[1.2824297e-01 4.7729194e-01 3.1856444e-02 1.1945261e-02 3.2888201e-01
  2.0382142e-02 4.3109222e-04 9.6824358e-04]]
Age : (4-6), conf = 0.477
time : 0.100
Gender : Male, conf = 1.000
Age Output : [[1.8840486e-01 6.1216593e-01 2.0852420e-02 2.6088578e-03 1.6871107e-01
  6.5131984e-03 2.4343647e-04 5.0016318e-04]]
Age : (4-6), conf = 0.612
time : 0.085
Gender : Male, conf = 1.000
Age Output : [[2.4410416e-01 6.3339305e-01 1.2408491e-02 3.5636940e-03 1.0161441e-01
  4.3331184e-03 2.5669165e-04 3.2651526e-04]]
Age : (4-6), conf = 0.633
time : 0.096
Gender : Male, conf = 1.000
Age Output : [[1.3148183e-01 8.0852938e-01 1.9340985e-02 1.9977412e-03 3.7097204e-02
  1.3406512e-03 5.9777874e-05 1.5250265e-04]]
Age : (4-6), conf = 0.809
time : 0.077
Gender : Male, conf = 1.000
Age Output : [[1.53994143e-01 7.68205464e-01 2.02639569e-02 2.30138795e-03
  5.24322689e-02 2.40008137e-03 1.08488166e-04 2.94128200e-04]]
Age : (4-6), conf = 0.768
time : 0.104
Gender : Male, conf = 1.000
Age Output : [[3.4206808e-01 5.8781213e-01 1.4002454e-02 1.4588815e-03 5.0800506e-02
  3.2860509e-03 1.8216803e-04 3.8959293e-04]]
Age : (4-6), conf = 0.588
time : 0.086
Gender : Male, conf = 1.000
Age Output : [[2.0616469e-01 7.2666448e-01 1.5642276e-02 1.1128829e-03 4.7392324e-02
  2.6930724e-03 1.1313092e-04 2.1718246e-04]]
Age : (4-6), conf = 0.727
time : 0.084
Gender : Male, conf = 1.000
Age Output : [[2.0616469e-01 7.2666448e-01 1.5642276e-02 1.1128829e-03 4.7392324e-02
  2.6930724e-03 1.1313092e-04 2.1718246e-04]]
Age : (4-6), conf = 0.727
time : 0.087
Gender : Male, conf = 0.999
Age Output : [[2.0636473e-02 5.2000338e-01 4.8936136e-02 7.2290045e-03 3.9979562e-01
  3.0632725e-03 1.0500469e-04 2.3107842e-04]]
Age : (4-6), conf = 0.520
time : 0.099
Gender : Male, conf = 1.000
Age Output : [[1.4732437e-01 8.0004966e-01 1.0467749e-02 1.6063357e-03 3.9532539e-02
  8.0623676e-04 8.6137014e-05 1.2705679e-04]]
Age : (4-6), conf = 0.800
time : 0.089
Gender : Male, conf = 0.997
Age Output : [[3.3278335e-02 1.8432926e-01 7.0975022e-03 4.2939321e-03 7.6467139e-01
  5.3618485e-03 4.6887185e-04 4.9882004e-04]]
Age : (25-32), conf = 0.765
time : 0.099
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 1.000
Age Output : [[9.9137928e-03 4.3962768e-01 2.7774617e-01 6.6294007e-02 1.1697629e-01
  8.8831544e-02 2.5872601e-04 3.5171601e-04]]
Age : (4-6), conf = 0.440
time : 0.090
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.999
Age Output : [[1.8355456e-03 2.5297241e-02 5.1317103e-02 3.5750885e-02 3.6728072e-01
  5.1767582e-01 3.5843454e-04 4.8432118e-04]]
Age : (38-43), conf = 0.518
time : 0.089
Gender : Male, conf = 1.000
Age Output : [[0.00358502 0.05596131 0.07162619 0.20027363 0.33633563 0.33086956
  0.0005727  0.00077598]]
Age : (25-32), conf = 0.336
time : 0.078
Gender : Male, conf = 1.000
Age Output : [[0.00170083 0.14447485 0.15049149 0.04945213 0.26655775 0.38626763
  0.00054507 0.00051016]]
Age : (38-43), conf = 0.386
time : 0.127
Gender : Male, conf = 0.999
Age Output : [[0.00584604 0.18151295 0.26478675 0.12828346 0.09781694 0.32088134
  0.00041658 0.00045601]]
Age : (38-43), conf = 0.321
time : 0.111
Gender : Male, conf = 0.999
Age Output : [[1.4089893e-03 9.3516342e-02 3.3031380e-01 1.5109295e-01 2.2876211e-01
  1.9435477e-01 2.4538810e-04 3.0556039e-04]]
Age : (8-12), conf = 0.330
time : 0.122
Gender : Male, conf = 0.999
Age Output : [[2.29402934e-03 1.52932107e-01 4.20489699e-01 8.71701613e-02
  1.23063825e-01 2.13628501e-01 2.01143848e-04 2.20558271e-04]]
Age : (8-12), conf = 0.420
time : 0.116
Gender : Male, conf = 0.999
Age Output : [[2.6056673e-03 1.1933529e-01 3.5955450e-01 1.5506665e-01 1.4942446e-01
  2.1336335e-01 3.3639398e-04 3.1362660e-04]]
Age : (8-12), conf = 0.360
time : 0.133
Gender : Male, conf = 0.999
Age Output : [[2.8805588e-03 4.1941598e-01 3.4505472e-01 1.2588982e-01 4.7333203e-02
  5.9159029e-02 1.2798999e-04 1.3870756e-04]]
Age : (4-6), conf = 0.419
time : 0.115
Gender : Male, conf = 0.993
Age Output : [[2.87875329e-04 2.41909474e-02 3.38916600e-01 3.57024670e-01
  2.23344177e-01 5.60523309e-02 7.62203199e-05 1.07211374e-04]]
Age : (15-20), conf = 0.357
time : 0.116
Gender : Male, conf = 0.995
Age Output : [[1.7026134e-05 9.6139155e-04 8.9163706e-02 1.1580374e-01 6.1047530e-01
  1.8337147e-01 1.1515874e-04 9.2292568e-05]]
Age : (25-32), conf = 0.610
time : 0.116
Gender : Male, conf = 0.995
Age Output : [[3.60734593e-05 2.67630257e-03 2.42140532e-01 1.44657180e-01
  5.05444467e-01 1.04872145e-01 9.57290758e-05 7.75281369e-05]]
Age : (25-32), conf = 0.505
time : 0.122
Gender : Male, conf = 0.997
Age Output : [[1.1294489e-05 5.0218491e-04 4.4837367e-02 7.7013262e-02 7.9700392e-01
  8.0532528e-02 5.5321892e-05 4.4153297e-05]]
Age : (25-32), conf = 0.797
time : 0.116
Gender : Male, conf = 0.986
Age Output : [[4.3974120e-05 2.3701061e-04 2.7681919e-02 4.4963822e-02 7.1088338e-01
  2.1601805e-01 6.6007568e-05 1.0584657e-04]]
Age : (25-32), conf = 0.711
time : 0.118
Gender : Male, conf = 0.988
Age Output : [[1.6215334e-04 1.3419441e-03 9.7821772e-02 5.4318346e-02 6.3658118e-01
  2.0947401e-01 1.1527436e-04 1.8531583e-04]]
Age : (25-32), conf = 0.637
time : 0.113
Gender : Male, conf = 0.992
Age Output : [[1.0486257e-04 1.0500625e-03 1.3532943e-01 3.4004781e-02 7.0370936e-01
  1.2557854e-01 9.4414885e-05 1.2860855e-04]]
Age : (25-32), conf = 0.704
time : 0.116
Gender : Male, conf = 0.994
Age Output : [[3.8178259e-06 1.8117810e-04 1.9261817e-02 5.6861728e-02 8.8792235e-01
  3.5714038e-02 3.2612759e-05 2.2461987e-05]]
Age : (25-32), conf = 0.888
time : 0.116
Gender : Male, conf = 0.990
Age Output : [[1.6257207e-05 8.6849753e-04 2.5777251e-02 1.4678626e-01 7.8307670e-01
  4.3394357e-02 4.6234531e-05 3.4559973e-05]]
Age : (25-32), conf = 0.783
time : 0.122
Gender : Male, conf = 0.986
Age Output : [[2.2075365e-05 7.6113467e-04 1.5459452e-02 4.8060093e-02 8.8605911e-01
  4.9514379e-02 7.0804737e-05 5.2934287e-05]]
Age : (25-32), conf = 0.886
time : 0.116
Gender : Male, conf = 0.992
Age Output : [[4.4292578e-06 1.8449761e-04 3.9672670e-03 2.8146617e-02 9.4543445e-01
  2.2222120e-02 2.5619436e-05 1.5052707e-05]]
Age : (25-32), conf = 0.945
time : 0.132
Gender : Male, conf = 0.997
Age Output : [[5.1237630e-06 1.3748730e-04 1.6658850e-02 5.1058788e-02 8.5669565e-01
  7.5286143e-02 9.9857425e-05 5.8070993e-05]]
Age : (25-32), conf = 0.857
time : 0.105
Gender : Male, conf = 0.991
Age Output : [[6.0189514e-06 1.1812140e-04 1.4946357e-02 3.2760177e-02 8.4409928e-01
  1.0791031e-01 9.5273252e-05 6.4500964e-05]]
Age : (25-32), conf = 0.844
time : 0.116
Gender : Male, conf = 0.977
Age Output : [[5.6964232e-05 1.8293032e-03 3.4985527e-02 1.0871902e-01 7.2312474e-01
  1.3108532e-01 1.0591774e-04 9.3202274e-05]]
Age : (25-32), conf = 0.723
time : 0.116
Gender : Male, conf = 0.992
Age Output : [[5.3991712e-06 1.7667031e-04 6.5966141e-03 4.0897362e-02 9.2855936e-01
  2.3707720e-02 3.2756634e-05 2.3976261e-05]]
Age : (25-32), conf = 0.929
time : 0.120
Gender : Male, conf = 0.990
Age Output : [[1.3282032e-05 5.4899853e-04 4.1534867e-02 8.6601831e-02 8.2940942e-01
  4.1816507e-02 4.3415828e-05 3.1772975e-05]]
Age : (25-32), conf = 0.829
time : 0.103
Gender : Male, conf = 0.987
Age Output : [[6.9167550e-06 1.3307390e-04 1.4990600e-02 4.1972499e-02 8.8136172e-01
  6.1447922e-02 4.7853679e-05 3.9383569e-05]]
Age : (25-32), conf = 0.881
time : 0.099
Gender : Male, conf = 0.994
Age Output : [[1.5020411e-05 6.1301142e-04 2.3454908e-02 9.1292277e-02 8.4988981e-01
  3.4662992e-02 3.7039030e-05 3.4803783e-05]]
Age : (25-32), conf = 0.850
time : 0.082
Gender : Male, conf = 0.987
Age Output : [[1.7600468e-06 2.0444617e-05 1.4822135e-03 8.1580495e-03 9.6490002e-01
  2.5394605e-02 2.2560527e-05 2.0319030e-05]]
Age : (25-32), conf = 0.965
time : 0.102
Gender : Male, conf = 0.987
Age Output : [[1.7600468e-06 2.0444617e-05 1.4822135e-03 8.1580495e-03 9.6490002e-01
  2.5394605e-02 2.2560527e-05 2.0319030e-05]]
Age : (25-32), conf = 0.965
time : 0.086
Gender : Male, conf = 0.995
Age Output : [[3.2452253e-06 1.5617369e-04 1.8463472e-02 4.9747609e-02 9.1086811e-01
  2.0717226e-02 2.3699875e-05 2.0363599e-05]]
Age : (25-32), conf = 0.911
time : 0.121
Gender : Male, conf = 0.993
Age Output : [[4.0107379e-06 1.5618969e-04 1.1422387e-02 4.9055174e-02 9.1759676e-01
  2.1719594e-02 2.4094395e-05 2.1924918e-05]]
Age : (25-32), conf = 0.918
time : 0.115
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.991
Age Output : [[3.5050693e-05 8.2007324e-04 7.7841487e-03 4.4634465e-02 9.1206199e-01
  3.4566265e-02 5.8313868e-05 3.9838153e-05]]
Age : (25-32), conf = 0.912
time : 0.132
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.994
Age Output : [[6.4483988e-06 6.5655848e-05 7.0015211e-03 2.7881904e-02 9.4342506e-01
  2.1550000e-02 3.0459139e-05 3.9035713e-05]]
Age : (25-32), conf = 0.943
time : 0.100
Gender : Male, conf = 0.989
Age Output : [[2.2117870e-06 1.6558230e-05 3.0495124e-03 1.8077457e-02 9.4694316e-01
  3.1850766e-02 2.3886685e-05 3.6351052e-05]]
Age : (25-32), conf = 0.947
time : 0.085
Gender : Male, conf = 0.986
Age Output : [[3.0568558e-06 2.1922742e-05 4.5458716e-03 2.4952734e-02 9.3945009e-01
  3.0958766e-02 2.7170783e-05 4.0417261e-05]]
Age : (25-32), conf = 0.939
time : 0.100
Gender : Male, conf = 0.964
Age Output : [[4.8572703e-05 1.8646901e-04 4.1072968e-02 1.0164494e-02 8.8526386e-01
  6.3034691e-02 8.0335820e-05 1.4854108e-04]]
Age : (25-32), conf = 0.885
time : 0.090
Gender : Male, conf = 0.964
Age Output : [[4.8572703e-05 1.8646901e-04 4.1072968e-02 1.0164494e-02 8.8526386e-01
  6.3034691e-02 8.0335820e-05 1.4854108e-04]]
Age : (25-32), conf = 0.885
time : 0.098
Gender : Male, conf = 0.979
Age Output : [[1.21946905e-05 1.27260544e-04 5.32757081e-02 1.81399547e-02
  8.95605922e-01 3.27471420e-02 3.15082070e-05 6.03105800e-05]]
Age : (25-32), conf = 0.896
time : 0.090
Gender : Male, conf = 0.967
Age Output : [[1.9585363e-05 1.0298400e-04 2.2947609e-02 7.3357201e-03 9.1174495e-01
  5.7724461e-02 4.4326203e-05 8.0345417e-05]]
Age : (25-32), conf = 0.912
time : 0.101
Gender : Male, conf = 0.977
Age Output : [[4.6141675e-05 2.3862917e-04 8.1527360e-02 1.9449137e-02 8.4416389e-01
  5.4407448e-02 4.5832789e-05 1.2157443e-04]]
Age : (25-32), conf = 0.844
time : 0.093
Gender : Male, conf = 0.993
Age Output : [[4.2285497e-05 2.7835730e-04 3.7450269e-02 1.3797609e-02 9.0886235e-01
  3.9466184e-02 3.3353517e-05 6.9443013e-05]]
Age : (25-32), conf = 0.909
time : 0.104
Gender : Male, conf = 0.988
Age Output : [[9.5452117e-05 3.8421739e-04 9.0284944e-02 2.5337126e-02 8.4153503e-01
  4.2173289e-02 5.2908472e-05 1.3702360e-04]]
Age : (25-32), conf = 0.842
time : 0.087
Gender : Male, conf = 0.977
Age Output : [[3.3504550e-06 2.2089589e-05 3.1563137e-03 1.8684322e-02 9.4568586e-01
  3.2348435e-02 4.8712653e-05 5.0902388e-05]]
Age : (25-32), conf = 0.946
time : 0.085
Gender : Male, conf = 0.993
Age Output : [[1.7926910e-06 2.1656477e-05 6.9062226e-03 5.8701236e-02 9.2170697e-01
  1.2618060e-02 1.8908186e-05 2.5132398e-05]]
Age : (25-32), conf = 0.922
time : 0.085
Gender : Male, conf = 0.993
Age Output : [[1.7926910e-06 2.1656477e-05 6.9062226e-03 5.8701236e-02 9.2170697e-01
  1.2618060e-02 1.8908186e-05 2.5132398e-05]]
Age : (25-32), conf = 0.922
time : 0.100
Gender : Male, conf = 0.987
Age Output : [[1.7973423e-05 8.2498016e-05 3.8134053e-02 6.7829695e-03 9.0191495e-01
  5.2922912e-02 4.8754653e-05 9.5946089e-05]]
Age : (25-32), conf = 0.902
time : 0.089
Gender : Male, conf = 0.989
Age Output : [[3.1454795e-06 2.0370415e-05 2.3789194e-03 2.0551294e-02 9.5039958e-01
  2.6560808e-02 4.1911022e-05 4.4004679e-05]]
Age : (25-32), conf = 0.950
time : 0.100
Gender : Male, conf = 0.984
Age Output : [[2.0158834e-06 1.8496610e-05 3.3567296e-03 3.1512558e-02 9.4780028e-01
  1.7248161e-02 2.8918570e-05 3.2778971e-05]]
Age : (25-32), conf = 0.948
time : 0.087
Gender : Male, conf = 0.985
Age Output : [[4.81108473e-05 1.30945846e-04 4.43353206e-02 1.31295165e-02
  8.27391326e-01 1.14652105e-01 8.97965292e-05 2.22925722e-04]]
Age : (25-32), conf = 0.827
time : 0.100
Gender : Male, conf = 0.987
Age Output : [[4.7120693e-06 3.7049300e-05 2.9704724e-03 2.1003462e-02 9.5402855e-01
  2.1889882e-02 3.0489437e-05 3.5320401e-05]]
Age : (25-32), conf = 0.954
time : 0.087
Gender : Male, conf = 0.986
Age Output : [[2.62825733e-06 1.36398585e-05 1.28466892e-03 9.98627115e-03
  9.70792353e-01 1.78586375e-02 3.04569239e-05 3.13469245e-05]]
Age : (25-32), conf = 0.971
time : 0.099
Gender : Male, conf = 0.992
Age Output : [[1.5749989e-04 1.0395533e-03 9.6125908e-02 3.0542836e-02 8.3771539e-01
  3.4252133e-02 4.8934427e-05 1.1775053e-04]]
Age : (25-32), conf = 0.838
time : 0.088
Gender : Male, conf = 0.990
Age Output : [[4.9535331e-05 2.7945286e-04 3.1146897e-02 2.1586159e-02 9.0485114e-01
  4.1955363e-02 4.6445421e-05 8.4840918e-05]]
Age : (25-32), conf = 0.905
time : 0.099
Gender : Male, conf = 0.991
Age Output : [[4.9502069e-05 2.0297861e-04 3.2893937e-02 1.0863430e-02 8.8547617e-01
  7.0317484e-02 6.9093199e-05 1.2727758e-04]]
Age : (25-32), conf = 0.885
time : 0.083
Gender : Male, conf = 0.993
Age Output : [[1.9695237e-05 9.5204290e-05 8.6592371e-03 4.5685335e-03 9.5483726e-01
  3.1706218e-02 4.5918918e-05 6.8094159e-05]]
Age : (25-32), conf = 0.955
time : 0.098
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.996
Age Output : [[3.4010361e-04 6.9413874e-03 1.4250150e-01 2.1138249e-02 6.8980503e-01
  1.3895866e-01 1.6783143e-04 1.4721607e-04]]
Age : (25-32), conf = 0.690
time : 0.098
Gender : Male, conf = 0.999
Age Output : [[2.0296979e-03 6.3114323e-02 4.6650141e-01 2.8776849e-02 3.6574787e-01
  7.3611364e-02 7.9907397e-05 1.3855408e-04]]
Age : (8-12), conf = 0.467
time : 0.086
Gender : Male, conf = 1.000
Age Output : [[3.5958798e-04 3.9624446e-03 7.3045804e-03 9.3094381e-03 9.6808237e-01
  1.0748343e-02 7.5284835e-05 1.5799374e-04]]
Age : (25-32), conf = 0.968
time : 0.103
Gender : Male, conf = 1.000
Age Output : [[3.7686997e-03 1.4509118e-02 1.2514507e-02 7.1846028e-03 9.2329502e-01
  3.7440974e-02 5.6834944e-04 7.1876153e-04]]
Age : (25-32), conf = 0.923
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[1.9662652e-02 1.5620914e-01 3.8977571e-02 5.0449600e-03 7.4815857e-01
  3.0524207e-02 6.3969282e-04 7.8324461e-04]]
Age : (25-32), conf = 0.748
time : 0.099
Gender : Male, conf = 1.000
Age Output : [[1.6811509e-02 1.8173468e-01 1.4175218e-01 3.5792389e-03 6.3683665e-01
  1.8677013e-02 2.3751218e-04 3.7117398e-04]]
Age : (25-32), conf = 0.637
time : 0.081
Gender : Male, conf = 1.000
Age Output : [[0.20263436 0.0937774  0.05118191 0.01832042 0.56808513 0.06248605
  0.00062658 0.00288817]]
Age : (25-32), conf = 0.568
time : 0.100
Gender : Male, conf = 1.000
Age Output : [[5.0894335e-02 4.0424369e-02 6.8498157e-02 2.9098550e-02 7.2271538e-01
  8.6456075e-02 3.5787444e-04 1.5552230e-03]]
Age : (25-32), conf = 0.723
time : 0.082
Gender : Male, conf = 1.000
Age Output : [[9.2214540e-02 3.2959852e-01 5.9318986e-02 3.3516411e-02 4.5357415e-01
  3.0125272e-02 2.3868452e-04 1.4135233e-03]]
Age : (25-32), conf = 0.454
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[1.5857511e-03 1.7397581e-02 4.6711525e-01 7.8273028e-02 3.1065810e-01
  1.2330483e-01 2.7944203e-04 1.3860238e-03]]
Age : (8-12), conf = 0.467
time : 0.083
Gender : Male, conf = 0.999
Age Output : [[1.5857511e-03 1.7397581e-02 4.6711525e-01 7.8273028e-02 3.1065810e-01
  1.2330483e-01 2.7944203e-04 1.3860238e-03]]
Age : (8-12), conf = 0.467
time : 0.102
Gender : Male, conf = 0.993
Age Output : [[0.5495122  0.09108166 0.06691286 0.02706347 0.1765878  0.07884366
  0.00087134 0.00912692]]
Age : (0-2), conf = 0.550
time : 0.082
Gender : Male, conf = 0.998
Age Output : [[9.2311913e-01 3.8389586e-02 2.0989757e-02 1.9381862e-03 5.7495125e-03
  5.5700555e-03 2.4316586e-04 4.0005208e-03]]
Age : (0-2), conf = 0.923
time : 0.103
Gender : Male, conf = 0.999
Age Output : [[1.8846624e-02 1.2961414e-01 5.6244868e-01 1.5339153e-01 1.0776019e-01
  2.6640328e-02 2.0465399e-04 1.0938158e-03]]
Age : (8-12), conf = 0.562
time : 0.082
Gender : Male, conf = 0.974
Age Output : [[0.15954511 0.23299067 0.34483096 0.07633597 0.11870337 0.06360818
  0.00035229 0.00363357]]
Age : (8-12), conf = 0.345
time : 0.120
Gender : Male, conf = 0.987
Age Output : [[0.03120838 0.11913702 0.45838436 0.02451177 0.29158103 0.07168099
  0.00066761 0.00282882]]
Age : (8-12), conf = 0.458
time : 0.079
Gender : Male, conf = 0.989
Age Output : [[1.22587666e-01 2.35667661e-01 5.03925085e-01 1.25160953e-02
  9.38782021e-02 2.78338697e-02 2.61394336e-04 3.32998042e-03]]
Age : (8-12), conf = 0.504
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>time : 0.091
Gender : Male, conf = 0.995
Age Output : [[0.06072003 0.07854459 0.10858956 0.04879595 0.64488083 0.0500665
  0.00071483 0.00768776]]
Age : (25-32), conf = 0.645
time : 0.084
Gender : Male, conf = 0.997
Age Output : [[2.6676457e-02 9.4393805e-02 7.2220987e-01 2.1528421e-02 8.3546750e-02
  4.7850605e-02 2.1143524e-04 3.5825637e-03]]
Age : (8-12), conf = 0.722
time : 0.091
Gender : Male, conf = 0.989
Age Output : [[2.6100825e-03 1.2939011e-02 4.8722646e-01 2.2844154e-01 2.0960464e-01
  5.8249284e-02 7.9927500e-05 8.4907893e-04]]
Age : (8-12), conf = 0.487
time : 0.088
Gender : Male, conf = 0.988
Age Output : [[2.0846946e-02 2.7529120e-02 5.2194506e-01 9.8642766e-02 1.8614520e-01
  1.4175035e-01 2.1898106e-04 2.9215622e-03]]
Age : (8-12), conf = 0.522
time : 0.089
Gender : Male, conf = 0.976
Age Output : [[6.8197952e-04 5.0681513e-03 8.5175252e-01 5.6774534e-02 4.6321135e-02
  3.9111570e-02 2.3610301e-05 2.6657493e-04]]
Age : (8-12), conf = 0.852
time : 0.086
Gender : Male, conf = 0.986
Age Output : [[4.5767744e-04 4.0961169e-03 7.8091258e-01 8.0032080e-02 8.9407533e-02
  4.4828147e-02 2.4168732e-05 2.4169739e-04]]
Age : (8-12), conf = 0.781
time : 0.096
Gender : Male, conf = 0.986
Age Output : [[3.7268057e-04 2.8737290e-03 8.7593740e-01 6.9474153e-02 3.3389088e-02
  1.7674634e-02 1.2221672e-05 2.6602930e-04]]
Age : (8-12), conf = 0.876
time : 0.085
Gender : Male, conf = 0.986
Age Output : [[3.7268057e-04 2.8737290e-03 8.7593740e-01 6.9474153e-02 3.3389088e-02
  1.7674634e-02 1.2221672e-05 2.6602930e-04]]
Age : (8-12), conf = 0.876
time : 0.097
Gender : Male, conf = 0.991
Age Output : [[2.4932381e-04 1.7550961e-03 7.8571516e-01 6.5612994e-02 8.6689293e-02
  5.9637271e-02 2.2028347e-05 3.1888857e-04]]
Age : (8-12), conf = 0.786
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[1.1139247e-02 8.0430359e-02 7.8349811e-01 3.5054024e-02 7.1346112e-02
  1.8066924e-02 3.2459440e-05 4.3274544e-04]]
Age : (8-12), conf = 0.783
time : 0.091
Gender : Male, conf = 0.989
Age Output : [[3.2377850e-02 8.0395371e-02 8.1670815e-01 2.1424394e-02 2.3131490e-02
  2.2782546e-02 6.6795612e-05 3.1134081e-03]]
Age : (8-12), conf = 0.817
time : 0.088
Gender : Male, conf = 0.993
Age Output : [[4.6939641e-02 2.3377442e-01 6.8435735e-01 1.6056456e-02 1.5183954e-02
  2.9001425e-03 2.5003435e-05 7.6315610e-04]]
Age : (8-12), conf = 0.684
time : 0.090
Gender : Male, conf = 0.986
Age Output : [[4.5970991e-02 2.7400218e-02 1.8512240e-01 7.0493855e-02 4.2455301e-01
  2.3818600e-01 3.2553609e-04 7.9479776e-03]]
Age : (25-32), conf = 0.425
time : 0.084
Gender : Male, conf = 0.986
Age Output : [[4.5970991e-02 2.7400218e-02 1.8512240e-01 7.0493855e-02 4.2455301e-01
  2.3818600e-01 3.2553609e-04 7.9479776e-03]]
Age : (25-32), conf = 0.425
time : 0.092
Gender : Male, conf = 0.986
Age Output : [[2.7020974e-02 4.9529638e-02 5.3868419e-01 9.2451833e-02 2.1296860e-01
  7.6714955e-02 2.2514084e-04 2.4047440e-03]]
Age : (8-12), conf = 0.539
time : 0.085
Gender : Male, conf = 0.951
Age Output : [[2.3467443e-03 7.6044719e-03 7.0807290e-01 5.5091076e-02 1.5187053e-01
  7.2424725e-02 9.7198499e-05 2.4923591e-03]]
Age : (8-12), conf = 0.708
time : 0.108
Gender : Male, conf = 0.913
Age Output : [[4.2883705e-04 1.0273081e-02 8.7764579e-01 3.5728145e-02 3.9967176e-02
  3.5730939e-02 2.3909712e-05 2.0211461e-04]]
Age : (8-12), conf = 0.878
time : 0.080
Gender : Male, conf = 0.936
Age Output : [[5.9735437e-04 4.8279217e-03 8.4122467e-01 3.7727237e-02 8.2629360e-02
  3.2532208e-02 3.0598894e-05 4.3067508e-04]]
Age : (8-12), conf = 0.841
time : 0.100
Gender : Male, conf = 0.981
Age Output : [[1.4892807e-03 2.7763134e-02 9.2476451e-01 3.0494275e-02 1.1573388e-02
  3.6820897e-03 1.1589275e-05 2.2172078e-04]]
Age : (8-12), conf = 0.925
time : 0.087
Gender : Male, conf = 0.987
Age Output : [[1.0328370e-02 5.3306736e-02 8.9742517e-01 1.6705159e-02 1.3186640e-02
  7.1187387e-03 7.6387958e-05 1.8527629e-03]]
Age : (8-12), conf = 0.897
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[1.5006566e-03 2.7137490e-03 4.3668085e-01 9.2522435e-02 3.1416386e-01
  1.4896072e-01 2.9188296e-04 3.1658737e-03]]
Age : (8-12), conf = 0.437
time : 0.089
Gender : Male, conf = 0.996
Age Output : [[1.5006566e-03 2.7137490e-03 4.3668085e-01 9.2522435e-02 3.1416386e-01
  1.4896072e-01 2.9188296e-04 3.1658737e-03]]
Age : (8-12), conf = 0.437
time : 0.094
Gender : Male, conf = 0.998
Age Output : [[4.8018536e-03 8.7110009e-03 7.8643930e-01 5.4975759e-02 6.8406373e-02
  7.2162770e-02 1.9665247e-04 4.3062703e-03]]
Age : (8-12), conf = 0.786
time : 0.090
Gender : Male, conf = 0.997
Age Output : [[3.4110479e-03 1.6362339e-02 8.6147147e-01 3.3821415e-02 5.7622239e-02
  2.5497921e-02 1.1622973e-04 1.6972263e-03]]
Age : (8-12), conf = 0.861
time : 0.094
No face Detected, Checking next frame
Gender : Male, conf = 0.964
Age Output : [[5.2724164e-03 2.6505485e-02 7.1947140e-01 4.6537455e-02 1.3270974e-01
  6.7064308e-02 1.3312711e-04 2.3061573e-03]]
Age : (8-12), conf = 0.719
time : 0.092
Gender : Male, conf = 0.968
Age Output : [[1.70948973e-03 4.30289656e-03 3.66111010e-01 2.35856861e-01
  2.78231502e-01 1.11467585e-01 1.73961336e-04 2.14667502e-03]]
Age : (8-12), conf = 0.366
time : 0.093
Gender : Male, conf = 0.968
Age Output : [[1.70948973e-03 4.30289656e-03 3.66111010e-01 2.35856861e-01
  2.78231502e-01 1.11467585e-01 1.73961336e-04 2.14667502e-03]]
Age : (8-12), conf = 0.366
time : 0.085
Gender : Male, conf = 0.985
Age Output : [[8.1480466e-05 2.0957724e-03 8.1749785e-01 5.1262192e-02 8.8659875e-02
  4.0218465e-02 2.6827851e-05 1.5757080e-04]]
Age : (8-12), conf = 0.817
time : 0.102
Gender : Male, conf = 0.995
Age Output : [[4.2308201e-03 4.1210772e-03 9.2653550e-02 1.6890411e-01 4.8391458e-01
  2.4070263e-01 3.2045454e-04 5.1527009e-03]]
Age : (25-32), conf = 0.484
time : 0.102
Gender : Male, conf = 0.993
Age Output : [[6.9137115e-04 6.8847327e-03 3.2675868e-01 8.1901379e-02 5.6370711e-01
  1.9581798e-02 8.9118425e-05 3.8578891e-04]]
Age : (25-32), conf = 0.564
time : 0.101
Gender : Male, conf = 0.992
Age Output : [[2.7180724e-03 2.6138209e-02 4.7942820e-01 2.6442155e-02 4.3420690e-01
  3.0548187e-02 1.9977039e-04 3.1854596e-04]]
Age : (8-12), conf = 0.479
time : 0.094
Gender : Male, conf = 0.986
Age Output : [[0.02957033 0.12489606 0.43128967 0.03187104 0.30509835 0.0762053
  0.00045418 0.00061513]]
Age : (8-12), conf = 0.431
time : 0.102
Gender : Male, conf = 0.998
Age Output : [[0.04633554 0.04011748 0.03649345 0.01666554 0.7153254  0.14213386
  0.00171471 0.00121413]]
Age : (25-32), conf = 0.715
time : 0.092
Gender : Male, conf = 0.999
Age Output : [[6.8640348e-04 4.2290413e-03 2.6207939e-02 9.9354610e-03 8.8740301e-01
  7.0965268e-02 3.6968137e-04 2.0307449e-04]]
Age : (25-32), conf = 0.887
time : 0.107
Gender : Male, conf = 0.999
Age Output : [[1.5617235e-03 7.6003997e-03 1.7347613e-02 1.4317192e-02 8.4185821e-01
  1.1607008e-01 7.7894056e-04 4.6573585e-04]]
Age : (25-32), conf = 0.842
time : 0.090
Gender : Male, conf = 1.000
Age Output : [[5.5072647e-05 3.1216495e-04 1.4370334e-02 1.4692188e-02 8.8103932e-01
  8.9203447e-02 1.2452058e-04 2.0293848e-04]]
Age : (25-32), conf = 0.881
time : 0.099
Gender : Male, conf = 0.999
Age Output : [[0.00106338 0.00211238 0.0051657  0.00583387 0.69788325 0.28560185
  0.00147017 0.00086937]]
Age : (25-32), conf = 0.698
time : 0.092
Gender : Male, conf = 0.999
Age Output : [[0.00106338 0.00211238 0.0051657  0.00583387 0.69788325 0.28560185
  0.00147017 0.00086937]]
Age : (25-32), conf = 0.698
time : 0.102
Gender : Male, conf = 0.998
Age Output : [[0.0055898  0.0100749  0.03720583 0.02897405 0.75464994 0.1613311
  0.00079649 0.00137781]]
Age : (25-32), conf = 0.755
time : 0.078
Gender : Male, conf = 0.999
Age Output : [[0.03990714 0.1492803  0.41249305 0.05207648 0.21984632 0.12395941
  0.00052566 0.00191167]]
Age : (8-12), conf = 0.412
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[7.3656470e-02 6.7412329e-01 6.8031169e-02 2.4589233e-02 1.4760798e-01
  1.0637035e-02 4.6936687e-04 8.8553800e-04]]
Age : (4-6), conf = 0.674
time : 0.089
Gender : Male, conf = 1.000
Age Output : [[1.8495321e-02 3.8036594e-01 2.4433094e-01 5.1812612e-02 2.8069308e-01
  2.2886634e-02 3.0621301e-04 1.1091577e-03]]
Age : (4-6), conf = 0.380
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[3.4083347e-03 5.0641984e-02 4.2673331e-02 4.6135746e-02 8.3121449e-01
  2.4492763e-02 4.0996080e-04 1.0234331e-03]]
Age : (25-32), conf = 0.831
time : 0.083
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.999
Age Output : [[1.9304793e-02 5.6987233e-02 5.5666995e-01 4.5535304e-02 2.7556583e-01
  4.4042360e-02 3.2303095e-04 1.5715034e-03]]
Age : (8-12), conf = 0.557
time : 0.101
Gender : Male, conf = 0.998
Age Output : [[2.5391236e-03 2.2491068e-02 5.7913303e-01 5.8289897e-02 2.9883912e-01
  3.8191866e-02 1.1401004e-04 4.0189366e-04]]
Age : (8-12), conf = 0.579
time : 0.085
Gender : Male, conf = 0.998
Age Output : [[2.5391236e-03 2.2491068e-02 5.7913303e-01 5.8289897e-02 2.9883912e-01
  3.8191866e-02 1.1401004e-04 4.0189366e-04]]
Age : (8-12), conf = 0.579
time : 0.100
Gender : Male, conf = 0.998
Age Output : [[9.3246938e-04 5.3170468e-03 4.8279208e-01 3.3473760e-02 3.9400074e-01
  8.2649536e-02 1.2450057e-04 7.0986722e-04]]
Age : (8-12), conf = 0.483
time : 0.088
Gender : Male, conf = 0.999
Age Output : [[3.2722359e-03 1.9978825e-02 3.3221585e-01 4.5666836e-02 5.0797665e-01
  8.9790091e-02 2.9084002e-04 8.0865400e-04]]
Age : (25-32), conf = 0.508
time : 0.100
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.996
Age Output : [[2.2172544e-03 5.4552394e-01 2.1519989e-01 4.9665542e-03 2.0746131e-01
  2.3223870e-02 1.1488470e-03 2.5844760e-04]]
Age : (4-6), conf = 0.546
time : 0.094
Gender : Female, conf = 0.997
Age Output : [[0.00181337 0.25310844 0.26469395 0.00428219 0.42848593 0.04313753
  0.00397381 0.00050473]]
Age : (25-32), conf = 0.428
time : 0.081
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.875
Age Output : [[0.0095396  0.62018603 0.21515097 0.07594714 0.04782598 0.02877004
  0.00121324 0.00136709]]
Age : (4-6), conf = 0.620
time : 0.100
No face Detected, Checking next frame
Gender : Female, conf = 0.925
Age Output : [[0.01023176 0.37442502 0.32582825 0.12979311 0.07964271 0.07599609
  0.00152528 0.00255787]]
Age : (4-6), conf = 0.374
time : 0.100
Gender : Female, conf = 0.916
Age Output : [[6.2623238e-03 2.2556436e-01 5.8681381e-01 9.0176135e-02 5.3266287e-02
  3.6238477e-02 5.1204552e-04 1.1665528e-03]]
Age : (8-12), conf = 0.587
time : 0.119
Gender : Female, conf = 0.758
Age Output : [[0.00754506 0.29285347 0.4012956  0.11086271 0.15488483 0.02945415
  0.00091362 0.00219048]]
Age : (8-12), conf = 0.401
time : 0.122
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.510
Age Output : [[6.1118826e-03 9.4946957e-01 3.2756746e-02 4.6590343e-03 3.9765583e-03
  1.2309058e-03 1.4482494e-03 3.4708597e-04]]
Age : (4-6), conf = 0.949
time : 0.101
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.972
Age Output : [[1.9799547e-04 6.1955990e-04 1.0458699e-03 8.5013825e-03 8.7261492e-01
  1.1410898e-01 1.8756260e-03 1.0355894e-03]]
Age : (25-32), conf = 0.873
time : 0.090
Gender : Male, conf = 0.972
Age Output : [[0.00113106 0.0039975  0.00619751 0.06596293 0.45977128 0.45089355
  0.00926012 0.00278609]]
Age : (25-32), conf = 0.460
time : 0.085
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.955
Age Output : [[0.00100144 0.00357055 0.00492409 0.04737709 0.4445802  0.4879835
  0.00823408 0.00232908]]
Age : (38-43), conf = 0.488
time : 0.100
Gender : Male, conf = 0.973
Age Output : [[0.00197611 0.00681632 0.00556489 0.04650061 0.57646054 0.3448644
  0.01406517 0.00375197]]
Age : (25-32), conf = 0.576
time : 0.102
Gender : Male, conf = 0.973
Age Output : [[4.5581558e-04 1.7101618e-03 2.7407156e-03 2.3666298e-02 7.3851210e-01
  2.2762400e-01 3.3837867e-03 1.9070669e-03]]
Age : (25-32), conf = 0.739
time : 0.102
Gender : Male, conf = 0.971
Age Output : [[1.5485354e-04 5.9032702e-04 1.6694322e-03 2.1054959e-02 7.9256368e-01
  1.8083099e-01 2.0186189e-03 1.1172371e-03]]
Age : (25-32), conf = 0.793
time : 0.092
Gender : Male, conf = 0.957
Age Output : [[6.2590589e-05 2.2637795e-04 7.6072186e-04 9.8045692e-03 8.1340468e-01
  1.7389350e-01 1.0300889e-03 8.1750640e-04]]
Age : (25-32), conf = 0.813
time : 0.101
Gender : Male, conf = 0.985
Age Output : [[7.2636700e-05 3.4841313e-04 1.8739243e-03 2.3492109e-02 8.0204600e-01
  1.7019567e-01 1.1410515e-03 8.3028694e-04]]
Age : (25-32), conf = 0.802
time : 0.084
Gender : Male, conf = 0.985
Age Output : [[7.2636700e-05 3.4841313e-04 1.8739243e-03 2.3492109e-02 8.0204600e-01
  1.7019567e-01 1.1410515e-03 8.3028694e-04]]
Age : (25-32), conf = 0.802
time : 0.101
Gender : Male, conf = 0.979
Age Output : [[1.3290139e-05 4.5605906e-05 3.1462696e-04 5.9262025e-03 8.7507802e-01
  1.1794877e-01 3.0925308e-04 3.6412806e-04]]
Age : (25-32), conf = 0.875
time : 0.091
Gender : Male, conf = 0.973
Age Output : [[6.6792294e-05 1.8237437e-04 6.7521678e-04 2.0841625e-02 7.8447747e-01
  1.9147763e-01 1.2717651e-03 1.0071477e-03]]
Age : (25-32), conf = 0.784
time : 0.103
Gender : Male, conf = 0.993
Age Output : [[1.05248604e-04 2.93577672e-04 7.86278106e-04 2.77243741e-02
  7.36455023e-01 2.31172830e-01 1.99536304e-03 1.46728510e-03]]
Age : (25-32), conf = 0.736
time : 0.086
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.603
Age Output : [[0.18301451 0.3408941  0.05759341 0.04862742 0.2374355  0.1268064
  0.00212113 0.00350751]]
Age : (4-6), conf = 0.341
time : 0.087
No face Detected, Checking next frame
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>No face Detected, Checking next frame
Gender : Male, conf = 0.995
Age Output : [[8.5289357e-03 1.4085746e-02 8.4514963e-03 2.7220210e-02 8.7530947e-01
  6.5308996e-02 4.0725333e-04 6.8779179e-04]]
Age : (25-32), conf = 0.875
time : 0.084
Gender : Male, conf = 0.992
Age Output : [[3.8757543e-03 7.8878300e-03 8.4547438e-03 2.7302913e-02 9.0308338e-01
  4.8613846e-02 1.9854015e-04 5.8292295e-04]]
Age : (25-32), conf = 0.903
time : 0.085
Gender : Male, conf = 0.958
Age Output : [[1.5647883e-04 4.0912634e-04 1.5176263e-03 7.7925576e-03 9.7972578e-01
  1.0221418e-02 5.5957669e-05 1.2111503e-04]]
Age : (25-32), conf = 0.980
time : 0.085
Gender : Male, conf = 0.958
Age Output : [[1.5647883e-04 4.0912634e-04 1.5176263e-03 7.7925576e-03 9.7972578e-01
  1.0221418e-02 5.5957669e-05 1.2111503e-04]]
Age : (25-32), conf = 0.980
time : 0.101
Gender : Male, conf = 0.997
Age Output : [[6.4877812e-03 1.5157062e-01 1.4181818e-02 2.1121800e-02 7.9471886e-01
  1.1288727e-02 3.0918443e-04 3.2125652e-04]]
Age : (25-32), conf = 0.795
time : 0.088
Gender : Male, conf = 0.998
Age Output : [[1.6094871e-03 3.3815417e-02 7.5217485e-03 1.1799665e-02 9.3753833e-01
  7.3722522e-03 1.5731866e-04 1.8579091e-04]]
Age : (25-32), conf = 0.938
time : 0.110
Gender : Male, conf = 0.997
Age Output : [[3.8319841e-04 6.2466864e-03 2.7632092e-03 1.0871815e-02 9.7326434e-01
  6.2065092e-03 1.1082446e-04 1.5349976e-04]]
Age : (25-32), conf = 0.973
time : 0.079
Gender : Male, conf = 0.997
Age Output : [[5.6807621e-04 6.1111548e-03 4.0792702e-03 8.1267180e-03 9.6750915e-01
  1.3271260e-02 1.2461934e-04 2.0974224e-04]]
Age : (25-32), conf = 0.968
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[0.03074362 0.14248797 0.01834947 0.01558417 0.76145905 0.02940876
  0.00107318 0.00089381]]
Age : (25-32), conf = 0.761
time : 0.087
Gender : Male, conf = 0.999
Age Output : [[0.01860306 0.0540003  0.01400157 0.01386448 0.8509847  0.04663515
  0.00099911 0.00091159]]
Age : (25-32), conf = 0.851
time : 0.098
Gender : Male, conf = 0.991
Age Output : [[2.8785053e-03 4.3610446e-03 1.8264604e-03 4.5497939e-03 9.4174945e-01
  4.2928725e-02 7.3551974e-04 9.7057450e-04]]
Age : (25-32), conf = 0.942
time : 0.092
Gender : Male, conf = 0.991
Age Output : [[2.8785053e-03 4.3610446e-03 1.8264604e-03 4.5497939e-03 9.4174945e-01
  4.2928725e-02 7.3551974e-04 9.7057450e-04]]
Age : (25-32), conf = 0.942
time : 0.101
Gender : Male, conf = 0.997
Age Output : [[0.04358033 0.01550821 0.00555511 0.00902136 0.8193567  0.10153827
  0.00309262 0.00234741]]
Age : (25-32), conf = 0.819
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[0.36620855 0.16763139 0.03628962 0.02191182 0.21208829 0.17235285
  0.01741419 0.00610326]]
Age : (0-2), conf = 0.366
time : 0.085
Gender : Male, conf = 0.994
Age Output : [[0.01953736 0.14194258 0.0221556  0.01320487 0.5778276  0.19449975
  0.02486752 0.00596471]]
Age : (25-32), conf = 0.578
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[0.0032401  0.10304461 0.02045773 0.07477897 0.70882124 0.08602028
  0.00245147 0.00118563]]
Age : (25-32), conf = 0.709
time : 0.099
Gender : Male, conf = 0.998
Age Output : [[0.009009   0.24156661 0.02606281 0.11117201 0.5033795  0.10317884
  0.00410677 0.0015244 ]]
Age : (25-32), conf = 0.503
time : 0.096
Gender : Male, conf = 0.999
Age Output : [[3.9579070e-04 7.8724138e-03 3.5255377e-03 4.6749342e-02 9.0035009e-01
  4.0015612e-02 6.6761038e-04 4.2367092e-04]]
Age : (25-32), conf = 0.900
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[1.3853729e-03 5.2925799e-02 1.2136690e-02 2.0571331e-02 8.3972931e-01
  7.2328709e-02 5.1135226e-04 4.1141949e-04]]
Age : (25-32), conf = 0.840
time : 0.094
Gender : Male, conf = 0.999
Age Output : [[1.8404996e-03 6.2783554e-02 1.1470313e-02 2.2065511e-02 8.4216785e-01
  5.8433626e-02 7.5016863e-04 4.8848678e-04]]
Age : (25-32), conf = 0.842
time : 0.117
Gender : Male, conf = 0.998
Age Output : [[3.72917537e-04 1.26654599e-02 7.10788183e-03 9.58680082e-03
  9.53574240e-01 1.63243767e-02 1.16981624e-04 2.51373742e-04]]
Age : (25-32), conf = 0.954
time : 0.099
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.965
Age Output : [[4.4470453e-03 3.6744627e-01 5.9948069e-01 2.0165578e-03 2.5418526e-02
  9.0719457e-04 6.9399779e-05 2.1429709e-04]]
Age : (8-12), conf = 0.599
time : 0.083
Gender : Male, conf = 0.981
Age Output : [[7.7509754e-03 5.2943558e-01 4.4051102e-01 1.7957375e-03 1.9217376e-02
  8.7129395e-04 6.9364920e-05 3.4869200e-04]]
Age : (4-6), conf = 0.529
time : 0.103
Gender : Male, conf = 0.950
Age Output : [[7.9729146e-04 1.8760160e-01 7.9458511e-01 5.2300566e-03 1.1177193e-02
  4.9452699e-04 2.1932321e-05 9.2255344e-05]]
Age : (8-12), conf = 0.795
time : 0.083
Gender : Male, conf = 0.937
Age Output : [[6.9662295e-03 9.1519123e-01 7.7068962e-02 4.1887217e-04 2.7874816e-04
  5.2555704e-05 4.5742850e-06 1.8924044e-05]]
Age : (4-6), conf = 0.915
time : 0.100
No face Detected, Checking next frame
Gender : Male, conf = 0.989
Age Output : [[8.7420356e-01 1.2474869e-01 7.3149189e-04 2.5343374e-05 2.4447503e-04
  2.3520564e-05 8.1329099e-06 1.4766427e-05]]
Age : (0-2), conf = 0.874
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[8.8306260e-01 1.1117237e-01 1.5793245e-03 8.6488806e-05 3.8608764e-03
  1.6413757e-04 3.3309381e-05 4.0916926e-05]]
Age : (0-2), conf = 0.883
time : 0.086
Gender : Male, conf = 0.998
Age Output : [[8.8306260e-01 1.1117237e-01 1.5793245e-03 8.6488806e-05 3.8608764e-03
  1.6413757e-04 3.3309381e-05 4.0916926e-05]]
Age : (0-2), conf = 0.883
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[3.6897421e-01 6.0207856e-01 8.5091256e-03 5.9221213e-04 1.9199071e-02
  5.3662132e-04 5.4618966e-05 5.5522651e-05]]
Age : (4-6), conf = 0.602
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[3.6897421e-01 6.0207856e-01 8.5091256e-03 5.9221213e-04 1.9199071e-02
  5.3662132e-04 5.4618966e-05 5.5522651e-05]]
Age : (4-6), conf = 0.602
time : 0.081
Gender : Male, conf = 0.998
Age Output : [[1.7610641e-01 3.9098817e-01 3.7441749e-02 2.7723543e-03 3.8695142e-01
  5.2327053e-03 2.2465162e-04 2.8243355e-04]]
Age : (4-6), conf = 0.391
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[5.1442677e-01 3.9595318e-01 1.5599850e-02 9.5973426e-04 7.0895255e-02
  1.9175410e-03 1.0324345e-04 1.4442788e-04]]
Age : (0-2), conf = 0.514
time : 0.085
Gender : Male, conf = 0.996
Age Output : [[4.4528976e-01 2.9084867e-01 2.6751103e-02 1.7343081e-03 2.2876897e-01
  5.9160884e-03 2.8456489e-04 4.0657559e-04]]
Age : (0-2), conf = 0.445
time : 0.085
Gender : Male, conf = 0.996
Age Output : [[4.4528976e-01 2.9084867e-01 2.6751103e-02 1.7343081e-03 2.2876897e-01
  5.9160884e-03 2.8456489e-04 4.0657559e-04]]
Age : (0-2), conf = 0.445
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[3.9036152e-01 2.8562239e-01 2.2521669e-02 2.0087718e-03 2.9163602e-01
  7.1297362e-03 3.4410006e-04 3.7584777e-04]]
Age : (0-2), conf = 0.390
time : 0.099
Gender : Male, conf = 0.998
Age Output : [[7.4966371e-01 1.6445933e-01 6.2093288e-03 1.0665004e-03 7.7086255e-02
  1.2752055e-03 1.1550176e-04 1.2422199e-04]]
Age : (0-2), conf = 0.750
time : 0.083
Gender : Male, conf = 0.994
Age Output : [[1.4384829e-03 2.3526710e-03 1.7098198e-03 3.0976047e-03 9.8888868e-01
  2.4051843e-03 5.6625719e-05 5.0895218e-05]]
Age : (25-32), conf = 0.989
time : 0.101
Gender : Male, conf = 0.998
Age Output : [[8.1075355e-02 4.2740386e-02 7.8605162e-03 7.1767527e-03 8.5524863e-01
  5.4120971e-03 2.0376808e-04 2.8243547e-04]]
Age : (25-32), conf = 0.855
time : 0.099
Gender : Male, conf = 0.999
Age Output : [[8.4951270e-01 1.0727307e-01 3.5570702e-03 1.2229464e-03 3.6645941e-02
  1.5071626e-03 1.1648904e-04 1.6468436e-04]]
Age : (0-2), conf = 0.850
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[8.4951270e-01 1.0727307e-01 3.5570702e-03 1.2229464e-03 3.6645941e-02
  1.5071626e-03 1.1648904e-04 1.6468436e-04]]
Age : (0-2), conf = 0.850
time : 0.079
Gender : Male, conf = 0.999
Age Output : [[3.5990365e-02 2.0591509e-02 7.3825056e-03 6.4442591e-03 9.1811776e-01
  1.0519720e-02 3.7078912e-04 5.8299792e-04]]
Age : (25-32), conf = 0.918
time : 0.085
Gender : Male, conf = 0.998
Age Output : [[2.3683328e-02 1.4563061e-02 1.1355388e-02 1.0619061e-02 9.2100435e-01
  1.8072050e-02 2.8969289e-04 4.1299660e-04]]
Age : (25-32), conf = 0.921
time : 0.085
Gender : Male, conf = 0.998
Age Output : [[1.5370217e-01 3.2000910e-02 5.1824455e-03 6.4369938e-03 7.8656632e-01
  1.5019857e-02 4.4196763e-04 6.4928952e-04]]
Age : (25-32), conf = 0.787
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>time : 0.084
Gender : Male, conf = 0.999
Age Output : [[8.2864491e-03 6.6569932e-03 7.3380517e-03 7.5924573e-03 9.5354760e-01
  1.6190099e-02 1.5655645e-04 2.3175060e-04]]
Age : (25-32), conf = 0.954
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[1.6246267e-03 2.7454761e-03 5.3261630e-03 1.2143386e-02 9.5991027e-01
  1.8027654e-02 8.4923551e-05 1.3740089e-04]]
Age : (25-32), conf = 0.960
time : 0.097
Gender : Male, conf = 0.998
Age Output : [[6.1025377e-04 1.0907028e-03 5.8687082e-03 1.0363470e-02 9.4650596e-01
  3.5366487e-02 8.2080980e-05 1.1233466e-04]]
Age : (25-32), conf = 0.947
time : 0.092
Gender : Male, conf = 0.998
Age Output : [[6.1025377e-04 1.0907028e-03 5.8687082e-03 1.0363470e-02 9.4650596e-01
  3.5366487e-02 8.2080980e-05 1.1233466e-04]]
Age : (25-32), conf = 0.947
time : 0.099
Gender : Male, conf = 0.996
Age Output : [[2.01477529e-03 1.98428659e-03 7.62242172e-03 5.80610754e-03
  9.60622907e-01 2.16964688e-02 1.08258995e-04 1.44764490e-04]]
Age : (25-32), conf = 0.961
time : 0.083
Gender : Male, conf = 0.998
Age Output : [[4.4157434e-02 2.6312541e-02 3.0103795e-02 1.0608393e-02 8.5774142e-01
  3.0016690e-02 2.9887317e-04 7.6086336e-04]]
Age : (25-32), conf = 0.858
time : 0.097
Gender : Male, conf = 0.999
Age Output : [[4.6090335e-02 8.0672480e-02 2.7384968e-02 8.7262178e-03 8.1757987e-01
  1.8495085e-02 3.3332969e-04 7.1771891e-04]]
Age : (25-32), conf = 0.818
time : 0.087
Gender : Male, conf = 0.999
Age Output : [[2.4151437e-02 7.7800169e-03 8.4918747e-03 8.3325393e-03 8.8110697e-01
  6.4749345e-02 6.0060143e-04 4.7872043e-03]]
Age : (25-32), conf = 0.881
time : 0.097
Gender : Male, conf = 0.999
Age Output : [[0.20416784 0.01970005 0.01457577 0.0167558  0.43963677 0.26439244
  0.00197289 0.03879843]]
Age : (25-32), conf = 0.440
time : 0.077
Gender : Male, conf = 0.998
Age Output : [[3.7592266e-02 3.9683776e-03 6.6965362e-03 3.6895266e-03 8.9561850e-01
  4.8435166e-02 2.7718427e-04 3.7225282e-03]]
Age : (25-32), conf = 0.896
time : 0.099
Gender : Male, conf = 0.999
Age Output : [[4.9853344e-03 2.9597117e-03 8.9074234e-03 3.3099749e-03 9.6519667e-01
  1.3911017e-02 6.5966604e-05 6.6386501e-04]]
Age : (25-32), conf = 0.965
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[4.9853344e-03 2.9597117e-03 8.9074234e-03 3.3099749e-03 9.6519667e-01
  1.3911017e-02 6.5966604e-05 6.6386501e-04]]
Age : (25-32), conf = 0.965
time : 0.099
Gender : Male, conf = 0.997
Age Output : [[3.0812181e-03 8.2063035e-04 6.0411613e-03 3.4942375e-03 9.2993605e-01
  5.3257395e-02 2.2531778e-04 3.1440235e-03]]
Age : (25-32), conf = 0.930
time : 0.082
Gender : Male, conf = 0.996
Age Output : [[0.0568601  0.00321024 0.00982608 0.00643326 0.74181324 0.15372033
  0.00127719 0.02685951]]
Age : (25-32), conf = 0.742
time : 0.100
Gender : Male, conf = 0.997
Age Output : [[1.0358031e-02 2.6189443e-03 1.4863060e-02 7.4223862e-03 9.0183717e-01
  5.9949663e-02 3.2617897e-04 2.6245259e-03]]
Age : (25-32), conf = 0.902
time : 0.092
Gender : Male, conf = 0.996
Age Output : [[1.0340221e-02 1.3044905e-02 3.9445054e-02 2.6608381e-02 8.9271623e-01
  1.7189370e-02 1.9353209e-04 4.6213833e-04]]
Age : (25-32), conf = 0.893
time : 0.097
Gender : Male, conf = 0.989
Age Output : [[9.9631757e-02 2.3691805e-02 4.7353499e-02 3.3168349e-02 7.5682443e-01
  3.7596013e-02 4.6843142e-04 1.2656624e-03]]
Age : (25-32), conf = 0.757
time : 0.089
Gender : Male, conf = 0.998
Age Output : [[6.8465815e-05 6.2303978e-04 7.0982482e-03 3.4115694e-02 9.2836607e-01
  2.9586913e-02 5.1702496e-05 8.9903719e-05]]
Age : (25-32), conf = 0.928
time : 0.103
Gender : Male, conf = 0.999
Age Output : [[4.22362937e-05 2.92276032e-04 1.44543918e-02 2.24700451e-01
  6.34734094e-01 1.25456542e-01 1.07016975e-04 2.12994782e-04]]
Age : (25-32), conf = 0.635
time : 0.090
Gender : Male, conf = 0.996
Age Output : [[3.2453077e-05 3.0547340e-04 8.5602300e-03 5.8942623e-02 9.0503818e-01
  2.7005723e-02 4.2772263e-05 7.2629475e-05]]
Age : (25-32), conf = 0.905
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[3.2453077e-05 3.0547340e-04 8.5602300e-03 5.8942623e-02 9.0503818e-01
  2.7005723e-02 4.2772263e-05 7.2629475e-05]]
Age : (25-32), conf = 0.905
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[1.7282133e-06 1.7304439e-05 1.5288703e-03 6.7988262e-03 9.7278702e-01
  1.8820006e-02 1.8771167e-05 2.7431492e-05]]
Age : (25-32), conf = 0.973
time : 0.103
Gender : Male, conf = 0.998
Age Output : [[1.0546522e-05 1.5499242e-04 8.4005212e-03 3.8579181e-02 9.2839277e-01
  2.4374034e-02 3.3257656e-05 5.4575827e-05]]
Age : (25-32), conf = 0.928
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[1.7982676e-06 1.4851947e-05 1.4096365e-03 1.1450650e-02 9.7927183e-01
  7.8190928e-03 1.0951014e-05 2.1074915e-05]]
Age : (25-32), conf = 0.979
time : 0.102
Gender : Male, conf = 0.996
Age Output : [[7.5187984e-07 3.3532140e-06 7.0637977e-04 6.4642173e-03 9.8686206e-01
  5.9380042e-03 4.7429949e-06 2.0493910e-05]]
Age : (25-32), conf = 0.987
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[3.9512747e-06 2.5880727e-05 1.7672461e-02 7.1434565e-02 8.9200646e-01
  1.8772358e-02 1.0933838e-05 7.3408322e-05]]
Age : (25-32), conf = 0.892
time : 0.101
Gender : Male, conf = 0.997
Age Output : [[3.0896588e-06 6.4088708e-05 9.0114791e-03 1.1260720e-02 9.6917278e-01
  1.0431783e-02 1.8254259e-05 3.7796010e-05]]
Age : (25-32), conf = 0.969
time : 0.086
Gender : Male, conf = 0.994
Age Output : [[8.3627474e-06 9.4086463e-05 1.1568923e-02 3.6523242e-02 9.0272641e-01
  4.8941214e-02 4.4520635e-05 9.3174080e-05]]
Age : (25-32), conf = 0.903
time : 0.107
Gender : Male, conf = 0.994
Age Output : [[8.3627474e-06 9.4086463e-05 1.1568923e-02 3.6523242e-02 9.0272641e-01
  4.8941214e-02 4.4520635e-05 9.3174080e-05]]
Age : (25-32), conf = 0.903
time : 0.079
Gender : Male, conf = 0.998
Age Output : [[2.7387081e-05 3.2433344e-04 1.1568667e-02 3.7882768e-02 8.9261991e-01
  5.7369038e-02 7.0268907e-05 1.3768510e-04]]
Age : (25-32), conf = 0.893
time : 0.101
Gender : Male, conf = 0.997
Age Output : [[1.8879868e-05 1.7198246e-04 6.3019418e-03 5.3624094e-02 8.7120163e-01
  6.8526953e-02 5.9223425e-05 9.5314637e-05]]
Age : (25-32), conf = 0.871
time : 0.082
Gender : Male, conf = 0.998
Age Output : [[4.3184227e-06 3.3674933e-05 1.0043384e-02 1.8347833e-02 8.1646872e-01
  1.5497054e-01 5.5750264e-05 7.5693926e-05]]
Age : (25-32), conf = 0.816
time : 0.121
Gender : Male, conf = 0.999
Age Output : [[6.8007685e-06 9.6783522e-05 6.8570431e-03 1.5865603e-02 9.3318468e-01
  4.3892004e-02 4.4859655e-05 5.2289030e-05]]
Age : (25-32), conf = 0.933
time : 0.137
Gender : Male, conf = 0.997
Age Output : [[2.2089103e-05 1.7108192e-04 1.0395013e-02 4.4464786e-02 8.5583526e-01
  8.8918291e-02 4.6750323e-05 1.4668482e-04]]
Age : (25-32), conf = 0.856
time : 0.137
Gender : Male, conf = 0.999
Age Output : [[5.6943836e-06 8.7697430e-05 1.4000432e-02 2.7308617e-02 9.1070366e-01
  4.7795072e-02 3.8492024e-05 6.0297305e-05]]
Age : (25-32), conf = 0.911
time : 0.155
Gender : Male, conf = 0.997
Age Output : [[8.9825016e-06 2.8873488e-05 3.0969512e-03 8.2645202e-03 9.7654575e-01
  1.2003781e-02 1.4536888e-05 3.6700563e-05]]
Age : (25-32), conf = 0.977
time : 0.126
Gender : Male, conf = 0.999
Age Output : [[1.1477823e-03 1.3337713e-03 1.0206193e-02 1.2398029e-02 9.5042902e-01
  2.4135264e-02 1.3047924e-04 2.1948235e-04]]
Age : (25-32), conf = 0.950
time : 0.171
Gender : Male, conf = 0.998
Age Output : [[2.8178765e-04 8.1976491e-04 2.6407971e-03 1.3653020e-02 9.7086942e-01
  1.1581243e-02 5.7937104e-05 9.6007454e-05]]
Age : (25-32), conf = 0.971
time : 0.200
Gender : Male, conf = 0.999
Age Output : [[1.6067801e-05 1.0112860e-04 1.8253449e-03 7.5799294e-02 9.0204477e-01
  2.0123046e-02 3.0014535e-05 6.0324943e-05]]
Age : (25-32), conf = 0.902
time : 0.168
Gender : Male, conf = 0.998
Age Output : [[7.4134339e-05 2.1320157e-04 4.9240119e-03 1.3688438e-01 8.1215757e-01
  4.5489669e-02 7.0930582e-05 1.8608882e-04]]
Age : (25-32), conf = 0.812
time : 0.107
Gender : Male, conf = 0.999
Age Output : [[3.1977244e-05 6.8262183e-05 3.0176635e-03 3.6683820e-02 8.6886048e-01
  9.1070876e-02 5.5515440e-05 2.1137776e-04]]
Age : (25-32), conf = 0.869
time : 0.107
Gender : Male, conf = 0.999
Age Output : [[2.73188925e-05 7.37994415e-05 2.70877965e-03 1.53178405e-02
  9.29653764e-01 5.20277619e-02 4.84665106e-05 1.42311430e-04]]
Age : (25-32), conf = 0.930
time : 0.088
Gender : Male, conf = 0.999
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[2.4763422e-05 6.2010695e-05 2.0061501e-03 1.8341003e-02 9.4862568e-01
  3.0774700e-02 3.1102438e-05 1.3454955e-04]]
Age : (25-32), conf = 0.949
time : 0.108
Gender : Male, conf = 0.996
Age Output : [[2.1151402e-05 4.5078552e-05 1.3974984e-03 2.0295316e-02 9.0735769e-01
  7.0615858e-02 6.2492931e-05 2.0497483e-04]]
Age : (25-32), conf = 0.907
time : 0.088
Gender : Male, conf = 0.995
Age Output : [[7.8575786e-06 1.3374454e-05 8.9463580e-04 2.9597782e-02 9.0692437e-01
  6.2378675e-02 4.4359411e-05 1.3899073e-04]]
Age : (25-32), conf = 0.907
time : 0.100
Gender : Male, conf = 0.997
Age Output : [[1.0968388e-05 2.7733180e-05 1.9209865e-03 3.4120604e-02 9.0369427e-01
  6.0032096e-02 4.8504760e-05 1.4489994e-04]]
Age : (25-32), conf = 0.904
time : 0.093
Gender : Male, conf = 0.997
Age Output : [[1.0968388e-05 2.7733180e-05 1.9209865e-03 3.4120604e-02 9.0369427e-01
  6.0032096e-02 4.8504760e-05 1.4489994e-04]]
Age : (25-32), conf = 0.904
time : 0.107
Gender : Male, conf = 0.999
Age Output : [[5.41567124e-06 1.38165860e-05 8.83182278e-04 1.35313682e-02
  9.51130509e-01 3.43035460e-02 2.52472619e-05 1.06873005e-04]]
Age : (25-32), conf = 0.951
time : 0.097
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.998
Age Output : [[3.7049015e-06 4.9028217e-06 3.6397346e-04 4.4258782e-03 9.6027070e-01
  3.4791950e-02 2.5869793e-05 1.1294959e-04]]
Age : (25-32), conf = 0.960
time : 0.090
Gender : Male, conf = 0.997
Age Output : [[2.8301968e-06 4.1590047e-06 2.2094947e-04 3.6207037e-03 9.6625704e-01
  2.9797062e-02 2.3618026e-05 7.3572075e-05]]
Age : (25-32), conf = 0.966
time : 0.105
Gender : Male, conf = 0.999
Age Output : [[2.2838283e-06 5.1412899e-06 3.8382708e-04 7.7243787e-03 9.7570002e-01
  1.6121021e-02 1.2593080e-05 5.0826788e-05]]
Age : (25-32), conf = 0.976
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[4.0858440e-06 6.5532204e-06 5.4467842e-04 8.7732980e-03 9.4585645e-01
  4.4702180e-02 2.1800284e-05 9.0943206e-05]]
Age : (25-32), conf = 0.946
time : 0.131
Gender : Male, conf = 0.998
Age Output : [[4.8050683e-06 8.2999659e-06 6.0902751e-04 1.1624457e-02 9.5252711e-01
  3.5093918e-02 2.3748131e-05 1.0870442e-04]]
Age : (25-32), conf = 0.953
time : 0.123
Gender : Male, conf = 0.997
Age Output : [[2.33368564e-06 5.07963205e-06 4.94356267e-04 3.96319991e-03
  9.80102479e-01 1.53851127e-02 1.26619225e-05 3.47863206e-05]]
Age : (25-32), conf = 0.980
time : 0.122
Gender : Male, conf = 0.990
Age Output : [[1.5335032e-06 4.3128630e-06 7.1784196e-04 1.1608530e-02 9.7155601e-01
  1.6063293e-02 1.2801754e-05 3.5506717e-05]]
Age : (25-32), conf = 0.972
time : 0.116
Gender : Male, conf = 0.998
Age Output : [[7.4148566e-06 8.1600556e-06 1.1841477e-03 1.8102014e-02 8.1632739e-01
  1.6410279e-01 5.2046718e-05 2.1604760e-04]]
Age : (25-32), conf = 0.816
time : 0.125
Gender : Male, conf = 0.997
Age Output : [[2.3433317e-06 6.0911430e-06 6.4467196e-04 1.1609980e-02 9.5908016e-01
  2.8581552e-02 1.4931238e-05 6.0306233e-05]]
Age : (25-32), conf = 0.959
time : 0.113
Gender : Male, conf = 0.995
Age Output : [[2.0605262e-06 3.7583040e-06 3.5562884e-04 5.2119289e-03 9.7137648e-01
  2.2980655e-02 1.2733521e-05 5.6755278e-05]]
Age : (25-32), conf = 0.971
time : 0.122
Gender : Male, conf = 0.997
Age Output : [[5.9789340e-06 1.1135361e-05 1.0093701e-03 1.8548153e-02 9.1308701e-01
  6.7183234e-02 3.0799805e-05 1.2435768e-04]]
Age : (25-32), conf = 0.913
time : 0.125
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.998
Age Output : [[1.93821165e-06 3.91335379e-06 3.86403874e-04 1.29318601e-02
  9.47639883e-01 3.89571413e-02 1.44514415e-05 6.43952953e-05]]
Age : (25-32), conf = 0.948
time : 0.177
Gender : Male, conf = 0.997
Age Output : [[6.2820200e-06 1.3491138e-05 7.1390765e-04 1.1844841e-02 9.6201313e-01
  2.5308952e-02 2.2664493e-05 7.6743221e-05]]
Age : (25-32), conf = 0.962
time : 0.144
Gender : Male, conf = 0.997
Age Output : [[4.7983085e-06 7.6412052e-06 6.2567118e-04 1.0090221e-02 9.2049628e-01
  6.8625838e-02 3.5008972e-05 1.1442832e-04]]
Age : (25-32), conf = 0.920
time : 0.136
Gender : Male, conf = 0.994
Age Output : [[3.2150816e-05 6.3606247e-05 2.9884151e-03 2.3430998e-02 8.9722300e-01
  7.6018594e-02 4.4905079e-05 1.9835039e-04]]
Age : (25-32), conf = 0.897
time : 0.136
Gender : Male, conf = 0.995
Age Output : [[2.7747130e-06 5.0789336e-06 4.6681258e-04 8.6559001e-03 9.4006330e-01
  5.0696429e-02 2.0139229e-05 8.9486661e-05]]
Age : (25-32), conf = 0.940
time : 0.117
Gender : Male, conf = 0.996
Age Output : [[1.12230055e-05 1.64974408e-05 8.44425755e-04 1.11002978e-02
  9.12311375e-01 7.54919648e-02 4.65070625e-05 1.77727066e-04]]
Age : (25-32), conf = 0.912
time : 0.134
Gender : Male, conf = 0.993
Age Output : [[5.7679176e-06 9.4987763e-06 4.6082452e-04 7.2119781e-03 9.4153386e-01
  5.0631445e-02 3.3429438e-05 1.1316111e-04]]
Age : (25-32), conf = 0.942
time : 0.133
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.998
Age Output : [[7.01795261e-06 1.34520951e-05 1.19075424e-03 1.95539035e-02
  9.05966163e-01 7.31328726e-02 3.15836332e-05 1.04286395e-04]]
Age : (25-32), conf = 0.906
time : 0.120
Gender : Male, conf = 0.997
Age Output : [[7.21120523e-06 1.28856063e-05 9.73035116e-04 2.56933477e-02
  9.04072642e-01 6.90979660e-02 2.69564443e-05 1.15974115e-04]]
Age : (25-32), conf = 0.904
time : 0.131
Gender : Male, conf = 0.996
Age Output : [[1.3392025e-05 2.7122202e-05 2.8197584e-03 4.3441538e-02 8.4903610e-01
  1.0444751e-01 3.3693792e-05 1.8087201e-04]]
Age : (25-32), conf = 0.849
time : 0.184
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.994
Age Output : [[2.5432955e-05 2.1429456e-04 7.2436766e-03 2.1683812e-02 9.3478310e-01
  3.5938449e-02 4.8758193e-05 6.2496700e-05]]
Age : (25-32), conf = 0.935
time : 0.124
Gender : Male, conf = 0.994
Age Output : [[3.0689065e-05 1.6551949e-04 1.0668769e-03 1.8707590e-02 9.6566576e-01
  1.4302352e-02 2.7063332e-05 3.4060955e-05]]
Age : (25-32), conf = 0.966
time : 0.128
Gender : Male, conf = 0.995
Age Output : [[2.8154192e-05 1.2673017e-04 6.7267223e-04 1.2768201e-02 9.7942585e-01
  6.9319275e-03 1.9141520e-05 2.7347300e-05]]
Age : (25-32), conf = 0.979
time : 0.194
Gender : Male, conf = 0.997
Age Output : [[3.3080265e-05 1.5623383e-04 1.5828235e-03 1.3805751e-02 9.6537858e-01
  1.8973725e-02 3.3716668e-05 3.6176843e-05]]
Age : (25-32), conf = 0.965
time : 0.163
Gender : Male, conf = 0.996
Age Output : [[1.16588244e-05 4.63250544e-05 1.67377410e-03 1.06986770e-02
  9.76269007e-01 1.12441685e-02 2.39109031e-05 3.24546927e-05]]
Age : (25-32), conf = 0.976
time : 0.172
Gender : Male, conf = 0.996
Age Output : [[6.4153530e-05 2.7392007e-04 1.0151890e-02 9.1305912e-02 8.6078507e-01
  3.7274458e-02 4.7165322e-05 9.7336393e-05]]
Age : (25-32), conf = 0.861
time : 0.141
Gender : Male, conf = 0.998
Age Output : [[6.2276406e-05 1.5143714e-04 3.5558657e-03 3.8604829e-02 9.3733829e-01
  2.0190084e-02 3.6986898e-05 6.0212202e-05]]
Age : (25-32), conf = 0.937
time : 0.111
Gender : Male, conf = 0.997
Age Output : [[9.1709935e-06 4.6334335e-05 2.9388838e-03 2.7475340e-02 9.3681264e-01
  3.2626785e-02 4.4509819e-05 4.6268629e-05]]
Age : (25-32), conf = 0.937
time : 0.096
Gender : Male, conf = 0.996
Age Output : [[2.2930308e-05 9.0601396e-05 1.7961897e-03 2.7180716e-02 9.4512564e-01
  2.5688920e-02 4.4082135e-05 5.0956867e-05]]
Age : (25-32), conf = 0.945
time : 0.117
Gender : Male, conf = 0.995
Age Output : [[6.9837042e-05 2.1732473e-04 6.8575842e-03 2.8784214e-02 9.2439151e-01
  3.9546624e-02 6.0418573e-05 7.2492207e-05]]
Age : (25-32), conf = 0.924
time : 0.093
Gender : Male, conf = 0.996
Age Output : [[3.6889443e-05 2.2498499e-04 6.7603365e-03 4.5265961e-02 9.1917390e-01
  2.8426213e-02 5.4724136e-05 5.6956767e-05]]
Age : (25-32), conf = 0.919
time : 0.100
Gender : Male, conf = 0.998
Age Output : [[9.6123433e-05 4.8036632e-04 9.7988835e-03 4.2656858e-02 9.0267855e-01
  4.4103701e-02 9.0092741e-05 9.5599593e-05]]
Age : (25-32), conf = 0.903
time : 0.098
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.996
Age Output : [[1.7176886e-06 8.4813773e-06 7.3245255e-04 9.9392310e-03 9.7305775e-01
  1.6200954e-02 3.0740681e-05 2.8722108e-05]]
Age : (25-32), conf = 0.973
time : 0.112
Gender : Male, conf = 0.997
Age Output : [[9.1631424e-05 2.7330246e-04 6.5480121e-03 1.8672951e-02 9.4384187e-01
  3.0384403e-02 8.7435823e-05 1.0049395e-04]]
Age : (25-32), conf = 0.944
time : 0.104
Gender : Male, conf = 0.998
Age Output : [[2.8299137e-05 5.7745434e-05 2.0651422e-03 5.6095263e-03 9.8147774e-01
  1.0694930e-02 2.7089091e-05 3.9483097e-05]]
Age : (25-32), conf = 0.981
time : 0.114
Gender : Male, conf = 0.996
Age Output : [[5.7424600e-06 1.4240469e-05 4.6383313e-04 2.0462028e-03 9.9165338e-01
  5.7763746e-03 1.7741575e-05 2.2432054e-05]]
Age : (25-32), conf = 0.992
time : 0.101
Gender : Male, conf = 0.995
Age Output : [[7.9585461e-06 1.7325005e-05 8.9164142e-04 2.9961462e-03 9.8946548e-01
  6.5856650e-03 1.6392742e-05 1.9363972e-05]]
Age : (25-32), conf = 0.989
time : 0.116
Gender : Male, conf = 0.995
Age Output : [[5.7808706e-05 9.0553731e-05 2.2711263e-03 3.3425554e-03 9.8035920e-01
  1.3768746e-02 5.4609238e-05 5.5399953e-05]]
Age : (25-32), conf = 0.980
time : 0.101
Gender : Male, conf = 0.996
Age Output : [[1.7411476e-05 5.1589876e-05 1.4753556e-03 5.9604351e-03 9.7270817e-01
  1.9700227e-02 3.8912574e-05 4.7849906e-05]]
Age : (25-32), conf = 0.973
time : 0.107
Gender : Male, conf = 0.998
Age Output : [[2.3858868e-06 1.6338056e-05 1.9737873e-03 5.9707388e-03 9.7770762e-01
  1.4292048e-02 1.6229335e-05 2.0900019e-05]]
Age : (25-32), conf = 0.978
time : 0.092
Gender : Male, conf = 0.998
Age Output : [[1.5643024e-06 7.9617257e-06 1.7117729e-04 1.7437703e-03 9.9529231e-01
  2.7654322e-03 8.0523650e-06 9.7435495e-06]]
Age : (25-32), conf = 0.995
time : 0.101
Gender : Male, conf = 0.994
Age Output : [[5.1901652e-04 4.3034120e-04 7.6566928e-04 2.2423698e-03 9.7934097e-01
  1.6424328e-02 1.3759620e-04 1.3960424e-04]]
Age : (25-32), conf = 0.979
time : 0.087
Gender : Male, conf = 0.994
Age Output : [[5.1901652e-04 4.3034120e-04 7.6566928e-04 2.2423698e-03 9.7934097e-01
  1.6424328e-02 1.3759620e-04 1.3960424e-04]]
Age : (25-32), conf = 0.979
time : 0.114
Gender : Male, conf = 0.999
Age Output : [[3.9178908e-06 1.8504630e-05 7.8679516e-04 1.4593430e-03 9.9010617e-01
  7.5760772e-03 2.5719470e-05 2.3509905e-05]]
Age : (25-32), conf = 0.990
time : 0.150
Gender : Male, conf = 0.997
Age Output : [[6.8651396e-05 9.3292641e-05 1.6179287e-03 3.3946456e-03 9.7430497e-01
  2.0370409e-02 5.3799860e-05 9.6232310e-05]]
Age : (25-32), conf = 0.974
time : 0.122
Gender : Male, conf = 0.998
Age Output : [[2.9912186e-04 3.6089259e-04 2.1010495e-03 2.7850037e-03 9.8062241e-01
  1.3618365e-02 8.3245133e-05 1.2986005e-04]]
Age : (25-32), conf = 0.981
time : 0.118
Gender : Male, conf = 0.996
Age Output : [[7.8068770e-06 4.3172655e-05 6.8439310e-03 3.7517226e-03 9.5850438e-01
  3.0773968e-02 3.4559111e-05 4.0463114e-05]]
Age : (25-32), conf = 0.959
time : 0.136
Gender : Male, conf = 0.998
Age Output : [[3.0769102e-04 1.1889997e-03 3.5491027e-02 1.5358265e-02 8.4744322e-01
  9.9857852e-02 1.5206901e-04 2.0091553e-04]]
Age : (25-32), conf = 0.847
time : 0.115
Gender : Male, conf = 0.996
Age Output : [[2.5574578e-04 1.0187748e-03 1.1411219e-02 1.1084620e-02 9.5306927e-01
  2.3024254e-02 5.7175399e-05 7.8978162e-05]]
Age : (25-32), conf = 0.953
time : 0.103
Gender : Male, conf = 0.999
Age Output : [[1.8935349e-05 6.8991081e-05 5.1690056e-03 3.4537513e-03 9.8229730e-01
  8.9388359e-03 2.5011039e-05 2.8092471e-05]]
Age : (25-32), conf = 0.982
time : 0.101
Gender : Male, conf = 0.998
Age Output : [[1.8508288e-05 7.3850584e-05 7.4547939e-03 6.0134400e-03 9.6769375e-01
  1.8674869e-02 2.8501057e-05 4.2393254e-05]]
Age : (25-32), conf = 0.968
time : 0.119
Gender : Male, conf = 0.998
Age Output : [[2.69262353e-04 3.02954722e-04 1.03185792e-02 5.81126614e-03
  9.42025065e-01 4.10721973e-02 8.43799498e-05 1.16351854e-04]]
Age : (25-32), conf = 0.942
time : 0.088
Gender : Male, conf = 0.998
Age Output : [[6.3147739e-04 7.2777871e-04 7.4916426e-03 7.2497907e-03 9.5349568e-01
  3.0138660e-02 9.8983641e-05 1.6590685e-04]]
Age : (25-32), conf = 0.953
time : 0.100
Gender : Male, conf = 0.995
Age Output : [[5.6358380e-04 8.5748627e-04 4.5344890e-03 9.7492384e-03 9.6244842e-01
  2.1647511e-02 7.6081349e-05 1.2314199e-04]]
Age : (25-32), conf = 0.962
time : 0.103
Gender : Male, conf = 0.998
Age Output : [[1.2100609e-05 5.1659867e-05 4.9979948e-03 5.9526879e-03 9.6979386e-01
  1.9117292e-02 2.9746479e-05 4.4737750e-05]]
Age : (25-32), conf = 0.970
time : 0.118
Gender : Male, conf = 0.999
Age Output : [[2.4947862e-05 9.7570737e-05 1.1491438e-02 1.1230374e-02 9.4893873e-01
  2.8121842e-02 4.2285203e-05 5.2740383e-05]]
Age : (25-32), conf = 0.949
time : 0.101
Gender : Male, conf = 0.996
Age Output : [[1.8582678e-05 7.0571616e-05 3.2210192e-03 5.2249986e-03 9.7799760e-01
  1.3398764e-02 2.9967774e-05 3.8437687e-05]]
Age : (25-32), conf = 0.978
time : 0.106
Gender : Male, conf = 0.997
Age Output : [[1.1293508e-04 3.1061459e-04 5.2353870e-03 5.6177815e-03 9.7132629e-01
  1.7271092e-02 5.7757607e-05 6.8187037e-05]]
Age : (25-32), conf = 0.971
time : 0.101
Gender : Male, conf = 0.997
Age Output : [[3.3255099e-04 8.8614447e-04 7.5656865e-03 6.6037145e-03 9.4619167e-01
  3.8241964e-02 7.9791913e-05 9.8449171e-05]]
Age : (25-32), conf = 0.946
time : 0.101
Gender : Male, conf = 0.998
Age Output : [[7.17831063e-05 1.13797076e-04 5.41604776e-03 1.41027439e-02
  9.36735511e-01 4.34045456e-02 6.37526609e-05 9.17712750e-05]]
Age : (25-32), conf = 0.937
time : 0.107
Gender : Male, conf = 0.997
Age Output : [[1.2434568e-03 9.1801630e-04 6.9312593e-03 8.2914904e-03 9.4337612e-01
  3.8833126e-02 1.6236247e-04 2.4418865e-04]]
Age : (25-32), conf = 0.943
time : 0.190
Gender : Male, conf = 0.998
Age Output : [[1.8856967e-05 3.2803120e-05 9.4047975e-04 2.6928280e-03 9.8510277e-01
  1.1153477e-02 2.3354300e-05 3.5510093e-05]]
Age : (25-32), conf = 0.985
time : 0.115
Gender : Male, conf = 0.999
Age Output : [[7.6654260e-06 6.7418478e-05 3.6686407e-03 9.7792270e-03 9.7649777e-01
  9.9304151e-03 2.0650810e-05 2.8315200e-05]]
Age : (25-32), conf = 0.976
time : 0.110
Gender : Male, conf = 0.998
Age Output : [[3.0498652e-06 1.5769927e-05 9.8255114e-04 5.2117850e-03 9.7946805e-01
  1.4277674e-02 1.9332336e-05 2.1819502e-05]]
Age : (25-32), conf = 0.979
time : 0.122
Gender : Male, conf = 0.998
Age Output : [[2.7673790e-05 5.4444485e-05 2.4596162e-03 3.5996768e-03 9.7690672e-01
  1.6853841e-02 4.6162615e-05 5.1906274e-05]]
Age : (25-32), conf = 0.977
time : 0.100
Gender : Male, conf = 0.992
Age Output : [[8.58153653e-05 1.03302540e-04 1.20346539e-03 2.44138134e-03
  9.66481924e-01 2.94658169e-02 1.01250298e-04 1.17046395e-04]]
Age : (25-32), conf = 0.966
time : 0.085
Gender : Male, conf = 0.992
Age Output : [[8.58153653e-05 1.03302540e-04 1.20346539e-03 2.44138134e-03
  9.66481924e-01 2.94658169e-02 1.01250298e-04 1.17046395e-04]]
Age : (25-32), conf = 0.966
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[8.3032210e-05 1.4412699e-04 8.8993408e-04 1.9221633e-03 9.6504617e-01
  3.1739935e-02 8.5216605e-05 8.9318935e-05]]
Age : (25-32), conf = 0.965
time : 0.100
Gender : Male, conf = 0.994
Age Output : [[1.9145991e-05 3.8812235e-05 7.5116556e-04 4.6324306e-03 9.9126679e-01
  3.2544534e-03 1.3513282e-05 2.3700002e-05]]
Age : (25-32), conf = 0.991
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[9.2582486e-06 2.8208136e-05 8.7228121e-04 3.2848986e-03 9.6515501e-01
  3.0562023e-02 3.8722661e-05 4.9431052e-05]]
Age : (25-32), conf = 0.965
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[2.0266367e-05 2.6698865e-05 3.7778064e-04 1.1434994e-03 9.9234104e-01
  6.0461853e-03 1.8881017e-05 2.5591977e-05]]
Age : (25-32), conf = 0.992
time : 0.116
Gender : Male, conf = 0.999
Age Output : [[3.0922579e-02 7.1013579e-03 1.3634099e-02 1.4616906e-02 9.2141843e-01
  1.1798452e-02 1.6131686e-04 3.4689571e-04]]
Age : (25-32), conf = 0.921
time : 0.123
Gender : Male, conf = 0.998
Age Output : [[2.1432117e-01 4.8268195e-02 2.8515706e-02 9.2976093e-03 6.8435335e-01
  1.4500153e-02 1.9999762e-04 5.4374739e-04]]
Age : (25-32), conf = 0.684
time : 0.102
Gender : Male, conf = 0.998
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[1.7569608e-03 1.3747356e-03 2.4467003e-02 7.8160632e-03 9.4924897e-01
  1.5157212e-02 5.3797150e-05 1.2525878e-04]]
Age : (25-32), conf = 0.949
time : 0.103
Gender : Male, conf = 0.998
Age Output : [[3.11478935e-02 1.25468411e-02 2.61102542e-02 1.06547829e-02
  9.06859457e-01 1.22512039e-02 1.19529526e-04 3.09963856e-04]]
Age : (25-32), conf = 0.907
time : 0.119
Gender : Male, conf = 1.000
Age Output : [[1.9910730e-01 6.4307578e-02 2.3593251e-02 5.6600361e-03 6.9771087e-01
  9.1130082e-03 1.7679030e-04 3.3115008e-04]]
Age : (25-32), conf = 0.698
time : 0.125
Gender : Male, conf = 0.999
Age Output : [[6.2325176e-02 1.3907664e-02 2.8084371e-02 7.7730757e-03 8.6371505e-01
  2.3398632e-02 2.9434086e-04 5.0162274e-04]]
Age : (25-32), conf = 0.864
time : 0.104
Gender : Male, conf = 0.999
Age Output : [[6.2325176e-02 1.3907664e-02 2.8084371e-02 7.7730757e-03 8.6371505e-01
  2.3398632e-02 2.9434086e-04 5.0162274e-04]]
Age : (25-32), conf = 0.864
time : 0.132
Gender : Male, conf = 0.999
Age Output : [[1.4771359e-03 1.1713625e-03 3.2537968e-03 3.6191884e-03 9.7800797e-01
  1.2178617e-02 1.4468914e-04 1.4721006e-04]]
Age : (25-32), conf = 0.978
time : 0.112
Gender : Male, conf = 0.999
Age Output : [[1.1119404e-03 6.6701887e-04 2.1258651e-03 2.0684467e-03 9.8193711e-01
  1.1849191e-02 1.0474807e-04 1.3570076e-04]]
Age : (25-32), conf = 0.982
time : 0.103
Gender : Male, conf = 0.999
Age Output : [[1.1939154e-03 8.4263395e-04 1.8687798e-03 5.8594886e-03 9.8053265e-01
  9.4556613e-03 1.0136667e-04 1.4540851e-04]]
Age : (25-32), conf = 0.981
time : 0.098
Gender : Male, conf = 0.999
Age Output : [[7.1323605e-04 3.3489501e-04 1.9452325e-03 2.1192110e-03 9.9041057e-01
  4.3189130e-03 5.1401905e-05 1.0665919e-04]]
Age : (25-32), conf = 0.990
time : 0.104
Gender : Male, conf = 0.999
Age Output : [[5.7956157e-03 3.1851467e-03 3.1582552e-03 8.3601279e-03 9.6886885e-01
  1.0185722e-02 1.9676564e-04 2.4951104e-04]]
Age : (25-32), conf = 0.969
time : 0.092
Gender : Male, conf = 0.999
Age Output : [[2.9161101e-04 2.2027285e-04 6.8075012e-04 1.3451873e-03 9.9572080e-01
  1.6791765e-03 2.1869868e-05 4.0479950e-05]]
Age : (25-32), conf = 0.996
time : 0.131
Gender : Male, conf = 0.999
Age Output : [[3.7298137e-03 8.2543690e-04 1.3648933e-03 1.4577759e-03 9.8561794e-01
  6.7662168e-03 9.8843419e-05 1.3906253e-04]]
Age : (25-32), conf = 0.986
time : 0.086
Gender : Male, conf = 0.996
Age Output : [[2.7213385e-02 6.1145695e-03 2.0315277e-03 2.4709480e-03 9.5552647e-01
  6.2858099e-03 1.4675604e-04 2.1058670e-04]]
Age : (25-32), conf = 0.956
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[5.9761908e-03 1.5359635e-03 1.1199475e-03 1.7124799e-03 9.8075533e-01
  8.5919816e-03 1.3426701e-04 1.7394112e-04]]
Age : (25-32), conf = 0.981
time : 0.103
Gender : Male, conf = 0.998
Age Output : [[1.4305613e-03 4.8097310e-04 9.1039506e-04 1.7920708e-03 9.8736215e-01
  7.7958121e-03 1.0442842e-04 1.2370849e-04]]
Age : (25-32), conf = 0.987
time : 0.101
Gender : Male, conf = 0.995
Age Output : [[5.5971056e-01 2.8570667e-02 5.9519433e-03 2.9121626e-03 3.9462605e-01
  7.5493213e-03 2.4613913e-04 4.3311858e-04]]
Age : (0-2), conf = 0.560
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[1.6471228e-01 3.0608201e-02 1.5715804e-02 4.8915511e-03 7.5965208e-01
  2.3540478e-02 3.7347563e-04 5.0610473e-04]]
Age : (25-32), conf = 0.760
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[1.6471228e-01 3.0608201e-02 1.5715804e-02 4.8915511e-03 7.5965208e-01
  2.3540478e-02 3.7347563e-04 5.0610473e-04]]
Age : (25-32), conf = 0.760
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[4.8506726e-04 1.1938249e-03 2.3685671e-02 1.6754573e-02 9.2477089e-01
  3.2872807e-02 1.1153514e-04 1.2553814e-04]]
Age : (25-32), conf = 0.925
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[3.7916731e-02 1.0553226e-02 7.5275125e-03 1.4210954e-02 8.9654130e-01
  3.2327097e-02 3.5778142e-04 5.6536007e-04]]
Age : (25-32), conf = 0.897
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[1.2432365e-03 7.6449255e-04 5.0539062e-03 9.1695245e-03 9.6704125e-01
  1.6506126e-02 9.0787180e-05 1.3060516e-04]]
Age : (25-32), conf = 0.967
time : 0.135
Gender : Male, conf = 0.989
Age Output : [[1.5996595e-05 2.4575796e-05 1.1226400e-03 1.1015699e-03 9.8914182e-01
  8.5331211e-03 2.5998115e-05 3.4371718e-05]]
Age : (25-32), conf = 0.989
time : 0.156
Gender : Male, conf = 0.992
Age Output : [[1.1104470e-03 9.0719434e-04 3.2724997e-03 2.4377604e-03 9.7025126e-01
  2.1643419e-02 1.8656476e-04 1.9085883e-04]]
Age : (25-32), conf = 0.970
time : 0.149
Gender : Male, conf = 0.990
Age Output : [[5.0710440e-02 1.6874103e-02 8.2373191e-03 6.2826616e-03 8.9217257e-01
  2.4861207e-02 3.7226302e-04 4.8945448e-04]]
Age : (25-32), conf = 0.892
time : 0.110
Gender : Male, conf = 0.996
Age Output : [[3.2225215e-01 5.3115990e-02 1.2964529e-02 9.0997675e-03 5.7482117e-01
  2.6422894e-02 5.5878877e-04 7.6473324e-04]]
Age : (25-32), conf = 0.575
time : 0.136
Gender : Male, conf = 0.997
Age Output : [[1.7598487e-02 7.2579319e-03 5.1602055e-03 6.0088108e-03 9.3574911e-01
  2.7437260e-02 3.5269835e-04 4.3552968e-04]]
Age : (25-32), conf = 0.936
time : 0.105
Gender : Male, conf = 0.992
Age Output : [[2.6668865e-02 4.9461569e-03 2.7890941e-03 3.2109926e-03 9.3132377e-01
  3.0117918e-02 3.7533272e-04 5.6790147e-04]]
Age : (25-32), conf = 0.931
time : 0.098
Gender : Male, conf = 0.991
Age Output : [[4.6935320e-04 5.4167281e-04 4.0174057e-03 7.5300434e-03 9.7924989e-01
  8.0893002e-03 3.4108107e-05 6.8327972e-05]]
Age : (25-32), conf = 0.979
time : 0.118
Gender : Male, conf = 0.996
Age Output : [[1.0480262e-01 3.2693155e-02 1.9018684e-02 9.8661641e-03 8.0690563e-01
  2.5847083e-02 3.3071358e-04 5.3598476e-04]]
Age : (25-32), conf = 0.807
time : 0.098
Gender : Male, conf = 0.995
Age Output : [[2.03141347e-02 1.11829275e-02 9.93308332e-03 8.07962101e-03
  9.19454992e-01 3.01779117e-02 3.89049819e-04 4.68387210e-04]]
Age : (25-32), conf = 0.919
time : 0.099
Gender : Male, conf = 0.995
Age Output : [[2.03141347e-02 1.11829275e-02 9.93308332e-03 8.07962101e-03
  9.19454992e-01 3.01779117e-02 3.89049819e-04 4.68387210e-04]]
Age : (25-32), conf = 0.919
time : 0.105
Gender : Male, conf = 0.997
Age Output : [[1.0365261e-02 1.2796769e-02 1.8919798e-02 1.0267731e-02 9.1164637e-01
  3.5183251e-02 4.2069759e-04 4.0016646e-04]]
Age : (25-32), conf = 0.912
time : 0.110
Gender : Male, conf = 0.994
Age Output : [[2.2522765e-04 2.8976260e-04 2.8425963e-03 1.8503908e-03 9.7107947e-01
  2.3514256e-02 1.0561010e-04 9.2686496e-05]]
Age : (25-32), conf = 0.971
time : 0.106
Gender : Male, conf = 0.995
Age Output : [[2.2948809e-02 1.2353128e-02 6.6188788e-03 4.5541553e-03 9.3349665e-01
  1.9242523e-02 3.7452666e-04 4.1132566e-04]]
Age : (25-32), conf = 0.933
time : 0.104
Gender : Male, conf = 0.996
Age Output : [[6.4852757e-05 1.4138302e-04 1.3226545e-03 1.2601129e-03 9.8700237e-01
  1.0093992e-02 6.3578264e-05 5.1119416e-05]]
Age : (25-32), conf = 0.987
time : 0.102
Gender : Male, conf = 0.998
Age Output : [[4.0135138e-02 4.6757620e-02 1.1476812e-02 1.8232659e-02 8.6551434e-01
  1.7335190e-02 2.9657505e-04 2.5160998e-04]]
Age : (25-32), conf = 0.866
time : 0.101
Gender : Male, conf = 0.992
Age Output : [[2.9443724e-03 1.5973335e-03 2.2471857e-03 3.6865934e-03 9.6481919e-01
  2.4325160e-02 1.9503900e-04 1.8503648e-04]]
Age : (25-32), conf = 0.965
time : 0.098
Gender : Male, conf = 0.993
Age Output : [[1.35296155e-02 1.28832487e-02 6.73341332e-03 5.68176853e-03
  9.42502499e-01 1.80867165e-02 3.26490263e-04 2.56307190e-04]]
Age : (25-32), conf = 0.943
time : 0.084
Gender : Male, conf = 0.992
Age Output : [[7.7260617e-04 2.0175308e-03 3.8343889e-03 5.6568277e-03 9.8359722e-01
  4.0310984e-03 4.2258132e-05 4.8079266e-05]]
Age : (25-32), conf = 0.984
time : 0.084
Gender : Male, conf = 0.992
Age Output : [[1.5564471e-04 4.9763190e-04 6.0712933e-03 2.0249616e-02 9.6619606e-01
  6.7569460e-03 3.2384381e-05 4.0523548e-05]]
Age : (25-32), conf = 0.966
time : 0.100
Gender : Male, conf = 0.992
Age Output : [[1.5564471e-04 4.9763190e-04 6.0712933e-03 2.0249616e-02 9.6619606e-01
  6.7569460e-03 3.2384381e-05 4.0523548e-05]]
Age : (25-32), conf = 0.966
time : 0.107
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.995
Age Output : [[6.8963468e-06 4.1886204e-05 1.2554184e-03 3.0940624e-03 9.8972195e-01
  5.8379010e-03 2.3061781e-05 1.8977413e-05]]
Age : (25-32), conf = 0.990
time : 0.118
Gender : Male, conf = 0.996
Age Output : [[2.1755641e-05 2.3841509e-04 3.0502977e-03 7.3649222e-03 9.8263180e-01
  6.6465521e-03 2.5716483e-05 2.0379826e-05]]
Age : (25-32), conf = 0.983
time : 0.104
Gender : Male, conf = 0.980
Age Output : [[1.2068375e-04 3.3791311e-04 1.7331331e-03 4.4592349e-03 9.8562175e-01
  7.6474817e-03 3.9274670e-05 4.0513612e-05]]
Age : (25-32), conf = 0.986
time : 0.100
Gender : Male, conf = 0.988
Age Output : [[3.5605914e-04 3.8449507e-04 1.0835071e-03 3.3986738e-03 9.8642689e-01
  8.1919171e-03 7.5474753e-05 8.2965875e-05]]
Age : (25-32), conf = 0.986
time : 0.106
Gender : Male, conf = 0.992
Age Output : [[1.4350227e-04 4.4153468e-04 1.6994131e-03 3.5778638e-03 9.8720282e-01
  6.7997333e-03 8.3577157e-05 5.1543841e-05]]
Age : (25-32), conf = 0.987
time : 0.097
Gender : Male, conf = 0.974
Age Output : [[1.6687276e-05 3.4424767e-05 5.0319883e-04 1.2676764e-03 9.9299425e-01
  5.1131425e-03 4.1403950e-05 2.9124729e-05]]
Age : (25-32), conf = 0.993
time : 0.108
Gender : Male, conf = 0.987
Age Output : [[1.9654100e-05 4.6803718e-05 1.9803329e-03 5.9965202e-03 9.6606177e-01
  2.5792297e-02 4.9832935e-05 5.2721032e-05]]
Age : (25-32), conf = 0.966
time : 0.099
Gender : Male, conf = 0.989
Age Output : [[9.8772551e-05 2.7531676e-04 2.6347123e-03 5.2403663e-03 9.8166013e-01
  9.9730454e-03 7.0698632e-05 4.6903293e-05]]
Age : (25-32), conf = 0.982
time : 0.100
Gender : Male, conf = 0.990
Age Output : [[2.6621409e-03 2.1367518e-03 6.0683531e-03 6.0370439e-03 9.7456884e-01
  8.3694598e-03 6.2476334e-05 9.4954470e-05]]
Age : (25-32), conf = 0.975
time : 0.104
Gender : Male, conf = 0.996
Age Output : [[4.7372575e-03 5.4509765e-03 5.7393904e-03 3.5500606e-03 9.7140449e-01
  8.9027230e-03 8.6957625e-05 1.2818478e-04]]
Age : (25-32), conf = 0.971
time : 0.120
Gender : Male, conf = 0.992
Age Output : [[3.0183536e-04 4.4743731e-04 1.5030967e-03 2.2600829e-03 9.9162489e-01
  3.7668319e-03 5.3183947e-05 4.2665841e-05]]
Age : (25-32), conf = 0.992
time : 0.129
Gender : Male, conf = 0.980
Age Output : [[2.2018580e-04 4.8906804e-04 4.0627453e-03 3.5302760e-03 9.8587650e-01
  5.6997407e-03 4.9078299e-05 7.2398267e-05]]
Age : (25-32), conf = 0.986
time : 0.133
Gender : Male, conf = 0.994
Age Output : [[4.7351167e-04 3.0718357e-04 1.6246823e-03 1.1861020e-03 9.9314475e-01
  3.1539036e-03 5.2047948e-05 5.7946301e-05]]
Age : (25-32), conf = 0.993
time : 0.147
Gender : Male, conf = 0.990
Age Output : [[1.9079474e-05 2.0363737e-05 1.0378580e-03 7.2873593e-04 9.9356067e-01
  4.5731165e-03 2.5741754e-05 3.4417248e-05]]
Age : (25-32), conf = 0.994
time : 0.140
Gender : Male, conf = 0.998
Age Output : [[9.5348747e-04 2.0884944e-03 5.0707575e-02 7.1912981e-03 9.2690396e-01
  1.1769957e-02 9.2113019e-05 2.9305441e-04]]
Age : (25-32), conf = 0.927
time : 0.137
Gender : Male, conf = 0.996
Age Output : [[5.10164129e-04 6.18097198e-04 1.48388389e-02 3.02324956e-03
  9.67799783e-01 1.27224270e-02 1.09174995e-04 3.78309516e-04]]
Age : (25-32), conf = 0.968
time : 0.133
Gender : Male, conf = 0.999
Age Output : [[1.7720138e-03 2.2038708e-03 2.4917947e-02 5.9816479e-03 9.4093907e-01
  2.3104092e-02 2.2347544e-04 8.5793698e-04]]
Age : (25-32), conf = 0.941
time : 0.117
Gender : Male, conf = 0.996
Age Output : [[1.0295388e-03 1.4284084e-03 3.9017890e-02 7.0701870e-03 9.2935240e-01
  2.1562552e-02 1.1306598e-04 4.2584713e-04]]
Age : (25-32), conf = 0.929
time : 0.131
Gender : Male, conf = 0.998
Age Output : [[1.1946064e-02 6.4446186e-03 7.2830588e-02 7.3429770e-03 8.5605413e-01
  4.3684736e-02 3.0876065e-04 1.3880917e-03]]
Age : (25-32), conf = 0.856
time : 0.119
Gender : Male, conf = 0.999
Age Output : [[1.3422765e-03 1.3970763e-03 6.4706944e-02 4.6563400e-03 8.9772940e-01
  2.9637497e-02 7.8774101e-05 4.5173697e-04]]
Age : (25-32), conf = 0.898
time : 0.113
Gender : Male, conf = 0.996
Age Output : [[1.2972614e-03 5.9457461e-04 1.7160023e-02 4.3341098e-03 9.4410521e-01
  3.1170113e-02 1.7611969e-04 1.1626405e-03]]
Age : (25-32), conf = 0.944
time : 0.136
Gender : Male, conf = 0.999
Age Output : [[0.16305083 0.21390267 0.27194357 0.01859461 0.30612454 0.02487662
  0.00039158 0.00111561]]
Age : (25-32), conf = 0.306
time : 0.129
Gender : Male, conf = 0.999
Age Output : [[2.4466173e-04 8.3088770e-04 9.3190357e-02 1.3890833e-02 8.7516576e-01
  1.6373551e-02 8.8392007e-05 2.1559943e-04]]
Age : (25-32), conf = 0.875
time : 0.128
Gender : Male, conf = 0.986
Age Output : [[0.09285755 0.039423   0.024025   0.01000908 0.81101954 0.02002179
  0.00110121 0.00154288]]
Age : (25-32), conf = 0.811
time : 0.135
Gender : Male, conf = 0.955
Age Output : [[5.2713021e-03 5.7371687e-03 2.0866098e-02 6.7981859e-03 9.5322609e-01
  7.6201232e-03 2.1891740e-04 2.6201556e-04]]
Age : (25-32), conf = 0.953
time : 0.129
Gender : Male, conf = 0.989
Age Output : [[1.8325726e-03 1.3599606e-03 6.9139693e-03 3.8958772e-03 9.7493774e-01
  1.0808323e-02 8.7778084e-05 1.6380347e-04]]
Age : (25-32), conf = 0.975
time : 0.116
Gender : Male, conf = 0.997
Age Output : [[5.0569894e-03 3.4081100e-03 8.3249947e-03 4.6247770e-03 9.7094697e-01
  7.2511700e-03 1.4417701e-04 2.4281276e-04]]
Age : (25-32), conf = 0.971
time : 0.139
Gender : Male, conf = 0.994
Age Output : [[2.4290371e-03 2.6779776e-03 1.6296098e-02 7.8783659e-03 9.5572746e-01
  1.4647954e-02 1.2093053e-04 2.2226010e-04]]
Age : (25-32), conf = 0.956
time : 0.136
Gender : Male, conf = 0.951
Age Output : [[8.3703249e-05 2.2630030e-04 7.4747545e-03 3.3323618e-03 9.7825068e-01
  1.0479685e-02 7.0801507e-05 8.1768878e-05]]
Age : (25-32), conf = 0.978
time : 0.150
Gender : Male, conf = 0.984
Age Output : [[1.3896454e-03 2.4379175e-03 1.0037508e-02 7.7060768e-03 9.6669513e-01
  1.1352854e-02 1.9621768e-04 1.8459845e-04]]
Age : (25-32), conf = 0.967
time : 0.133
Gender : Male, conf = 0.987
Age Output : [[2.71145807e-04 9.22380306e-04 1.88548937e-02 6.36779657e-03
  9.63021994e-01 1.03426306e-02 1.15010691e-04 1.04121325e-04]]
Age : (25-32), conf = 0.963
time : 0.137
Gender : Male, conf = 0.993
Age Output : [[1.1470886e-02 8.9072855e-03 1.0751716e-02 5.5550341e-03 9.5038098e-01
  1.2515888e-02 1.8576207e-04 2.3247625e-04]]
Age : (25-32), conf = 0.950
time : 0.111
Gender : Male, conf = 0.993
Age Output : [[1.1470886e-02 8.9072855e-03 1.0751716e-02 5.5550341e-03 9.5038098e-01
  1.2515888e-02 1.8576207e-04 2.3247625e-04]]
Age : (25-32), conf = 0.950
time : 0.100
Gender : Male, conf = 0.972
Age Output : [[1.8094714e-03 1.9949318e-03 7.0091407e-03 3.7331369e-03 9.6845031e-01
  1.6592572e-02 2.2325150e-04 1.8710998e-04]]
Age : (25-32), conf = 0.968
time : 0.100
Gender : Male, conf = 0.969
Age Output : [[1.56322378e-04 2.00217721e-04 4.03495505e-03 2.35910784e-03
  9.81426001e-01 1.16132051e-02 1.05159561e-04 1.05107014e-04]]
Age : (25-32), conf = 0.981
time : 0.101
Gender : Male, conf = 0.961
Age Output : [[4.1552219e-03 5.3735916e-03 1.0056685e-02 7.5238338e-03 9.5697069e-01
  1.5534855e-02 2.0767622e-04 1.7754344e-04]]
Age : (25-32), conf = 0.957
time : 0.119
Gender : Male, conf = 0.973
Age Output : [[4.80243587e-04 5.16051834e-04 2.12678616e-03 2.75156647e-03
  9.82215881e-01 1.15312245e-02 2.18493005e-04 1.59774587e-04]]
Age : (25-32), conf = 0.982
time : 0.187
Gender : Male, conf = 0.994
Age Output : [[6.3854023e-03 1.6150015e-03 3.3548223e-03 2.9732385e-03 9.6856034e-01
  1.6276456e-02 3.3182584e-04 5.0300721e-04]]
Age : (25-32), conf = 0.969
time : 0.205
Gender : Male, conf = 0.997
Age Output : [[2.3706433e-04 1.9427134e-04 4.8856051e-03 2.3532531e-03 9.7862387e-01
  1.3510623e-02 9.0691428e-05 1.0460093e-04]]
Age : (25-32), conf = 0.979
time : 0.181
Gender : Male, conf = 0.998
Age Output : [[2.1970760e-04 1.3729624e-04 2.2720499e-03 1.4349237e-03 9.7712016e-01
  1.8451570e-02 1.6519209e-04 1.9918672e-04]]
Age : (25-32), conf = 0.977
time : 0.139
Gender : Male, conf = 0.995
Age Output : [[1.7068918e-03 5.5843452e-04 3.1409145e-03 2.4536105e-03 9.7918218e-01
  1.2572623e-02 1.6100059e-04 2.2434381e-04]]
Age : (25-32), conf = 0.979
time : 0.112
Gender : Male, conf = 0.995
Age Output : [[1.7068918e-03 5.5843452e-04 3.1409145e-03 2.4536105e-03 9.7918218e-01
  1.2572623e-02 1.6100059e-04 2.2434381e-04]]
Age : (25-32), conf = 0.979
time : 0.102
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.997
Age Output : [[7.53218657e-04 4.26792278e-04 2.11861241e-03 4.65578027e-03
  9.76349235e-01 1.52844945e-02 1.99337097e-04 2.12488478e-04]]
Age : (25-32), conf = 0.976
time : 0.098
Gender : Male, conf = 0.995
Age Output : [[1.0925344e-03 3.7062450e-04 6.2128352e-03 7.5836312e-03 9.4474870e-01
  3.9330322e-02 2.4206354e-04 4.1933320e-04]]
Age : (25-32), conf = 0.945
time : 0.090
Gender : Male, conf = 0.997
Age Output : [[1.5449523e-03 3.1809157e-04 2.6079002e-03 2.6225427e-03 9.5123547e-01
  4.0936328e-02 2.7151487e-04 4.6326916e-04]]
Age : (25-32), conf = 0.951
time : 0.106
Gender : Male, conf = 0.998
Age Output : [[5.1754354e-03 2.4564138e-03 1.6375644e-02 8.8658417e-03 9.3001169e-01
  3.6291461e-02 2.9042989e-04 5.3307688e-04]]
Age : (25-32), conf = 0.930
time : 0.101
Gender : Male, conf = 0.996
Age Output : [[6.0498004e-04 2.9609891e-04 1.5573234e-02 3.6592721e-03 9.4716281e-01
  3.2283098e-02 1.4792701e-04 2.7272548e-04]]
Age : (25-32), conf = 0.947
time : 0.101
Gender : Male, conf = 0.996
Age Output : [[6.0498004e-04 2.9609891e-04 1.5573234e-02 3.6592721e-03 9.4716281e-01
  3.2283098e-02 1.4792701e-04 2.7272548e-04]]
Age : (25-32), conf = 0.947
time : 0.101
Gender : Male, conf = 0.988
Age Output : [[6.2762928e-04 4.2474302e-04 1.5315137e-02 8.5035292e-03 9.3707138e-01
  3.7612062e-02 1.5532781e-04 2.9026502e-04]]
Age : (25-32), conf = 0.937
time : 0.113
Gender : Male, conf = 0.996
Age Output : [[4.8948184e-02 2.0836294e-02 1.6420243e-02 9.0315696e-03 8.8760728e-01
  1.6438555e-02 2.9998441e-04 4.1786427e-04]]
Age : (25-32), conf = 0.888
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[5.6950818e-04 4.3685324e-04 1.5052490e-02 7.8735305e-03 9.3710274e-01
  3.8687550e-02 7.7330551e-05 2.0006721e-04]]
Age : (25-32), conf = 0.937
time : 0.087
Gender : Male, conf = 0.998
Age Output : [[5.4355385e-04 5.1295751e-04 1.6225865e-02 6.4803232e-03 9.4660306e-01
  2.9382620e-02 8.2522056e-05 1.6916967e-04]]
Age : (25-32), conf = 0.947
time : 0.078
Gender : Male, conf = 0.998
Age Output : [[2.6587237e-04 4.4161599e-04 2.7221577e-02 6.7929253e-03 9.4427973e-01
  2.0762734e-02 9.8070959e-05 1.3756493e-04]]
Age : (25-32), conf = 0.944
time : 0.091
Gender : Male, conf = 0.998
Age Output : [[5.8615947e-04 7.4324140e-04 1.5269832e-02 7.0825932e-03 9.1996098e-01
  5.5729806e-02 3.2249605e-04 3.0492287e-04]]
Age : (25-32), conf = 0.920
time : 0.088
Gender : Male, conf = 0.996
Age Output : [[8.5955464e-05 1.6580914e-04 8.2685975e-03 2.1068451e-03 9.6774131e-01
  2.1437498e-02 9.3244445e-05 1.0078291e-04]]
Age : (25-32), conf = 0.968
time : 0.099
Gender : Male, conf = 0.996
Age Output : [[8.5955464e-05 1.6580914e-04 8.2685975e-03 2.1068451e-03 9.6774131e-01
  2.1437498e-02 9.3244445e-05 1.0078291e-04]]
Age : (25-32), conf = 0.968
time : 0.101
Gender : Male, conf = 0.996
Age Output : [[1.18047494e-04 1.15783681e-04 2.70297774e-03 1.93636271e-03
  9.78039861e-01 1.69080794e-02 7.32009576e-05 1.05672472e-04]]
Age : (25-32), conf = 0.978
time : 0.087
Gender : Male, conf = 0.996
Age Output : [[1.18047494e-04 1.15783681e-04 2.70297774e-03 1.93636271e-03
  9.78039861e-01 1.69080794e-02 7.32009576e-05 1.05672472e-04]]
Age : (25-32), conf = 0.978
time : 0.103
Gender : Male, conf = 0.998
Age Output : [[4.1993818e-04 4.3654753e-04 2.2186477e-02 9.0047223e-03 9.0330577e-01
  6.3954808e-02 3.1675870e-04 3.7482369e-04]]
Age : (25-32), conf = 0.903
time : 0.111
Gender : Male, conf = 0.997
Age Output : [[6.1656442e-04 3.1800332e-04 6.6206586e-03 4.8589809e-03 9.2846417e-01
  5.8590908e-02 1.9379440e-04 3.3696872e-04]]
Age : (25-32), conf = 0.928
time : 0.098
Gender : Male, conf = 0.997
Age Output : [[1.2230271e-03 1.0416064e-03 3.0617040e-02 4.0261098e-03 9.2490560e-01
  3.7759855e-02 1.5472939e-04 2.7214055e-04]]
Age : (25-32), conf = 0.925
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[3.1795240e-05 6.9810812e-05 4.3932931e-03 1.0661560e-02 9.6737301e-01
  1.7329723e-02 5.3890337e-05 8.6973327e-05]]
Age : (25-32), conf = 0.967
time : 0.097
Gender : Male, conf = 0.997
Age Output : [[7.8153877e-05 2.0129765e-04 3.3918176e-02 1.2292758e-02 9.1630495e-01
  3.7061185e-02 5.1652125e-05 9.1801216e-05]]
Age : (25-32), conf = 0.916
time : 0.101
Gender : Male, conf = 0.996
Age Output : [[1.8118616e-04 1.7362632e-04 1.0375138e-02 7.0806295e-03 9.5709962e-01
  2.4719099e-02 1.0868385e-04 2.6200517e-04]]
Age : (25-32), conf = 0.957
time : 0.095
Gender : Male, conf = 0.994
Age Output : [[1.6846136e-03 2.3031365e-03 1.0598196e-01 1.4522041e-02 8.0754650e-01
  6.6974528e-02 3.1988492e-04 6.6737045e-04]]
Age : (25-32), conf = 0.808
time : 0.099
Gender : Male, conf = 0.998
Age Output : [[2.98747414e-04 4.28404193e-04 1.02269631e-02 7.99629278e-03
  9.65019345e-01 1.57570373e-02 1.14462004e-04 1.58743467e-04]]
Age : (25-32), conf = 0.965
time : 0.078
Gender : Male, conf = 0.997
Age Output : [[1.8062774e-04 2.1654727e-04 7.6140547e-03 5.1691006e-03 9.5764583e-01
  2.8772786e-02 1.4291937e-04 2.5798919e-04]]
Age : (25-32), conf = 0.958
time : 0.084
Gender : Male, conf = 0.997
Age Output : [[1.8062774e-04 2.1654727e-04 7.6140547e-03 5.1691006e-03 9.5764583e-01
  2.8772786e-02 1.4291937e-04 2.5798919e-04]]
Age : (25-32), conf = 0.958
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[1.3734367e-04 1.5289581e-04 1.7614099e-03 3.5213688e-03 9.8925334e-01
  4.9961810e-03 6.3989326e-05 1.1345522e-04]]
Age : (25-32), conf = 0.989
time : 0.090
Gender : Male, conf = 0.998
Age Output : [[6.47109264e-05 7.61360716e-05 1.47311129e-02 8.57442617e-03
  9.17992890e-01 5.81759550e-02 1.21639096e-04 2.63096503e-04]]
Age : (25-32), conf = 0.918
time : 0.079
Gender : Male, conf = 0.996
Age Output : [[1.3574229e-04 1.3700251e-04 1.2552236e-02 5.0731367e-03 9.1206980e-01
  6.9561608e-02 1.9514628e-04 2.7534243e-04]]
Age : (25-32), conf = 0.912
time : 0.084
Gender : Male, conf = 0.994
Age Output : [[1.5218505e-03 7.6294784e-04 7.4411058e-03 3.4328839e-03 9.5332164e-01
  3.2902833e-02 2.5264709e-04 3.6417253e-04]]
Age : (25-32), conf = 0.953
time : 0.116
Gender : Male, conf = 0.998
Age Output : [[5.3828237e-05 6.4389933e-05 7.9526473e-03 3.6068917e-03 9.3991625e-01
  4.8090052e-02 1.3097169e-04 1.8503502e-04]]
Age : (25-32), conf = 0.940
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[5.3828237e-05 6.4389933e-05 7.9526473e-03 3.6068917e-03 9.3991625e-01
  4.8090052e-02 1.3097169e-04 1.8503502e-04]]
Age : (25-32), conf = 0.940
time : 0.100
Gender : Male, conf = 0.995
Age Output : [[7.9121476e-04 3.3363226e-04 9.5979311e-03 1.9508195e-03 9.1331768e-01
  7.3036015e-02 3.7540661e-04 5.9730583e-04]]
Age : (25-32), conf = 0.913
time : 0.094
Gender : Male, conf = 0.995
Age Output : [[4.3441245e-04 2.8409128e-04 8.4363688e-03 3.1249775e-03 9.7088182e-01
  1.6577514e-02 9.4286937e-05 1.6657708e-04]]
Age : (25-32), conf = 0.971
time : 0.083
Gender : Male, conf = 0.996
Age Output : [[1.4754759e-04 1.5175683e-04 1.4686047e-02 3.9663333e-03 9.3143314e-01
  4.9401466e-02 8.5574815e-05 1.2815988e-04]]
Age : (25-32), conf = 0.931
time : 0.081
Gender : Male, conf = 0.996
Age Output : [[1.9862343e-04 2.0140698e-04 5.7667359e-03 3.2086796e-03 9.7358322e-01
  1.6786791e-02 1.3099480e-04 1.2349593e-04]]
Age : (25-32), conf = 0.974
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[7.1723090e-04 5.5235293e-04 6.1706547e-03 6.7495257e-03 9.6047103e-01
  2.4942910e-02 1.7009783e-04 2.2611152e-04]]
Age : (25-32), conf = 0.960
time : 0.098
Gender : Male, conf = 0.971
Age Output : [[1.4106575e-03 1.4469217e-03 1.8570289e-02 1.1155411e-02 9.2145741e-01
  4.4901524e-02 5.3271552e-04 5.2506133e-04]]
Age : (25-32), conf = 0.921
time : 0.099
Gender : Male, conf = 0.997
Age Output : [[2.3013208e-04 3.4336312e-04 1.5394147e-02 6.2128878e-03 9.4769484e-01
  2.9647354e-02 2.2548923e-04 2.5182794e-04]]
Age : (25-32), conf = 0.948
time : 0.095
Gender : Male, conf = 0.997
Age Output : [[2.3013208e-04 3.4336312e-04 1.5394147e-02 6.2128878e-03 9.4769484e-01
  2.9647354e-02 2.2548923e-04 2.5182794e-04]]
Age : (25-32), conf = 0.948
time : 0.079
Gender : Male, conf = 0.995
Age Output : [[4.8228558e-03 2.2739980e-03 2.4665529e-02 5.7841022e-03 9.2763847e-01
  3.3915579e-02 3.9055292e-04 5.0882407e-04]]
Age : (25-32), conf = 0.928
time : 0.084
Gender : Male, conf = 0.995
Age Output : [[1.9010169e-04 4.0397613e-04 1.9512177e-02 1.9514438e-02 9.2361647e-01
  3.6364742e-02 1.9822705e-04 1.9991727e-04]]
Age : (25-32), conf = 0.924
time : 0.094
Gender : Male, conf = 0.994
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[2.4787249e-04 1.6362261e-04 4.6431241e-03 3.5655908e-03 9.6396780e-01
  2.6924698e-02 1.7967670e-04 3.0763037e-04]]
Age : (25-32), conf = 0.964
time : 0.080
Gender : Male, conf = 0.996
Age Output : [[1.01581165e-04 1.62983008e-04 7.99567997e-03 5.30421874e-03
  9.46604252e-01 3.94765437e-02 1.65440259e-04 1.89348706e-04]]
Age : (25-32), conf = 0.947
time : 0.082
Gender : Male, conf = 0.997
Age Output : [[4.5672469e-04 3.4965109e-04 1.6578270e-02 4.9830908e-03 9.4024783e-01
  3.7052862e-02 1.2862745e-04 2.0294325e-04]]
Age : (25-32), conf = 0.940
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[4.5672469e-04 3.4965109e-04 1.6578270e-02 4.9830908e-03 9.4024783e-01
  3.7052862e-02 1.2862745e-04 2.0294325e-04]]
Age : (25-32), conf = 0.940
time : 0.101
Gender : Male, conf = 0.991
Age Output : [[5.1399245e-04 3.4062870e-04 9.2211310e-03 5.1687467e-03 9.5009118e-01
  3.4166742e-02 2.0559931e-04 2.9203642e-04]]
Age : (25-32), conf = 0.950
time : 0.103
Gender : Male, conf = 0.997
Age Output : [[2.4217840e-04 2.1238010e-04 1.7969038e-02 5.9767999e-03 9.1588140e-01
  5.9421740e-02 1.3177890e-04 1.6466726e-04]]
Age : (25-32), conf = 0.916
time : 0.098
Gender : Male, conf = 0.989
Age Output : [[2.2974471e-03 9.9648535e-04 3.2222502e-02 1.2083933e-02 8.2651693e-01
  1.2496534e-01 3.1119669e-04 6.0617144e-04]]
Age : (25-32), conf = 0.827
time : 0.105
Gender : Male, conf = 0.995
Age Output : [[4.1092717e-05 1.2987970e-04 2.8385885e-02 5.7634793e-02 8.5947812e-01
  5.3923290e-02 1.5021804e-04 2.5663630e-04]]
Age : (25-32), conf = 0.859
time : 0.104
Gender : Male, conf = 0.991
Age Output : [[2.4908799e-04 2.6074742e-04 1.6047606e-02 1.1407038e-02 8.4501463e-01
  1.2657741e-01 1.7377838e-04 2.6975301e-04]]
Age : (25-32), conf = 0.845
time : 0.108
Gender : Male, conf = 0.996
Age Output : [[7.4269069e-06 3.0803290e-05 1.3506880e-02 9.5653897e-03 9.5410919e-01
  2.2659397e-02 6.4429878e-05 5.6660516e-05]]
Age : (25-32), conf = 0.954
time : 0.102
Gender : Male, conf = 0.991
Age Output : [[2.8832248e-05 8.9660236e-05 2.8043756e-02 8.2813110e-03 8.9280212e-01
  7.0429437e-02 1.6002443e-04 1.6486279e-04]]
Age : (25-32), conf = 0.893
time : 0.102
Gender : Male, conf = 0.994
Age Output : [[3.3188771e-04 5.0173909e-04 2.9271867e-02 1.2807930e-02 8.9943159e-01
  5.7335559e-02 1.5530038e-04 1.6419741e-04]]
Age : (25-32), conf = 0.899
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[8.3514242e-05 9.5454525e-05 7.9687620e-03 2.7752428e-03 9.6680176e-01
  2.2122754e-02 6.0891154e-05 9.1648493e-05]]
Age : (25-32), conf = 0.967
time : 0.081
Gender : Male, conf = 0.998
Age Output : [[8.3514242e-05 9.5454525e-05 7.9687620e-03 2.7752428e-03 9.6680176e-01
  2.2122754e-02 6.0891154e-05 9.1648493e-05]]
Age : (25-32), conf = 0.967
time : 0.089
Gender : Male, conf = 0.989
Age Output : [[1.6763701e-05 7.1133945e-05 8.5768253e-03 6.0935901e-03 9.6310711e-01
  2.1973358e-02 8.7260189e-05 7.3930154e-05]]
Age : (25-32), conf = 0.963
time : 0.083
Gender : Male, conf = 0.998
Age Output : [[2.1656691e-04 9.5699485e-05 5.0035869e-03 3.0344438e-03 9.1247278e-01
  7.8767985e-02 1.6098752e-04 2.4795110e-04]]
Age : (25-32), conf = 0.912
time : 0.085
Gender : Male, conf = 0.996
Age Output : [[2.0468072e-04 2.1476598e-04 1.5830347e-02 3.3483261e-03 9.6415848e-01
  1.6095296e-02 5.8693320e-05 8.9467620e-05]]
Age : (25-32), conf = 0.964
time : 0.102
Gender : Male, conf = 0.994
Age Output : [[1.5528369e-04 1.5710662e-04 1.6134433e-02 5.5561308e-03 9.3131971e-01
  4.6497889e-02 6.5375956e-05 1.1396801e-04]]
Age : (25-32), conf = 0.931
time : 0.093
Gender : Male, conf = 0.997
Age Output : [[7.3545158e-04 9.5126819e-04 2.2076180e-02 1.0971614e-02 9.3356687e-01
  3.1460680e-02 9.5676165e-05 1.4225666e-04]]
Age : (25-32), conf = 0.934
time : 0.100
Gender : Male, conf = 0.982
Age Output : [[9.1688002e-05 9.8637312e-05 1.7429153e-02 5.4716924e-03 9.2578077e-01
  5.0915983e-02 6.8732923e-05 1.4329367e-04]]
Age : (25-32), conf = 0.926
time : 0.105
Gender : Male, conf = 0.982
Age Output : [[9.1688002e-05 9.8637312e-05 1.7429153e-02 5.4716924e-03 9.2578077e-01
  5.0915983e-02 6.8732923e-05 1.4329367e-04]]
Age : (25-32), conf = 0.926
time : 0.103
Gender : Male, conf = 0.992
Age Output : [[2.1301299e-05 5.0652343e-05 1.4195212e-02 4.4766627e-03 9.6424264e-01
  1.6942296e-02 2.8782886e-05 4.2482199e-05]]
Age : (25-32), conf = 0.964
time : 0.102
Gender : Male, conf = 0.974
Age Output : [[1.79673824e-03 1.21256604e-03 2.51934752e-02 1.33430287e-02
  8.39351833e-01 1.18546575e-01 1.75948153e-04 3.79927718e-04]]
Age : (25-32), conf = 0.839
time : 0.109
Gender : Male, conf = 0.992
Age Output : [[4.4806546e-04 2.9281850e-04 3.5574324e-02 6.0949507e-03 9.2991036e-01
  2.7419172e-02 8.5567088e-05 1.7470440e-04]]
Age : (25-32), conf = 0.930
time : 0.100
Gender : Male, conf = 0.993
Age Output : [[1.6948946e-03 5.6397979e-04 6.1464566e-03 1.9514789e-03 9.4177169e-01
  4.6816718e-02 4.4130706e-04 6.1343674e-04]]
Age : (25-32), conf = 0.942
time : 0.102
Gender : Male, conf = 0.995
Age Output : [[1.3473911e-04 2.5099469e-04 3.6921445e-02 1.0292263e-02 9.3106508e-01
  2.1057649e-02 8.5719847e-05 1.9208564e-04]]
Age : (25-32), conf = 0.931
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[1.2618093e-03 6.4466888e-04 1.0695429e-02 7.8415871e-03 9.6130854e-01
  1.7884526e-02 8.9967201e-05 2.7340555e-04]]
Age : (25-32), conf = 0.961
time : 0.105
Gender : Male, conf = 0.999
Age Output : [[5.1535119e-04 2.2316526e-04 1.0954656e-02 5.3085247e-03 9.4162810e-01
  4.1026413e-02 9.6016513e-05 2.4777994e-04]]
Age : (25-32), conf = 0.942
time : 0.098
Gender : Male, conf = 0.997
Age Output : [[3.0724186e-04 3.0399993e-04 5.4027927e-03 4.2641414e-03 9.7949731e-01
  1.0047980e-02 6.3403844e-05 1.1319709e-04]]
Age : (25-32), conf = 0.979
time : 0.105
Gender : Male, conf = 0.999
Age Output : [[1.4990370e-04 4.6600302e-04 1.7345035e-02 6.3603860e-03 9.6516055e-01
  1.0388534e-02 3.8704056e-05 9.0869784e-05]]
Age : (25-32), conf = 0.965
time : 0.105
Gender : Male, conf = 0.999
Age Output : [[1.4990370e-04 4.6600302e-04 1.7345035e-02 6.3603860e-03 9.6516055e-01
  1.0388534e-02 3.8704056e-05 9.0869784e-05]]
Age : (25-32), conf = 0.965
time : 0.098
Gender : Male, conf = 0.998
Age Output : [[7.2987847e-02 2.0666800e-02 2.3175076e-02 6.2011988e-03 8.4971583e-01
  2.5918495e-02 4.0462278e-04 9.3012472e-04]]
Age : (25-32), conf = 0.850
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[2.4220899e-03 1.0657099e-03 2.5307185e-03 1.4241599e-03 9.7660512e-01
  1.5470368e-02 1.3463647e-04 3.4728620e-04]]
Age : (25-32), conf = 0.977
time : 0.147
Gender : Male, conf = 0.999
Age Output : [[1.0334207e-02 3.5243086e-03 9.1807768e-03 3.2529174e-03 9.5493114e-01
  1.7949304e-02 1.8876772e-04 6.3859450e-04]]
Age : (25-32), conf = 0.955
time : 0.127
Gender : Male, conf = 0.999
Age Output : [[9.4969571e-02 2.0501794e-02 2.0792868e-02 7.8004878e-03 7.9400712e-01
  6.0063340e-02 4.0727915e-04 1.4575646e-03]]
Age : (25-32), conf = 0.794
time : 0.168
Gender : Male, conf = 0.999
Age Output : [[1.50243165e-02 2.10519973e-03 3.44348955e-03 1.63116399e-03
  9.65857446e-01 1.10925296e-02 2.40839596e-04 6.05095527e-04]]
Age : (25-32), conf = 0.966
time : 0.134
Gender : Male, conf = 0.999
Age Output : [[9.7992760e-04 1.6802517e-04 9.4929262e-04 9.6887787e-04 9.7970301e-01
  1.6861012e-02 8.9922236e-05 2.7997003e-04]]
Age : (25-32), conf = 0.980
time : 0.129
Gender : Male, conf = 0.999
Age Output : [[8.4738247e-03 1.1033396e-03 2.1835573e-03 1.4268300e-03 9.7701550e-01
  9.1437800e-03 1.3246540e-04 5.2076980e-04]]
Age : (25-32), conf = 0.977
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[7.0807990e-03 1.1534080e-03 3.8496775e-03 3.1349692e-03 9.5703173e-01
  2.6258815e-02 3.2435762e-04 1.1662157e-03]]
Age : (25-32), conf = 0.957
time : 0.113
Gender : Male, conf = 0.999
Age Output : [[3.6250863e-02 5.2534398e-03 2.6372133e-03 2.7041517e-03 9.4436169e-01
  8.0632679e-03 2.2040898e-04 5.0897012e-04]]
Age : (25-32), conf = 0.944
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[3.6250863e-02 5.2534398e-03 2.6372133e-03 2.7041517e-03 9.4436169e-01
  8.0632679e-03 2.2040898e-04 5.0897012e-04]]
Age : (25-32), conf = 0.944
time : 0.110
Gender : Male, conf = 0.998
Age Output : [[1.0137776e-02 1.3449719e-03 4.9677077e-03 2.9337984e-03 9.4623691e-01
  3.3538990e-02 1.9864744e-04 6.4117945e-04]]
Age : (25-32), conf = 0.946
time : 0.102
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.998
Age Output : [[7.5789476e-03 2.9310181e-03 4.7063516e-03 3.1443101e-03 9.6201032e-01
  1.9033650e-02 1.1853620e-04 4.7684426e-04]]
Age : (25-32), conf = 0.962
time : 0.114
Gender : Male, conf = 0.998
Age Output : [[1.0282424e-02 2.2280344e-03 8.8459291e-03 4.0169153e-03 9.3153781e-01
  4.1276798e-02 3.2845087e-04 1.4836128e-03]]
Age : (25-32), conf = 0.932
time : 0.105
Gender : Male, conf = 0.999
Age Output : [[3.4731142e-03 1.1611376e-03 3.7288591e-03 2.5715036e-03 9.4624025e-01
  4.2017434e-02 1.7217211e-04 6.3556706e-04]]
Age : (25-32), conf = 0.946
time : 0.134
Gender : Male, conf = 0.999
Age Output : [[4.6792636e-03 8.8040828e-04 5.4420354e-03 1.9324452e-03 9.6539283e-01
  2.1024782e-02 1.5525879e-04 4.9302098e-04]]
Age : (25-32), conf = 0.965
time : 0.115
Gender : Male, conf = 0.999
Age Output : [[2.0763388e-02 6.1696391e-03 1.0567207e-02 5.6041949e-03 9.3211573e-01
  2.3778459e-02 2.6663073e-04 7.3470280e-04]]
Age : (25-32), conf = 0.932
time : 0.103
Gender : Male, conf = 0.998
Age Output : [[5.4965746e-03 9.5170795e-04 4.9772789e-03 3.7342834e-03 9.5123571e-01
  3.2914076e-02 1.6487211e-04 5.2562513e-04]]
Age : (25-32), conf = 0.951
time : 0.121
Gender : Male, conf = 0.999
Age Output : [[8.8860067e-03 1.6863802e-03 8.6107114e-03 3.5816326e-03 9.5431679e-01
  2.1978021e-02 2.2692779e-04 7.1346381e-04]]
Age : (25-32), conf = 0.954
time : 0.117
Gender : Male, conf = 0.998
Age Output : [[1.3606841e-02 3.3748003e-03 5.5547771e-03 3.2147537e-03 9.5075542e-01
  2.2784572e-02 1.9550565e-04 5.1330501e-04]]
Age : (25-32), conf = 0.951
time : 0.110
Gender : Male, conf = 0.999
Age Output : [[6.2359357e-04 5.5695209e-04 3.9589959e-03 2.0077417e-03 9.8072207e-01
  1.1896806e-02 6.0640461e-05 1.7331808e-04]]
Age : (25-32), conf = 0.981
time : 0.103
Gender : Male, conf = 0.998
Age Output : [[1.0375460e-02 3.4915884e-03 4.1728946e-03 2.7437580e-03 9.6576691e-01
  1.2944171e-02 1.6436442e-04 3.4090830e-04]]
Age : (25-32), conf = 0.966
time : 0.104
Gender : Male, conf = 0.999
Age Output : [[1.3760690e-04 8.2487852e-05 7.3369505e-04 1.6354906e-03 9.8890215e-01
  8.3712125e-03 3.4710185e-05 1.0265180e-04]]
Age : (25-32), conf = 0.989
time : 0.121
Gender : Male, conf = 0.999
Age Output : [[2.2550434e-02 2.4039308e-03 5.6231795e-03 4.4290405e-03 9.2507327e-01
  3.8288031e-02 3.5896566e-04 1.2731460e-03]]
Age : (25-32), conf = 0.925
time : 0.134
Gender : Male, conf = 0.998
Age Output : [[7.1453699e-03 1.6293073e-03 5.0997757e-03 3.3319225e-03 9.2504656e-01
  5.6725010e-02 2.7212023e-04 7.4987701e-04]]
Age : (25-32), conf = 0.925
time : 0.113
Gender : Male, conf = 0.996
Age Output : [[1.0905343e-02 1.9528031e-03 4.0251086e-03 2.0471956e-03 9.5803839e-01
  2.2080483e-02 2.6867923e-04 6.8194774e-04]]
Age : (25-32), conf = 0.958
time : 0.106
Gender : Male, conf = 0.997
Age Output : [[1.9788941e-02 7.9347389e-03 1.3420881e-02 4.3360400e-03 9.3179911e-01
  2.1887679e-02 1.9934570e-04 6.3328736e-04]]
Age : (25-32), conf = 0.932
time : 0.104
Gender : Male, conf = 0.997
Age Output : [[3.6366212e-03 1.0362135e-03 5.9239217e-03 2.5464017e-03 9.6243829e-01
  2.3940001e-02 1.1836159e-04 3.6018214e-04]]
Age : (25-32), conf = 0.962
time : 0.129
Gender : Male, conf = 0.996
Age Output : [[5.3372208e-02 7.9460312e-03 1.3747879e-02 7.6043615e-03 8.5513437e-01
  6.0088128e-02 4.7980421e-04 1.6272718e-03]]
Age : (25-32), conf = 0.855
time : 0.154
Gender : Male, conf = 0.997
Age Output : [[2.6404471e-03 7.1692292e-04 2.7265467e-03 1.5408422e-03 9.8375976e-01
  8.2798619e-03 9.7839846e-05 2.3781853e-04]]
Age : (25-32), conf = 0.984
time : 0.145
Gender : Male, conf = 0.997
Age Output : [[1.9411692e-02 2.4441942e-03 5.9332489e-03 3.1988511e-03 9.2408234e-01
  4.3357261e-02 4.5211209e-04 1.1203395e-03]]
Age : (25-32), conf = 0.924
time : 0.148
Gender : Male, conf = 0.999
Age Output : [[3.7581141e-03 1.0187234e-03 4.4364510e-03 3.1068686e-03 9.3232697e-01
  5.4004669e-02 3.8042470e-04 9.6773496e-04]]
Age : (25-32), conf = 0.932
time : 0.155
Gender : Male, conf = 0.995
Age Output : [[6.6021448e-03 1.5709497e-03 7.8254398e-03 2.7806305e-03 9.6030194e-01
  1.9795056e-02 2.7289693e-04 8.5102936e-04]]
Age : (25-32), conf = 0.960
time : 0.139
Gender : Male, conf = 0.998
Age Output : [[1.1931599e-02 3.1829430e-03 6.2741893e-03 3.7714902e-03 9.4678819e-01
  2.7020542e-02 2.6441886e-04 7.6653314e-04]]
Age : (25-32), conf = 0.947
time : 0.170
Gender : Male, conf = 0.999
Age Output : [[0.27691323 0.06835751 0.01018604 0.00608068 0.6090803  0.02754344
  0.00072364 0.00111519]]
Age : (25-32), conf = 0.609
time : 0.156
Gender : Male, conf = 0.999
Age Output : [[3.6893139e-04 4.4728187e-04 3.9017305e-03 3.2576388e-03 9.7815847e-01
  1.3708391e-02 4.7625872e-05 1.0993357e-04]]
Age : (25-32), conf = 0.978
time : 0.150
Gender : Male, conf = 0.999
Age Output : [[2.1684861e-03 1.1433861e-03 1.1375982e-03 3.2344910e-03 9.8336780e-01
  8.6163227e-03 1.2154949e-04 2.1037812e-04]]
Age : (25-32), conf = 0.983
time : 0.186
Gender : Male, conf = 0.998
Age Output : [[3.3608184e-03 2.3946415e-03 5.7421434e-03 5.4070121e-03 9.6081263e-01
  2.1820491e-02 1.5873621e-04 3.0349800e-04]]
Age : (25-32), conf = 0.961
time : 0.129
Gender : Male, conf = 0.998
Age Output : [[8.4002601e-04 6.0257834e-04 2.4980146e-03 2.3070271e-03 9.7826171e-01
  1.5243197e-02 8.2506514e-05 1.6487027e-04]]
Age : (25-32), conf = 0.978
time : 0.123
Gender : Male, conf = 0.999
Age Output : [[6.9534709e-04 4.8543562e-04 2.6874151e-03 2.6492074e-03 9.8104799e-01
  1.2218454e-02 6.6973531e-05 1.4915034e-04]]
Age : (25-32), conf = 0.981
time : 0.113
Gender : Male, conf = 0.997
Age Output : [[2.45827425e-04 1.14710245e-04 8.46416166e-04 1.43697415e-03
  9.86918747e-01 1.02757923e-02 5.98041770e-05 1.01809717e-04]]
Age : (25-32), conf = 0.987
time : 0.125
Gender : Male, conf = 0.994
Age Output : [[1.2551590e-03 5.5794150e-04 1.1055911e-03 1.4520967e-03 9.7899103e-01
  1.6303614e-02 1.3603691e-04 1.9839233e-04]]
Age : (25-32), conf = 0.979
time : 0.126
Gender : Male, conf = 0.987
Age Output : [[2.6465547e-03 2.0425075e-03 2.2920060e-03 2.3258883e-03 9.7998446e-01
  1.0461574e-02 8.4902655e-05 1.6211247e-04]]
Age : (25-32), conf = 0.980
time : 0.148
Gender : Male, conf = 0.992
Age Output : [[1.1465824e-03 8.5682649e-04 2.1687658e-03 3.1356702e-03 9.7906059e-01
  1.3424006e-02 6.4332104e-05 1.4318632e-04]]
Age : (25-32), conf = 0.979
time : 0.140
Gender : Male, conf = 0.991
Age Output : [[6.6380855e-04 4.9288094e-04 1.3444071e-03 2.2415614e-03 9.8707378e-01
  8.0385245e-03 4.6320740e-05 9.8718658e-05]]
Age : (25-32), conf = 0.987
time : 0.122
Gender : Male, conf = 0.997
Age Output : [[1.2855555e-04 1.2814476e-04 8.3799969e-04 1.6488372e-03 9.8959738e-01
  7.5628166e-03 3.8904567e-05 5.7478850e-05]]
Age : (25-32), conf = 0.990
time : 0.129
Gender : Male, conf = 0.991
Age Output : [[1.0295034e-03 5.3044502e-04 2.1939238e-03 2.9382037e-03 9.8499608e-01
  8.1081111e-03 6.7484223e-05 1.3626598e-04]]
Age : (25-32), conf = 0.985
time : 0.125
Gender : Male, conf = 0.998
Age Output : [[3.27374204e-04 2.04460099e-04 2.03978107e-03 3.15398071e-03
  9.80032384e-01 1.40573448e-02 7.07189829e-05 1.14038856e-04]]
Age : (25-32), conf = 0.980
time : 0.109
Gender : Male, conf = 0.987
Age Output : [[1.1401282e-04 1.1390578e-04 8.6683373e-04 1.0223192e-03 9.9175173e-01
  6.0298499e-03 3.6352456e-05 6.4987827e-05]]
Age : (25-32), conf = 0.992
time : 0.127
Gender : Male, conf = 0.988
Age Output : [[4.4931304e-03 1.9579190e-03 3.5789032e-03 2.9769505e-03 9.7828901e-01
  8.3848108e-03 1.1495191e-04 2.0435796e-04]]
Age : (25-32), conf = 0.978
time : 0.111
Gender : Male, conf = 0.998
Age Output : [[1.0465733e-04 1.1721848e-04 1.2556690e-03 1.6451748e-03 9.8643595e-01
  1.0314559e-02 4.9389262e-05 7.7416349e-05]]
Age : (25-32), conf = 0.986
time : 0.093
Gender : Male, conf = 0.997
Age Output : [[2.3977842e-05 3.1854241e-05 5.9862947e-04 7.8374846e-04 9.9384934e-01
  4.6406612e-03 2.7932090e-05 4.3780587e-05]]
Age : (25-32), conf = 0.994
time : 0.091
Gender : Male, conf = 0.996
Age Output : [[7.8148628e-03 3.2749590e-03 6.9693639e-03 8.9258654e-03 9.4435793e-01
  2.8028127e-02 1.8964866e-04 4.3919022e-04]]
Age : (25-32), conf = 0.944
time : 0.093
Gender : Male, conf = 0.996
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[7.8148628e-03 3.2749590e-03 6.9693639e-03 8.9258654e-03 9.4435793e-01
  2.8028127e-02 1.8964866e-04 4.3919022e-04]]
Age : (25-32), conf = 0.944
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[1.7418757e-04 2.3719096e-04 3.4796139e-03 3.8697955e-03 9.7756702e-01
  1.4520089e-02 6.3051601e-05 8.9094261e-05]]
Age : (25-32), conf = 0.978
time : 0.116
Gender : Male, conf = 0.995
Age Output : [[2.6287712e-04 2.9392671e-04 4.2326958e-03 3.0927341e-03 9.7891104e-01
  1.3004751e-02 7.0758288e-05 1.3126337e-04]]
Age : (25-32), conf = 0.979
time : 0.122
Gender : Male, conf = 0.997
Age Output : [[7.2629022e-04 3.8102726e-04 2.4723841e-03 2.9664957e-03 9.8027819e-01
  1.2883650e-02 1.1106755e-04 1.8095775e-04]]
Age : (25-32), conf = 0.980
time : 0.116
Gender : Male, conf = 0.999
Age Output : [[1.6191967e-02 6.1085243e-03 7.3667164e-03 8.6290268e-03 9.3900651e-01
  2.1959659e-02 2.7275522e-04 4.6492633e-04]]
Age : (25-32), conf = 0.939
time : 0.120
Gender : Male, conf = 0.995
Age Output : [[5.4908660e-04 3.6072746e-04 2.4618921e-03 3.2518592e-03 9.8198408e-01
  1.1172594e-02 8.3234729e-05 1.3650370e-04]]
Age : (25-32), conf = 0.982
time : 0.118
Gender : Male, conf = 0.997
Age Output : [[2.3715835e-04 2.8831454e-04 1.5744360e-03 1.8773478e-03 9.9141413e-01
  4.4977418e-03 3.9007453e-05 7.1704017e-05]]
Age : (25-32), conf = 0.991
time : 0.100
Gender : Male, conf = 0.995
Age Output : [[1.2012030e-03 6.7229947e-04 3.9083185e-03 3.2708100e-03 9.8084360e-01
  9.8896511e-03 8.0499762e-05 1.3362007e-04]]
Age : (25-32), conf = 0.981
time : 0.088
Gender : Male, conf = 0.996
Age Output : [[1.84035278e-03 1.85979949e-03 1.08832382e-02 6.53141504e-03
  9.65287626e-01 1.32969152e-02 1.04785955e-04 1.95823814e-04]]
Age : (25-32), conf = 0.965
time : 0.086
Gender : Male, conf = 0.989
Age Output : [[2.7464500e-03 1.0667627e-03 3.0700550e-03 3.9252881e-03 9.7655892e-01
  1.2347328e-02 9.6634576e-05 1.8855536e-04]]
Age : (25-32), conf = 0.977
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[7.2033079e-05 1.0473897e-04 1.8317383e-03 1.7153730e-03 9.8870069e-01
  7.4605774e-03 3.9704195e-05 7.5240619e-05]]
Age : (25-32), conf = 0.989
time : 0.079
Gender : Male, conf = 0.994
Age Output : [[7.33106222e-04 5.62371162e-04 8.00777599e-03 3.91335599e-03
  9.25584972e-01 6.08709306e-02 1.16024064e-04 2.11426450e-04]]
Age : (25-32), conf = 0.926
time : 0.099
Gender : Male, conf = 0.997
Age Output : [[5.0255447e-05 7.6605422e-05 1.8139557e-03 1.3855339e-03 9.8044419e-01
  1.6117940e-02 4.3588720e-05 6.7869085e-05]]
Age : (25-32), conf = 0.980
time : 0.101
Gender : Male, conf = 0.991
Age Output : [[6.2226760e-03 2.4694426e-03 8.2667619e-03 7.4125859e-03 9.4632363e-01
  2.8695608e-02 1.8672168e-04 4.2255016e-04]]
Age : (25-32), conf = 0.946
time : 0.084
Gender : Male, conf = 0.991
Age Output : [[6.2226760e-03 2.4694426e-03 8.2667619e-03 7.4125859e-03 9.4632363e-01
  2.8695608e-02 1.8672168e-04 4.2255016e-04]]
Age : (25-32), conf = 0.946
time : 0.087
Gender : Male, conf = 0.997
Age Output : [[2.6966556e-04 2.4256262e-04 1.3608631e-03 1.8519383e-03 9.8777348e-01
  8.3454698e-03 5.8475824e-05 9.7551158e-05]]
Age : (25-32), conf = 0.988
time : 0.097
Gender : Male, conf = 0.996
Age Output : [[1.73466129e-03 1.42177672e-03 5.48294326e-03 5.04711596e-03
  9.71607089e-01 1.43042505e-02 1.27780382e-04 2.74386606e-04]]
Age : (25-32), conf = 0.972
time : 0.113
Gender : Male, conf = 0.993
Age Output : [[4.4186641e-03 2.6356278e-03 1.1244751e-02 8.2390513e-03 9.4549572e-01
  2.7519081e-02 1.3642274e-04 3.1079346e-04]]
Age : (25-32), conf = 0.945
time : 0.105
Gender : Male, conf = 0.996
Age Output : [[2.8138683e-04 2.2637600e-04 1.4642330e-03 2.1439921e-03 9.8138350e-01
  1.4246977e-02 8.8545770e-05 1.6505731e-04]]
Age : (25-32), conf = 0.981
time : 0.093
Gender : Male, conf = 0.995
Age Output : [[4.7612195e-03 1.2796575e-03 7.4070208e-03 8.0068409e-03 8.4112239e-01
  1.3633919e-01 4.2090981e-04 6.6267751e-04]]
Age : (25-32), conf = 0.841
time : 0.097
Gender : Male, conf = 0.998
Age Output : [[2.5076116e-04 4.5790177e-04 8.0351466e-03 2.3203674e-03 9.7338337e-01
  1.5380679e-02 6.0494793e-05 1.1132118e-04]]
Age : (25-32), conf = 0.973
time : 0.108
Gender : Male, conf = 0.994
Age Output : [[1.6775095e-03 1.0123418e-03 9.7195441e-03 6.4090341e-03 9.3362713e-01
  4.6914756e-02 2.2128593e-04 4.1849242e-04]]
Age : (25-32), conf = 0.934
time : 0.097
Gender : Male, conf = 0.997
Age Output : [[6.8935187e-05 1.4730371e-04 8.0355331e-03 6.5164054e-03 9.6458411e-01
  2.0494109e-02 5.5178814e-05 9.8452270e-05]]
Age : (25-32), conf = 0.965
time : 0.083
Gender : Male, conf = 0.997
Age Output : [[6.8935187e-05 1.4730371e-04 8.0355331e-03 6.5164054e-03 9.6458411e-01
  2.0494109e-02 5.5178814e-05 9.8452270e-05]]
Age : (25-32), conf = 0.965
time : 0.095
Gender : Male, conf = 0.997
Age Output : [[4.4336804e-05 7.3045019e-05 1.9766376e-03 1.2493301e-03 9.7899628e-01
  1.7545264e-02 5.0250954e-05 6.4809348e-05]]
Age : (25-32), conf = 0.979
time : 0.101
Gender : Male, conf = 0.998
Age Output : [[2.1422547e-04 2.1102431e-04 1.8579831e-03 1.5990465e-03 9.8925120e-01
  6.7179189e-03 5.3279084e-05 9.5329073e-05]]
Age : (25-32), conf = 0.989
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[1.2539617e-03 1.1167306e-03 3.0796102e-03 2.9690927e-03 9.7439551e-01
  1.6836163e-02 1.2949281e-04 2.1936654e-04]]
Age : (25-32), conf = 0.974
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[2.6058522e-04 2.4821385e-04 3.7265632e-03 1.6208050e-03 9.7273177e-01
  2.1179480e-02 8.7470624e-05 1.4513770e-04]]
Age : (25-32), conf = 0.973
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[4.3514784e-04 3.4356088e-04 1.5316948e-03 1.8272728e-03 9.8555470e-01
  1.0095839e-02 8.3050298e-05 1.2876790e-04]]
Age : (25-32), conf = 0.986
time : 0.088
Gender : Male, conf = 0.996
Age Output : [[4.3514784e-04 3.4356088e-04 1.5316948e-03 1.8272728e-03 9.8555470e-01
  1.0095839e-02 8.3050298e-05 1.2876790e-04]]
Age : (25-32), conf = 0.986
time : 0.094
Gender : Male, conf = 0.997
Age Output : [[8.1009773e-04 4.3395723e-04 1.8469981e-03 1.5916547e-03 9.8651868e-01
  8.5273013e-03 9.5421899e-05 1.7593843e-04]]
Age : (25-32), conf = 0.987
time : 0.102
Gender : Male, conf = 0.998
Age Output : [[2.2720278e-04 2.7172081e-04 3.0395195e-03 2.7753771e-03 9.7098541e-01
  2.2448463e-02 1.0142857e-04 1.5097127e-04]]
Age : (25-32), conf = 0.971
time : 0.103
Gender : Male, conf = 0.993
Age Output : [[1.2076760e-04 2.0216861e-04 8.4785745e-03 3.4416746e-03 9.4276625e-01
  4.4716116e-02 1.1452698e-04 1.5997552e-04]]
Age : (25-32), conf = 0.943
time : 0.100
Gender : Male, conf = 0.997
Age Output : [[6.5824366e-04 4.3453131e-04 2.1909387e-03 1.9759196e-03 9.8557949e-01
  8.9010391e-03 9.2261376e-05 1.6754560e-04]]
Age : (25-32), conf = 0.986
time : 0.093
Gender : Male, conf = 0.998
Age Output : [[1.7554106e-04 1.9417157e-04 1.3819539e-03 1.6962681e-03 9.8622906e-01
  1.0179926e-02 5.3330768e-05 8.9674802e-05]]
Age : (25-32), conf = 0.986
time : 0.083
Gender : Male, conf = 0.996
Age Output : [[1.9029952e-05 4.4115517e-05 2.1639725e-03 1.5952854e-03 9.7812599e-01
  1.7967822e-02 2.9382420e-05 5.4330529e-05]]
Age : (25-32), conf = 0.978
time : 0.100
Gender : Male, conf = 0.995
Age Output : [[1.1539080e-04 1.4889508e-04 2.7475581e-03 1.6513134e-03 9.7287685e-01
  2.2267323e-02 7.5166907e-05 1.1763414e-04]]
Age : (25-32), conf = 0.973
time : 0.084
Gender : Male, conf = 0.995
Age Output : [[1.1539080e-04 1.4889508e-04 2.7475581e-03 1.6513134e-03 9.7287685e-01
  2.2267323e-02 7.5166907e-05 1.1763414e-04]]
Age : (25-32), conf = 0.973
time : 0.100
Gender : Male, conf = 0.995
Age Output : [[9.3401075e-05 2.0372710e-04 7.7700475e-03 5.6347619e-03 9.7378570e-01
  1.2430736e-02 3.2784825e-05 4.8914233e-05]]
Age : (25-32), conf = 0.974
time : 0.094
Gender : Male, conf = 0.996
Age Output : [[4.8487869e-05 9.3977018e-05 1.4447429e-03 3.4286240e-03 9.7340310e-01
  2.1293381e-02 1.3675413e-04 1.5079555e-04]]
Age : (25-32), conf = 0.973
time : 0.082
Gender : Male, conf = 0.994
Age Output : [[3.0451377e-03 8.6513505e-04 2.0798449e-03 2.1759649e-03 9.6913695e-01
  2.2023991e-02 2.9063501e-04 3.8230658e-04]]
Age : (25-32), conf = 0.969
time : 0.085
Gender : Male, conf = 0.989
Age Output : [[2.4570999e-04 2.0056081e-04 2.0502710e-03 1.4283261e-03 9.7136688e-01
  2.4295991e-02 1.6493135e-04 2.4738998e-04]]
Age : (25-32), conf = 0.971
time : 0.084
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.993
Age Output : [[7.8532772e-05 6.3647218e-05 1.1142973e-03 1.4783852e-03 9.8601598e-01
  1.1104222e-02 5.7550391e-05 8.7289962e-05]]
Age : (25-32), conf = 0.986
time : 0.084
Gender : Male, conf = 0.994
Age Output : [[2.7383337e-04 2.1853292e-04 1.4464362e-03 1.3025581e-03 9.8172289e-01
  1.4802833e-02 8.8097302e-05 1.4475903e-04]]
Age : (25-32), conf = 0.982
time : 0.095
Gender : Male, conf = 0.994
Age Output : [[2.7383337e-04 2.1853292e-04 1.4464362e-03 1.3025581e-03 9.8172289e-01
  1.4802833e-02 8.8097302e-05 1.4475903e-04]]
Age : (25-32), conf = 0.982
time : 0.100
Gender : Male, conf = 0.995
Age Output : [[7.1993876e-05 1.1236521e-04 2.2834071e-03 2.4007724e-03 9.8599654e-01
  9.0182526e-03 5.2744079e-05 6.3908839e-05]]
Age : (25-32), conf = 0.986
time : 0.098
Gender : Male, conf = 0.992
Age Output : [[6.1469102e-05 1.2502083e-04 1.0467990e-02 6.0555637e-03 9.6198124e-01
  2.1166127e-02 4.9473227e-05 9.3123148e-05]]
Age : (25-32), conf = 0.962
time : 0.104
Gender : Male, conf = 0.996
Age Output : [[7.0813971e-05 1.3831157e-04 5.2830442e-03 3.2390789e-03 9.6451038e-01
  2.6651936e-02 3.7335350e-05 6.9075737e-05]]
Age : (25-32), conf = 0.965
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[2.3852857e-05 5.0298528e-05 2.6054091e-03 3.6476885e-03 9.6797848e-01
  2.5596716e-02 3.8233848e-05 5.9293572e-05]]
Age : (25-32), conf = 0.968
time : 0.101
Gender : Male, conf = 0.998
Age Output : [[2.0730415e-05 4.0324514e-05 2.0112046e-03 3.8148894e-03 9.7761154e-01
  1.6403034e-02 3.1041785e-05 6.7247362e-05]]
Age : (25-32), conf = 0.978
time : 0.087
Gender : Male, conf = 0.998
Age Output : [[3.2340580e-05 8.9094210e-05 6.1321352e-03 5.9347046e-03 9.4971442e-01
  3.7936345e-02 7.4976924e-05 8.6074841e-05]]
Age : (25-32), conf = 0.950
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[2.4943085e-05 3.7761416e-05 1.5840222e-03 2.5449197e-03 9.7792405e-01
  1.7782377e-02 3.6293848e-05 6.5680695e-05]]
Age : (25-32), conf = 0.978
time : 0.084
Gender : Male, conf = 0.993
Age Output : [[6.0080052e-05 6.0949922e-05 2.9197072e-03 2.0413720e-03 9.7442496e-01
  2.0350406e-02 5.3471220e-05 8.9132103e-05]]
Age : (25-32), conf = 0.974
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[2.8597176e-04 5.3806423e-04 7.7473302e-03 7.8885686e-03 9.5968866e-01
  2.3640534e-02 8.0072343e-05 1.3076108e-04]]
Age : (25-32), conf = 0.960
time : 0.084
Gender : Male, conf = 0.991
Age Output : [[3.9210474e-05 3.3611846e-05 7.6646410e-04 1.0820257e-03 9.6865529e-01
  2.9245082e-02 7.4356474e-05 1.0386931e-04]]
Age : (25-32), conf = 0.969
time : 0.085
Gender : Male, conf = 0.998
Age Output : [[4.8359347e-05 1.1176106e-04 2.1969606e-03 2.3911777e-03 9.8350775e-01
  1.1650298e-02 3.6356760e-05 5.7329318e-05]]
Age : (25-32), conf = 0.984
time : 0.085
Gender : Male, conf = 0.993
Age Output : [[1.19619224e-04 3.39390157e-04 1.02796964e-02 9.15134232e-03
  9.56841648e-01 2.30460577e-02 8.37213811e-05 1.38509000e-04]]
Age : (25-32), conf = 0.957
time : 0.085
Gender : Male, conf = 0.993
Age Output : [[1.19619224e-04 3.39390157e-04 1.02796964e-02 9.15134232e-03
  9.56841648e-01 2.30460577e-02 8.37213811e-05 1.38509000e-04]]
Age : (25-32), conf = 0.957
time : 0.101
Gender : Male, conf = 0.993
Age Output : [[1.7332262e-05 4.2943033e-05 4.1747699e-03 2.7115673e-03 9.6970505e-01
  2.3230070e-02 3.9753559e-05 7.8535995e-05]]
Age : (25-32), conf = 0.970
time : 0.100
Gender : Male, conf = 0.991
Age Output : [[4.1505937e-05 4.3603141e-05 2.9058242e-03 1.6695362e-03 9.7065395e-01
  2.4554711e-02 5.7738660e-05 7.3104915e-05]]
Age : (25-32), conf = 0.971
time : 0.099
Gender : Male, conf = 0.994
Age Output : [[8.9241592e-05 5.6999033e-05 2.4609265e-03 2.1676535e-03 9.7508889e-01
  1.9969668e-02 5.5521487e-05 1.1107289e-04]]
Age : (25-32), conf = 0.975
time : 0.095
Gender : Male, conf = 0.994
Age Output : [[8.9241592e-05 5.6999033e-05 2.4609265e-03 2.1676535e-03 9.7508889e-01
  1.9969668e-02 5.5521487e-05 1.1107289e-04]]
Age : (25-32), conf = 0.975
time : 0.100
Gender : Male, conf = 0.990
Age Output : [[3.35648838e-05 4.72238353e-05 1.86797313e-03 1.99021515e-03
  9.70862806e-01 2.50288863e-02 6.26927504e-05 1.06552056e-04]]
Age : (25-32), conf = 0.971
time : 0.088
Gender : Male, conf = 0.990
Age Output : [[1.8520899e-04 1.1947469e-04 9.6901157e-04 1.6210675e-03 9.8456109e-01
  1.2340238e-02 6.9318303e-05 1.3450385e-04]]
Age : (25-32), conf = 0.985
time : 0.112
Gender : Male, conf = 0.994
Age Output : [[2.0669709e-04 2.2002854e-04 3.7029868e-03 1.8973001e-03 9.7329921e-01
  2.0444779e-02 8.5693624e-05 1.4323540e-04]]
Age : (25-32), conf = 0.973
time : 0.096
Gender : Male, conf = 0.996
Age Output : [[1.3467945e-04 1.2719361e-04 2.2252658e-03 2.7687743e-03 9.7180980e-01
  2.2752024e-02 5.9789865e-05 1.2247871e-04]]
Age : (25-32), conf = 0.972
time : 0.097
Gender : Male, conf = 0.996
Age Output : [[3.1253963e-05 2.9648592e-05 8.7846379e-04 1.3361967e-03 9.8374093e-01
  1.3875126e-02 4.2059648e-05 6.6245200e-05]]
Age : (25-32), conf = 0.984
time : 0.083
Gender : Male, conf = 0.998
Age Output : [[1.09790824e-04 2.14941756e-04 1.11525282e-02 8.13370105e-03
  9.34564710e-01 4.55687270e-02 9.98277246e-05 1.55786402e-04]]
Age : (25-32), conf = 0.935
time : 0.095
Gender : Male, conf = 0.998
Age Output : [[1.09790824e-04 2.14941756e-04 1.11525282e-02 8.13370105e-03
  9.34564710e-01 4.55687270e-02 9.98277246e-05 1.55786402e-04]]
Age : (25-32), conf = 0.935
time : 0.104
Gender : Male, conf = 0.998
Age Output : [[1.8487617e-04 3.0719381e-04 7.2796652e-03 5.6324401e-03 9.5739788e-01
  2.9039141e-02 6.5847998e-05 9.2849943e-05]]
Age : (25-32), conf = 0.957
time : 0.112
Gender : Male, conf = 0.998
Age Output : [[3.11133626e-04 4.30197979e-04 6.17227703e-03 3.01750167e-03
  9.62889671e-01 2.70009972e-02 7.15678834e-05 1.06725056e-04]]
Age : (25-32), conf = 0.963
time : 0.108
Gender : Male, conf = 0.997
Age Output : [[3.0654471e-03 2.2154138e-03 5.2402145e-03 8.4074633e-03 9.5322078e-01
  2.7479198e-02 1.3082757e-04 2.4063357e-04]]
Age : (25-32), conf = 0.953
time : 0.098
Gender : Male, conf = 0.992
Age Output : [[6.4837199e-04 4.2543153e-04 3.3253310e-03 3.5700118e-03 9.8013866e-01
  1.1743446e-02 4.7374804e-05 1.0138480e-04]]
Age : (25-32), conf = 0.980
time : 0.097
Gender : Male, conf = 0.995
Age Output : [[1.7240364e-04 1.7671878e-04 5.9798043e-03 7.0038084e-03 9.6161276e-01
  2.4879800e-02 6.9861075e-05 1.0484318e-04]]
Age : (25-32), conf = 0.962
time : 0.082
Gender : Male, conf = 0.991
Age Output : [[9.8227290e-04 8.8737020e-04 9.8668570e-03 1.5351857e-02 9.5418721e-01
  1.8352140e-02 1.3895288e-04 2.3334385e-04]]
Age : (25-32), conf = 0.954
time : 0.086
Gender : Male, conf = 0.995
Age Output : [[3.6693370e-04 2.4774898e-04 8.1491992e-03 4.0879264e-03 9.7241479e-01
  1.4440236e-02 1.0849766e-04 1.8461038e-04]]
Age : (25-32), conf = 0.972
time : 0.084
Gender : Male, conf = 0.995
Age Output : [[1.4715337e-02 5.0414517e-03 2.3513336e-02 1.6119642e-02 9.1632271e-01
  2.3320209e-02 2.9457311e-04 6.7277887e-04]]
Age : (25-32), conf = 0.916
time : 0.084
Gender : Male, conf = 0.995
Age Output : [[1.4715337e-02 5.0414517e-03 2.3513336e-02 1.6119642e-02 9.1632271e-01
  2.3320209e-02 2.9457311e-04 6.7277887e-04]]
Age : (25-32), conf = 0.916
time : 0.118
Gender : Male, conf = 0.997
Age Output : [[2.2699079e-02 3.5853416e-03 1.6380088e-02 7.1817595e-03 8.6917412e-01
  7.8954294e-02 4.5855335e-04 1.5667103e-03]]
Age : (25-32), conf = 0.869
time : 0.081
Gender : Male, conf = 0.998
Age Output : [[3.1924743e-02 2.2977153e-03 9.2028165e-03 5.7996446e-03 8.2348812e-01
  1.2339564e-01 7.3977350e-04 3.1515574e-03]]
Age : (25-32), conf = 0.823
time : 0.082
Gender : Male, conf = 0.999
Age Output : [[2.4476206e-02 5.4194354e-03 2.3930263e-02 5.3978977e-03 9.1106725e-01
  2.8089687e-02 2.8186708e-04 1.3374642e-03]]
Age : (25-32), conf = 0.911
time : 0.107
Gender : Male, conf = 0.999
Age Output : [[3.8723417e-02 5.7216147e-03 5.5666314e-03 3.0939693e-03 9.2423415e-01
  2.1410726e-02 2.7411350e-04 9.7529375e-04]]
Age : (25-32), conf = 0.924
time : 0.103
Gender : Male, conf = 0.999
Age Output : [[4.2517221e-01 2.7327221e-02 1.1316304e-02 4.1421554e-03 5.0503987e-01
  2.5283717e-02 3.6216079e-04 1.3564092e-03]]
Age : (25-32), conf = 0.505
time : 0.104
Gender : Male, conf = 0.996
Age Output : [[3.8463149e-02 5.4672281e-03 9.5404815e-03 3.3203936e-03 9.1896498e-01
  2.3348391e-02 2.3330959e-04 6.6204928e-04]]
Age : (25-32), conf = 0.919
time : 0.104
Gender : Male, conf = 0.995
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[1.8886009e-02 6.7081382e-03 9.5109083e-03 8.2544405e-03 9.4064021e-01
  1.5185775e-02 2.7286314e-04 5.4169656e-04]]
Age : (25-32), conf = 0.941
time : 0.087
Gender : Male, conf = 0.995
Age Output : [[1.8886009e-02 6.7081382e-03 9.5109083e-03 8.2544405e-03 9.4064021e-01
  1.5185775e-02 2.7286314e-04 5.4169656e-04]]
Age : (25-32), conf = 0.941
time : 0.095
Gender : Male, conf = 0.997
Age Output : [[6.1793402e-02 1.4517127e-02 1.2213674e-02 6.7889774e-03 8.7209702e-01
  3.1310290e-02 4.5312577e-04 8.2643278e-04]]
Age : (25-32), conf = 0.872
time : 0.121
Gender : Male, conf = 0.997
Age Output : [[3.7925515e-02 1.5229617e-02 2.7906327e-02 7.9561286e-03 8.8013971e-01
  2.9636845e-02 3.4938173e-04 8.5647166e-04]]
Age : (25-32), conf = 0.880
time : 0.098
Gender : Male, conf = 0.986
Age Output : [[2.5863891e-02 4.1157193e-03 1.7677413e-02 5.1982175e-03 8.9962655e-01
  4.6373777e-02 3.7303663e-04 7.7156269e-04]]
Age : (25-32), conf = 0.900
time : 0.093
Gender : Male, conf = 0.996
Age Output : [[1.8286028e-04 9.7011747e-05 8.2962252e-03 3.5359371e-03 9.5739096e-01
  3.0187879e-02 8.9649031e-05 2.1950201e-04]]
Age : (25-32), conf = 0.957
time : 0.104
Gender : Male, conf = 0.996
Age Output : [[6.8402151e-03 1.6814823e-03 1.9629765e-02 4.1357856e-03 9.2720199e-01
  3.9427485e-02 3.7057669e-04 7.1270083e-04]]
Age : (25-32), conf = 0.927
time : 0.104
Gender : Male, conf = 0.996
Age Output : [[7.4442634e-03 2.1491712e-03 2.9166993e-02 6.7021446e-03 9.1113573e-01
  4.2421687e-02 2.7310450e-04 7.0693932e-04]]
Age : (25-32), conf = 0.911
time : 0.101
Gender : Male, conf = 0.998
Age Output : [[0.04484822 0.00807668 0.04221592 0.00698646 0.8007907  0.0934253
  0.00085875 0.00279791]]
Age : (25-32), conf = 0.801
time : 0.095
Gender : Male, conf = 0.993
Age Output : [[2.6540686e-03 8.1975787e-04 2.2334252e-02 5.1297043e-03 8.6966109e-01
  9.7433388e-02 5.3579971e-04 1.4318697e-03]]
Age : (25-32), conf = 0.870
time : 0.095
Gender : Male, conf = 0.993
Age Output : [[2.6540686e-03 8.1975787e-04 2.2334252e-02 5.1297043e-03 8.6966109e-01
  9.7433388e-02 5.3579971e-04 1.4318697e-03]]
Age : (25-32), conf = 0.870
time : 0.125
Gender : Male, conf = 0.975
Age Output : [[4.4056284e-03 1.2574637e-03 3.5953615e-02 7.0519843e-03 8.9626986e-01
  5.4230623e-02 2.5421119e-04 5.7662406e-04]]
Age : (25-32), conf = 0.896
time : 0.099
Gender : Male, conf = 0.975
Age Output : [[4.4056284e-03 1.2574637e-03 3.5953615e-02 7.0519843e-03 8.9626986e-01
  5.4230623e-02 2.5421119e-04 5.7662406e-04]]
Age : (25-32), conf = 0.896
time : 0.097
Gender : Male, conf = 0.994
Age Output : [[4.7966960e-04 3.7197882e-04 4.1027915e-02 7.6077981e-03 8.8774532e-01
  6.2355857e-02 1.1933676e-04 2.9213168e-04]]
Age : (25-32), conf = 0.888
time : 0.081
Gender : Male, conf = 0.994
Age Output : [[4.9084454e-04 4.0648488e-04 1.2621160e-01 2.0175131e-02 7.7631706e-01
  7.5842269e-02 1.4184788e-04 4.1468235e-04]]
Age : (25-32), conf = 0.776
time : 0.097
Gender : Male, conf = 0.997
Age Output : [[3.1450838e-02 9.0049291e-03 5.5035137e-02 2.4790600e-02 8.2827967e-01
  4.9944010e-02 3.3745897e-04 1.1573572e-03]]
Age : (25-32), conf = 0.828
time : 0.115
Gender : Male, conf = 0.998
Age Output : [[3.9602080e-04 3.5014204e-04 2.5774287e-02 7.0625925e-03 9.2936045e-01
  3.6272861e-02 1.5897381e-04 6.2457524e-04]]
Age : (25-32), conf = 0.929
time : 0.102
Gender : Male, conf = 0.997
Age Output : [[1.09406549e-03 1.63577637e-03 1.08808406e-01 2.15967782e-02
  7.86532164e-01 7.93352872e-02 2.98682309e-04 6.98828313e-04]]
Age : (25-32), conf = 0.787
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[1.6745476e-03 1.0068452e-03 9.8840125e-02 2.0616231e-02 7.8923905e-01
  8.8152364e-02 1.5249889e-04 3.1825172e-04]]
Age : (25-32), conf = 0.789
time : 0.087
Gender : Male, conf = 0.998
Age Output : [[3.8437336e-04 4.5268142e-04 3.8689833e-02 7.4808747e-03 9.3179071e-01
  2.0867519e-02 8.3834973e-05 2.5017423e-04]]
Age : (25-32), conf = 0.932
time : 0.082
Gender : Male, conf = 0.998
Age Output : [[3.8437336e-04 4.5268142e-04 3.8689833e-02 7.4808747e-03 9.3179071e-01
  2.0867519e-02 8.3834973e-05 2.5017423e-04]]
Age : (25-32), conf = 0.932
time : 0.088
Gender : Male, conf = 0.999
Age Output : [[3.9293040e-03 1.1830464e-03 2.9550564e-02 8.7374896e-03 8.5363430e-01
  1.0162889e-01 3.1902030e-04 1.0173947e-03]]
Age : (25-32), conf = 0.854
time : 0.084
Gender : Male, conf = 0.991
Age Output : [[6.5012440e-02 1.2185563e-02 1.2255702e-01 1.4707500e-02 7.0859563e-01
  7.4992359e-02 4.8966391e-04 1.4597949e-03]]
Age : (25-32), conf = 0.709
time : 0.081
Gender : Male, conf = 0.997
Age Output : [[1.2798123e-03 5.4944819e-04 3.0376980e-02 5.3432710e-03 9.1230214e-01
  4.9412314e-02 1.8844100e-04 5.4756942e-04]]
Age : (25-32), conf = 0.912
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[3.8967789e-03 2.4703296e-03 7.2170898e-02 1.5398820e-02 8.0059981e-01
  1.0412351e-01 3.1435542e-04 1.0255058e-03]]
Age : (25-32), conf = 0.801
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[7.6882582e-04 8.4846967e-04 3.6984541e-02 1.0020893e-02 9.1481060e-01
  3.6046743e-02 1.3618682e-04 3.8366558e-04]]
Age : (25-32), conf = 0.915
time : 0.092
Gender : Male, conf = 0.996
Age Output : [[7.6882582e-04 8.4846967e-04 3.6984541e-02 1.0020893e-02 9.1481060e-01
  3.6046743e-02 1.3618682e-04 3.8366558e-04]]
Age : (25-32), conf = 0.915
time : 0.115
Gender : Male, conf = 0.997
Age Output : [[5.6599180e-04 3.0322245e-04 8.2630599e-03 2.4711788e-03 9.7016698e-01
  1.7951641e-02 7.4055788e-05 2.0385248e-04]]
Age : (25-32), conf = 0.970
time : 0.097
Gender : Male, conf = 0.992
Age Output : [[7.6158606e-03 1.3198939e-03 2.0338750e-02 4.3964670e-03 8.8662213e-01
  7.6857708e-02 5.2171003e-04 2.3273274e-03]]
Age : (25-32), conf = 0.887
time : 0.093
Gender : Male, conf = 0.998
Age Output : [[1.1016259e-03 1.1097229e-03 7.5041614e-02 9.8699909e-03 8.7077445e-01
  4.1545685e-02 1.3965015e-04 4.1741718e-04]]
Age : (25-32), conf = 0.871
time : 0.084
Gender : Male, conf = 0.997
Age Output : [[3.0557967e-03 1.7313597e-03 2.4022434e-02 1.3034665e-02 9.1681302e-01
  4.0709406e-02 1.8333363e-04 4.5011021e-04]]
Age : (25-32), conf = 0.917
time : 0.118
Gender : Male, conf = 0.998
Age Output : [[2.4415343e-04 2.4286898e-04 2.3233108e-02 7.1386942e-03 9.1576153e-01
  5.2920129e-02 1.3747168e-04 3.2204442e-04]]
Age : (25-32), conf = 0.916
time : 0.114
Gender : Male, conf = 0.990
Age Output : [[2.2316050e-04 1.4145351e-04 2.1764342e-02 9.8745758e-03 9.2033535e-01
  4.7254231e-02 1.0542723e-04 3.0140451e-04]]
Age : (25-32), conf = 0.920
time : 0.122
Gender : Male, conf = 0.997
Age Output : [[8.7628380e-04 1.5430178e-03 1.7016885e-01 2.3027303e-02 7.3899269e-01
  6.5045550e-02 9.0772723e-05 2.5553844e-04]]
Age : (25-32), conf = 0.739
time : 0.131
Gender : Male, conf = 0.994
Age Output : [[1.0958785e-02 4.3658316e-03 4.1734967e-02 1.0521297e-02 8.7887686e-01
  5.2803390e-02 2.1310410e-04 5.2577292e-04]]
Age : (25-32), conf = 0.879
time : 0.121
Gender : Male, conf = 0.995
Age Output : [[9.1309502e-04 1.8843732e-04 1.5024251e-02 3.9138380e-03 8.5397190e-01
  1.2533833e-01 1.9335651e-04 4.5685127e-04]]
Age : (25-32), conf = 0.854
time : 0.121
Gender : Male, conf = 0.969
Age Output : [[4.0931785e-03 1.1666610e-03 4.9177904e-02 7.6454305e-03 8.7828809e-01
  5.8450535e-02 2.6536096e-04 9.1288314e-04]]
Age : (25-32), conf = 0.878
time : 0.121
Gender : Male, conf = 0.995
Age Output : [[5.8949675e-04 4.2316105e-04 2.0164698e-02 5.0529884e-03 9.1577083e-01
  5.7250794e-02 1.9239701e-04 5.5581395e-04]]
Age : (25-32), conf = 0.916
time : 0.116
Gender : Male, conf = 0.973
Age Output : [[2.09262152e-03 7.03837257e-04 1.46068055e-02 5.03940508e-03
  9.30369020e-01 4.61430289e-02 2.41857764e-04 8.03430565e-04]]
Age : (25-32), conf = 0.930
time : 0.122
Gender : Male, conf = 0.997
Age Output : [[7.40224030e-04 3.37077305e-04 1.53322695e-02 8.55323486e-03
  9.29034472e-01 4.56193797e-02 1.12156376e-04 2.71097262e-04]]
Age : (25-32), conf = 0.929
time : 0.116
Gender : Male, conf = 0.991
Age Output : [[1.5842270e-03 6.6510565e-04 2.4251333e-02 6.6558085e-03 9.1410875e-01
  5.2157786e-02 1.8335419e-04 3.9356417e-04]]
Age : (25-32), conf = 0.914
time : 0.116
Gender : Male, conf = 0.996
Age Output : [[3.7013557e-05 3.3282173e-05 6.9892122e-03 4.4582239e-03 9.3137926e-01
  5.6895074e-02 7.4745556e-05 1.3327452e-04]]
Age : (25-32), conf = 0.931
time : 0.107
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.983
Age Output : [[7.4076781e-04 2.0750859e-04 4.6489304e-03 2.8195991e-03 9.5071626e-01
  4.0216781e-02 1.7731458e-04 4.7281312e-04]]
Age : (25-32), conf = 0.951
time : 0.117
Gender : Male, conf = 0.974
Age Output : [[1.9293440e-04 8.7758424e-05 1.0808146e-02 3.8923067e-03 9.3968946e-01
  4.4980533e-02 1.1235717e-04 2.3642067e-04]]
Age : (25-32), conf = 0.940
time : 0.115
Gender : Male, conf = 0.976
Age Output : [[1.4416120e-04 1.5328548e-04 2.0528683e-02 4.0473868e-03 9.5637608e-01
  1.8466091e-02 9.5285002e-05 1.8896430e-04]]
Age : (25-32), conf = 0.956
time : 0.122
Gender : Male, conf = 0.973
Age Output : [[9.9739479e-04 2.1690076e-04 1.1836120e-02 3.0506151e-03 9.2466080e-01
  5.8692299e-02 1.7720593e-04 3.6863651e-04]]
Age : (25-32), conf = 0.925
time : 0.100
Gender : Male, conf = 0.991
Age Output : [[2.3552075e-03 8.8138116e-04 2.8141098e-02 6.3535622e-03 8.6611360e-01
  9.4984129e-02 3.1412879e-04 8.5701008e-04]]
Age : (25-32), conf = 0.866
time : 0.117
Gender : Male, conf = 0.976
Age Output : [[1.0632554e-02 3.4009251e-03 1.4014287e-02 1.5770223e-02 8.6680341e-01
  8.7808549e-02 4.8768826e-04 1.0822914e-03]]
Age : (25-32), conf = 0.867
time : 0.105
Gender : Male, conf = 0.996
Age Output : [[7.1830704e-04 5.4006669e-04 1.2388326e-02 1.3053615e-02 9.3504107e-01
  3.7820533e-02 1.4547202e-04 2.9256076e-04]]
Age : (25-32), conf = 0.935
time : 0.116
Gender : Male, conf = 0.985
Age Output : [[8.6476299e-04 2.6339409e-04 2.2821885e-02 5.7880976e-03 8.9222127e-01
  7.7557810e-02 1.5217396e-04 3.3059999e-04]]
Age : (25-32), conf = 0.892
time : 0.100
Gender : Male, conf = 0.998
Age Output : [[1.8839907e-03 1.5133903e-03 5.1507879e-02 2.4228543e-02 8.3248788e-01
  8.7448388e-02 2.9030460e-04 6.3973822e-04]]
Age : (25-32), conf = 0.832
time : 0.117
Gender : Male, conf = 0.986
Age Output : [[1.9891020e-04 1.3195095e-04 1.6101014e-02 6.9743930e-03 9.3345320e-01
  4.2956132e-02 5.9033053e-05 1.2530427e-04]]
Age : (25-32), conf = 0.933
time : 0.103
Gender : Male, conf = 0.990
Age Output : [[3.5611793e-04 2.3059460e-04 6.2387388e-02 1.1337525e-02 8.1581199e-01
  1.0932586e-01 1.5337653e-04 3.9716615e-04]]
Age : (25-32), conf = 0.816
time : 0.084
Gender : Male, conf = 0.990
Age Output : [[3.0842342e-04 1.7801575e-04 2.5739066e-02 7.7408231e-03 8.7596494e-01
  8.9602098e-02 1.2485783e-04 3.4180409e-04]]
Age : (25-32), conf = 0.876
time : 0.085
Gender : Male, conf = 0.991
Age Output : [[1.86250734e-04 2.48731929e-04 4.91268896e-02 1.21034775e-02
  8.71645391e-01 6.64229766e-02 8.31576690e-05 1.83079421e-04]]
Age : (25-32), conf = 0.872
time : 0.084
Gender : Male, conf = 0.991
Age Output : [[1.86250734e-04 2.48731929e-04 4.91268896e-02 1.21034775e-02
  8.71645391e-01 6.64229766e-02 8.31576690e-05 1.83079421e-04]]
Age : (25-32), conf = 0.872
time : 0.121
Gender : Male, conf = 0.993
Age Output : [[5.2349165e-04 7.1804516e-04 4.8074223e-02 7.2032185e-03 9.1566527e-01
  2.7411545e-02 1.1345852e-04 2.9079197e-04]]
Age : (25-32), conf = 0.916
time : 0.137
Gender : Male, conf = 0.985
Age Output : [[1.4824147e-04 1.8856431e-04 4.4798702e-02 1.0820835e-02 8.9383274e-01
  4.9880296e-02 6.7981186e-05 2.6256926e-04]]
Age : (25-32), conf = 0.894
time : 0.132
Gender : Male, conf = 0.972
Age Output : [[3.4583060e-04 3.9733324e-04 2.8868813e-02 5.5099991e-03 9.2318773e-01
  4.1415486e-02 8.2487844e-05 1.9223694e-04]]
Age : (25-32), conf = 0.923
time : 0.138
Gender : Male, conf = 0.993
Age Output : [[8.6197775e-04 3.8793767e-04 4.3483499e-02 6.6122464e-03 8.5246575e-01
  9.5790304e-02 1.3200099e-04 2.6635121e-04]]
Age : (25-32), conf = 0.852
time : 0.136
Gender : Male, conf = 0.994
Age Output : [[6.0017471e-04 6.5795647e-04 3.4103159e-02 9.5303329e-03 9.1318810e-01
  4.1590314e-02 9.3529117e-05 2.3641113e-04]]
Age : (25-32), conf = 0.913
time : 0.116
Gender : Male, conf = 0.993
Age Output : [[4.5834222e-05 1.5043891e-04 8.4065460e-02 9.8542543e-03 8.6953205e-01
  3.6192536e-02 4.1287349e-05 1.1820300e-04]]
Age : (25-32), conf = 0.870
time : 0.148
Gender : Male, conf = 0.993
Age Output : [[8.1187587e-05 9.2658840e-05 5.4629999e-03 1.4880531e-03 9.7631776e-01
  1.6390022e-02 4.2149331e-05 1.2511895e-04]]
Age : (25-32), conf = 0.976
time : 0.107
Gender : Male, conf = 0.991
Age Output : [[2.3604264e-04 2.6422870e-04 2.7285215e-02 6.1384439e-03 9.2033130e-01
  4.5383889e-02 8.6045518e-05 2.7483379e-04]]
Age : (25-32), conf = 0.920
time : 0.101
Gender : Male, conf = 0.989
Age Output : [[1.8645838e-02 6.7993500e-03 5.0795685e-02 1.4929197e-02 8.2378995e-01
  8.3640151e-02 3.7243206e-04 1.0274529e-03]]
Age : (25-32), conf = 0.824
time : 0.089
Gender : Male, conf = 0.994
Age Output : [[1.6810377e-03 6.9041061e-04 9.1103604e-03 3.9371415e-03 9.5675111e-01
  2.7043533e-02 2.0728449e-04 5.7930878e-04]]
Age : (25-32), conf = 0.957
time : 0.100
Gender : Male, conf = 0.991
Age Output : [[9.1714342e-04 4.1999176e-04 7.9587270e-03 3.2337510e-03 9.6371257e-01
  2.3292478e-02 1.3638615e-04 3.2885789e-04]]
Age : (25-32), conf = 0.964
time : 0.086
Gender : Male, conf = 0.997
Age Output : [[9.1637994e-05 1.2916904e-04 6.7476602e-03 4.9511245e-03 9.5712227e-01
  3.0671813e-02 1.1298539e-04 1.7338386e-04]]
Age : (25-32), conf = 0.957
time : 0.100
Gender : Male, conf = 0.994
Age Output : [[1.37791518e-04 1.20912635e-04 1.69195849e-02 7.81056052e-03
  8.60219002e-01 1.14361688e-01 1.01347054e-04 3.29172472e-04]]
Age : (25-32), conf = 0.860
time : 0.126
Gender : Male, conf = 0.998
Age Output : [[4.8016775e-03 2.0629296e-03 4.9084790e-02 8.2815466e-03 8.3408457e-01
  1.0045834e-01 3.4176494e-04 8.8443159e-04]]
Age : (25-32), conf = 0.834
time : 0.119
Gender : Male, conf = 0.992
Age Output : [[2.9913257e-04 2.2676842e-04 3.9055694e-02 1.2866016e-02 7.7722353e-01
  1.6962124e-01 1.7313719e-04 5.3449045e-04]]
Age : (25-32), conf = 0.777
time : 0.094
Gender : Male, conf = 0.991
Age Output : [[1.0908061e-03 7.0100796e-04 3.2298565e-02 3.6847936e-03 9.2509902e-01
  3.6567725e-02 1.5865329e-04 3.9931486e-04]]
Age : (25-32), conf = 0.925
time : 0.105
Gender : Male, conf = 0.998
Age Output : [[2.70294317e-04 1.18389304e-04 8.94797035e-03 3.30394064e-03
  8.85517120e-01 1.01488605e-01 1.12172158e-04 2.41441638e-04]]
Age : (25-32), conf = 0.886
time : 0.100
Gender : Male, conf = 0.997
Age Output : [[3.7447442e-04 3.9479873e-04 7.1807988e-02 9.6344939e-03 8.3488840e-01
  8.2358025e-02 1.2706475e-04 4.1473610e-04]]
Age : (25-32), conf = 0.835
time : 0.109
Gender : Male, conf = 0.992
Age Output : [[1.6103989e-04 7.1745808e-04 4.2365283e-01 3.0242329e-02 4.9649855e-01
  4.8526738e-02 5.3788110e-05 1.4726935e-04]]
Age : (25-32), conf = 0.496
time : 0.092
Gender : Male, conf = 0.997
Age Output : [[4.8065686e-04 1.0344338e-03 1.5180498e-01 1.5901806e-02 7.5071484e-01
  7.9535529e-02 1.4805398e-04 3.7972117e-04]]
Age : (25-32), conf = 0.751
time : 0.103
Gender : Male, conf = 0.999
Age Output : [[6.9247428e-05 3.1530555e-05 5.1222928e-03 4.8033530e-03 8.7778467e-01
  1.1171892e-01 1.4896231e-04 3.2101385e-04]]
Age : (25-32), conf = 0.878
time : 0.097
Gender : Male, conf = 0.991
Age Output : [[4.8719605e-05 5.9727190e-05 1.1660659e-02 4.9100397e-03 9.2898589e-01
  5.4083481e-02 7.2563911e-05 1.7897093e-04]]
Age : (25-32), conf = 0.929
time : 0.106
Gender : Male, conf = 0.990
Age Output : [[5.58205975e-05 5.57882959e-05 6.37013558e-03 4.18785494e-03
  9.63406980e-01 2.57578287e-02 5.90431519e-05 1.06524756e-04]]
Age : (25-32), conf = 0.963
time : 0.099
Gender : Male, conf = 0.994
Age Output : [[3.6046276e-05 2.6247242e-05 1.3088212e-02 5.1336172e-03 8.8228244e-01
  9.9148914e-02 9.1768132e-05 1.9263577e-04]]
Age : (25-32), conf = 0.882
time : 0.117
Gender : Male, conf = 0.984
Age Output : [[1.62717828e-04 9.68893582e-05 1.99315324e-02 5.25528193e-03
  8.25677872e-01 1.48436591e-01 1.09191504e-04 3.29905917e-04]]
Age : (25-32), conf = 0.826
time : 0.101
Gender : Male, conf = 0.988
Age Output : [[6.9080043e-04 2.4463027e-04 2.0475063e-02 4.1836207e-03 8.0085641e-01
  1.7256476e-01 2.2295772e-04 7.6179544e-04]]
Age : (25-32), conf = 0.801
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[7.6277985e-04 4.3636523e-04 5.6690309e-02 1.8203091e-02 7.9040569e-01
  1.3261652e-01 1.9070451e-04 6.9454807e-04]]
Age : (25-32), conf = 0.790
time : 0.221
Gender : Male, conf = 0.997
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[2.2587376e-03 7.8969693e-04 3.7263289e-02 1.8066330e-02 7.4133867e-01
  1.9890894e-01 2.5604718e-04 1.1183044e-03]]
Age : (25-32), conf = 0.741
time : 0.187
Gender : Male, conf = 0.982
Age Output : [[1.8653467e-04 1.5835177e-04 2.4201412e-02 2.9736083e-02 8.5974002e-01
  8.5324764e-02 1.3648185e-04 5.1629898e-04]]
Age : (25-32), conf = 0.860
time : 0.286
Gender : Male, conf = 0.997
Age Output : [[6.1549908e-05 4.6294714e-05 8.8951970e-03 2.3357969e-02 9.0943545e-01
  5.7703078e-02 8.5986270e-05 4.1451288e-04]]
Age : (25-32), conf = 0.909
time : 0.212
Gender : Male, conf = 0.999
Age Output : [[1.9424311e-04 1.3510411e-04 2.0330516e-03 4.9744784e-03 9.6622276e-01
  2.5691798e-02 1.2461173e-04 6.2377518e-04]]
Age : (25-32), conf = 0.966
time : 0.165
Gender : Male, conf = 0.999
Age Output : [[7.7589258e-04 3.1727558e-04 4.9542440e-03 5.9653306e-03 9.1725934e-01
  6.9171958e-02 3.0142191e-04 1.2545000e-03]]
Age : (25-32), conf = 0.917
time : 0.265
Gender : Male, conf = 0.998
Age Output : [[4.1536172e-03 2.2086184e-03 6.8632312e-02 2.7860560e-02 7.3111016e-01
  1.6210863e-01 3.2227754e-04 3.6038794e-03]]
Age : (25-32), conf = 0.731
time : 0.323
Gender : Male, conf = 0.998
Age Output : [[8.0496958e-03 2.7054984e-03 2.9093537e-02 2.9023979e-02 7.2926867e-01
  1.9363596e-01 4.2647755e-04 7.7961730e-03]]
Age : (25-32), conf = 0.729
time : 0.227
Gender : Male, conf = 0.994
Age Output : [[1.9168779e-02 5.6209443e-03 4.4659227e-02 2.2940680e-02 7.3537534e-01
  1.6642115e-01 5.3158205e-04 5.2823476e-03]]
Age : (25-32), conf = 0.735
time : 0.223
Gender : Male, conf = 0.997
Age Output : [[0.01050956 0.00132891 0.01002685 0.00957427 0.61499107 0.33077127
  0.00094444 0.02185364]]
Age : (25-32), conf = 0.615
time : 0.296
Gender : Male, conf = 0.993
Age Output : [[1.9270189e-03 5.4597663e-04 1.4494248e-02 1.5184059e-02 6.5577930e-01
  3.0481616e-01 4.6530526e-04 6.7879404e-03]]
Age : (25-32), conf = 0.656
time : 0.256
Gender : Male, conf = 0.987
Age Output : [[1.0827634e-04 3.4824800e-04 1.9617272e-03 1.3966714e-03 9.9323493e-01
  2.8817574e-03 1.2848700e-05 5.5367051e-05]]
Age : (25-32), conf = 0.993
time : 0.361
Gender : Male, conf = 0.974
Age Output : [[5.0151715e-04 2.5380286e-04 3.3975588e-03 2.5659697e-03 9.4989306e-01
  4.2686537e-02 4.9577615e-05 6.5205380e-04]]
Age : (25-32), conf = 0.950
time : 0.274
Gender : Male, conf = 0.996
Age Output : [[7.8389847e-01 2.2965211e-02 1.0662334e-02 1.7556313e-03 1.5828377e-01
  2.0009400e-02 3.5554130e-04 2.0696577e-03]]
Age : (0-2), conf = 0.784
time : 0.168
Gender : Male, conf = 0.996
Age Output : [[1.2023649e-01 8.8610547e-03 2.0042961e-02 2.5912893e-03 8.0068052e-01
  4.4639036e-02 4.1739945e-04 2.5313166e-03]]
Age : (25-32), conf = 0.801
time : 0.152
Gender : Male, conf = 0.995
Age Output : [[4.1668868e-01 1.0307104e-02 9.6630678e-03 1.9197831e-03 5.1470023e-01
  4.2907689e-02 4.7479392e-04 3.3386752e-03]]
Age : (25-32), conf = 0.515
time : 0.141
Gender : Male, conf = 0.994
Age Output : [[1.6274701e-01 8.0110673e-03 2.0719642e-02 3.6444895e-03 6.9134176e-01
  1.0988898e-01 5.4813590e-04 3.0988792e-03]]
Age : (25-32), conf = 0.691
time : 0.097
Gender : Male, conf = 0.993
Age Output : [[5.7754487e-01 1.2349149e-02 9.2872903e-03 1.2811419e-03 3.6734226e-01
  2.8961554e-02 4.6354570e-04 2.7701790e-03]]
Age : (0-2), conf = 0.578
time : 0.095
Gender : Male, conf = 0.999
Age Output : [[4.2765284e-01 3.0494263e-02 7.2669715e-02 3.2597871e-03 4.0865669e-01
  5.3497579e-02 2.7268942e-04 3.4964872e-03]]
Age : (0-2), conf = 0.428
time : 0.090
Gender : Male, conf = 0.999
Age Output : [[3.6280710e-02 5.8172387e-03 3.7492480e-02 4.7509540e-03 8.3132720e-01
  8.1056274e-02 2.5510986e-04 3.0200309e-03]]
Age : (25-32), conf = 0.831
time : 0.100
Gender : Male, conf = 0.994
Age Output : [[4.7538623e-02 2.9049753e-03 1.5769109e-02 4.9780686e-03 7.8307319e-01
  1.3696940e-01 7.6542684e-04 8.0011263e-03]]
Age : (25-32), conf = 0.783
time : 0.091
Gender : Male, conf = 0.997
Age Output : [[2.6622855e-03 6.2781799e-04 1.0791700e-02 3.1901614e-03 9.1735876e-01
  6.3819423e-02 1.3098515e-04 1.4189554e-03]]
Age : (25-32), conf = 0.917
time : 0.098
Gender : Male, conf = 0.997
Age Output : [[2.6622855e-03 6.2781799e-04 1.0791700e-02 3.1901614e-03 9.1735876e-01
  6.3819423e-02 1.3098515e-04 1.4189554e-03]]
Age : (25-32), conf = 0.917
time : 0.101
Gender : Male, conf = 0.998
Age Output : [[1.5913539e-02 2.6767345e-03 2.4191596e-02 4.9955207e-03 9.0995210e-01
  4.0579800e-02 1.9016044e-04 1.5006843e-03]]
Age : (25-32), conf = 0.910
time : 0.104
Gender : Male, conf = 0.992
Age Output : [[4.8507933e-02 8.9836968e-03 4.2559110e-02 4.0588798e-03 8.1195402e-01
  8.1852399e-02 2.9188950e-04 1.7921104e-03]]
Age : (25-32), conf = 0.812
time : 0.082
Gender : Male, conf = 0.992
Age Output : [[1.25406701e-02 1.35242345e-03 1.59526467e-02 2.35462142e-03
  8.60112727e-01 1.05662644e-01 2.20378497e-04 1.80400175e-03]]
Age : (25-32), conf = 0.860
time : 0.105
Gender : Male, conf = 0.997
Age Output : [[2.3342936e-01 8.5694855e-03 2.3801800e-02 3.0606028e-03 6.5281969e-01
  7.4471533e-02 4.1764902e-04 3.4298890e-03]]
Age : (25-32), conf = 0.653
time : 0.094
Gender : Male, conf = 0.999
Age Output : [[5.9100538e-02 1.3869027e-02 9.6321076e-02 6.2113688e-03 7.3661029e-01
  8.5139021e-02 2.4665744e-04 2.5020228e-03]]
Age : (25-32), conf = 0.737
time : 0.102
Gender : Male, conf = 0.998
Age Output : [[3.3441402e-02 3.8484177e-03 3.5589252e-02 3.9041059e-03 8.2892025e-01
  9.2573799e-02 2.5271368e-04 1.4700543e-03]]
Age : (25-32), conf = 0.829
time : 0.097
Gender : Male, conf = 0.994
Age Output : [[1.3439826e-03 1.3838399e-03 2.9392101e-02 4.5552752e-03 9.3792051e-01
  2.5041504e-02 6.0853214e-05 3.0205006e-04]]
Age : (25-32), conf = 0.938
time : 0.119
Gender : Male, conf = 0.994
Age Output : [[1.7105341e-02 3.4904066e-03 3.2788225e-02 3.2756452e-03 9.0732110e-01
  3.5214391e-02 1.5399116e-04 6.5085216e-04]]
Age : (25-32), conf = 0.907
time : 0.117
Gender : Male, conf = 0.995
Age Output : [[2.4343822e-03 2.5141935e-03 1.4553992e-01 8.6600892e-03 6.7750323e-01
  1.6229159e-01 1.6196228e-04 8.9464511e-04]]
Age : (25-32), conf = 0.678
time : 0.109
Gender : Male, conf = 0.989
Age Output : [[1.3206592e-03 2.8747876e-04 1.3015880e-02 2.8665075e-03 7.6482058e-01
  2.1675701e-01 1.6432740e-04 7.6759688e-04]]
Age : (25-32), conf = 0.765
time : 0.107
Gender : Male, conf = 0.995
Age Output : [[0.19949244 0.01468718 0.04148451 0.00810882 0.59460104 0.13508186
  0.00111272 0.00543144]]
Age : (25-32), conf = 0.595
time : 0.105
Gender : Male, conf = 0.986
Age Output : [[9.9796150e-03 1.3799586e-03 2.6380448e-02 5.3534955e-03 8.3974808e-01
  1.1511418e-01 2.2322084e-04 1.8209652e-03]]
Age : (25-32), conf = 0.840
time : 0.087
Gender : Male, conf = 0.986
Age Output : [[9.9796150e-03 1.3799586e-03 2.6380448e-02 5.3534955e-03 8.3974808e-01
  1.1511418e-01 2.2322084e-04 1.8209652e-03]]
Age : (25-32), conf = 0.840
time : 0.113
Gender : Male, conf = 0.994
Age Output : [[5.6272905e-02 4.6145017e-03 2.9209804e-02 5.8595142e-03 7.9448658e-01
  1.0593131e-01 3.6612307e-04 3.2591268e-03]]
Age : (25-32), conf = 0.794
time : 0.107
Gender : Male, conf = 0.993
Age Output : [[1.0142836e-02 9.4094116e-04 1.5946163e-02 3.4212812e-03 8.7311596e-01
  9.4799832e-02 2.2200697e-04 1.4111036e-03]]
Age : (25-32), conf = 0.873
time : 0.102
Gender : Male, conf = 0.994
Age Output : [[1.3564031e-02 4.6307328e-03 4.1986149e-02 3.7542568e-03 8.9428109e-01
  4.0823437e-02 1.3556388e-04 8.2476140e-04]]
Age : (25-32), conf = 0.894
time : 0.093
Gender : Male, conf = 0.984
Age Output : [[2.8819656e-03 1.9707379e-03 4.1515879e-02 3.0680469e-03 9.3388605e-01
  1.6362183e-02 5.9094345e-05 2.5609921e-04]]
Age : (25-32), conf = 0.934
time : 0.106
Gender : Male, conf = 0.991
Age Output : [[2.7991665e-04 2.6215910e-04 2.4812063e-02 2.9392648e-03 9.4880855e-01
  2.2675913e-02 3.2801949e-05 1.8937218e-04]]
Age : (25-32), conf = 0.949
time : 0.139
Gender : Male, conf = 0.981
Age Output : [[8.7931566e-04 5.2072096e-04 2.7631333e-02 2.2683872e-03 9.3115795e-01
  3.7165597e-02 7.9944213e-05 2.9678363e-04]]
Age : (25-32), conf = 0.931
time : 0.131
Gender : Male, conf = 0.989
Age Output : [[4.7232495e-03 5.7858019e-04 4.6683419e-03 1.1959500e-03 9.6697372e-01
  2.1273240e-02 1.0676863e-04 4.8017740e-04]]
Age : (25-32), conf = 0.967
time : 0.100
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.996
Age Output : [[2.7879432e-04 1.1847097e-04 1.2052543e-02 1.2201293e-03 9.4913727e-01
  3.6921546e-02 5.9241836e-05 2.1187172e-04]]
Age : (25-32), conf = 0.949
time : 0.085
Gender : Male, conf = 0.988
Age Output : [[3.3039856e-03 1.2479909e-03 1.6670102e-02 1.8456038e-03 9.4238383e-01
  3.3980928e-02 9.3195369e-05 4.7445920e-04]]
Age : (25-32), conf = 0.942
time : 0.085
Gender : Male, conf = 0.987
Age Output : [[6.2275387e-02 1.4636810e-02 5.6139268e-02 7.4266237e-03 8.2208806e-01
  3.5100259e-02 2.7320164e-04 2.0603491e-03]]
Age : (25-32), conf = 0.822
time : 0.100
Gender : Male, conf = 0.988
Age Output : [[1.8784229e-02 3.4528391e-03 2.8615460e-02 6.1592204e-03 8.4602273e-01
  9.4491832e-02 3.5797016e-04 2.1158527e-03]]
Age : (25-32), conf = 0.846
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[1.2634134e-01 1.6789256e-02 8.4598288e-02 1.0878272e-02 6.5412873e-01
  1.0254367e-01 6.2024896e-04 4.1002696e-03]]
Age : (25-32), conf = 0.654
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[0.12317088 0.01355497 0.12107555 0.01813294 0.53570205 0.1787316
  0.00083239 0.00879952]]
Age : (25-32), conf = 0.536
time : 0.099
Gender : Male, conf = 0.988
Age Output : [[0.02766791 0.0033169  0.02655618 0.00878513 0.5955982  0.33335358
  0.00067674 0.00404533]]
Age : (25-32), conf = 0.596
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[8.6614899e-03 9.6118689e-04 1.4096292e-02 3.3735109e-03 8.3468330e-01
  1.3570753e-01 3.8068157e-04 2.1360088e-03]]
Age : (25-32), conf = 0.835
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[8.6614899e-03 9.6118689e-04 1.4096292e-02 3.3735109e-03 8.3468330e-01
  1.3570753e-01 3.8068157e-04 2.1360088e-03]]
Age : (25-32), conf = 0.835
time : 0.106
Gender : Male, conf = 0.994
Age Output : [[2.19159275e-02 5.66399237e-03 6.99976385e-02 1.63636245e-02
  7.60589957e-01 1.20406836e-01 3.92363407e-04 4.66977200e-03]]
Age : (25-32), conf = 0.761
time : 0.113
Gender : Male, conf = 0.995
Age Output : [[8.2102651e-03 6.1547809e-04 8.3127357e-03 2.7148875e-03 8.3052152e-01
  1.4635704e-01 5.4088340e-04 2.7271837e-03]]
Age : (25-32), conf = 0.831
time : 0.126
Gender : Male, conf = 0.991
Age Output : [[1.0521128e-02 2.9719973e-03 2.0217387e-02 4.9168915e-03 9.2771268e-01
  3.2793704e-02 1.6757935e-04 6.9863367e-04]]
Age : (25-32), conf = 0.928
time : 0.116
Gender : Male, conf = 0.994
Age Output : [[2.3934238e-03 1.6992469e-03 5.7213806e-02 1.3446702e-02 8.8363212e-01
  4.1141298e-02 1.0208119e-04 3.7134663e-04]]
Age : (25-32), conf = 0.884
time : 0.100
Gender : Male, conf = 0.978
Age Output : [[9.6021598e-04 4.8746378e-04 8.0274783e-02 1.2152660e-02 7.9044485e-01
  1.1452986e-01 1.4033749e-04 1.0098087e-03]]
Age : (25-32), conf = 0.790
time : 0.107
Gender : Male, conf = 0.994
Age Output : [[1.9817011e-02 4.5292415e-03 2.4963405e-02 6.7398534e-03 9.0503567e-01
  3.8006801e-02 1.9327171e-04 7.1472093e-04]]
Age : (25-32), conf = 0.905
time : 0.100
Gender : Male, conf = 0.991
Age Output : [[3.6904395e-03 1.2829634e-03 2.2902250e-02 9.1667771e-03 9.3495280e-01
  2.7499326e-02 1.0355084e-04 4.0192358e-04]]
Age : (25-32), conf = 0.935
time : 0.085
Gender : Male, conf = 0.995
Age Output : [[1.3538221e-03 2.5002907e-03 1.3344100e-01 6.6250831e-02 7.5394934e-01
  4.1723948e-02 1.2093200e-04 6.5966492e-04]]
Age : (25-32), conf = 0.754
time : 0.106
Gender : Male, conf = 0.991
Age Output : [[1.7726442e-04 2.3772572e-04 4.3064974e-02 1.6723208e-02 9.2434341e-01
  1.5335390e-02 3.2778989e-05 8.5242420e-05]]
Age : (25-32), conf = 0.924
time : 0.094
Gender : Male, conf = 0.992
Age Output : [[4.6656604e-04 3.3967043e-04 3.7220888e-02 1.7201614e-02 9.1681242e-01
  2.7620170e-02 8.4262640e-05 2.5447269e-04]]
Age : (25-32), conf = 0.917
time : 0.100
Gender : Male, conf = 0.965
Age Output : [[2.6275990e-05 4.4160770e-05 4.5111306e-02 6.6848584e-03 8.9397222e-01
  5.4009192e-02 5.1935393e-05 1.0012977e-04]]
Age : (25-32), conf = 0.894
time : 0.122
Gender : Male, conf = 0.997
Age Output : [[2.4400123e-03 1.3083417e-03 4.5749541e-02 2.0375235e-02 8.9371544e-01
  3.5945926e-02 1.1891893e-04 3.4672380e-04]]
Age : (25-32), conf = 0.894
time : 0.131
Gender : Male, conf = 0.973
Age Output : [[2.91629058e-05 3.22152264e-05 3.48072164e-02 1.40015725e-02
  8.80439579e-01 7.04310685e-02 8.42740410e-05 1.74813977e-04]]
Age : (25-32), conf = 0.880
time : 0.138
Gender : Male, conf = 0.840
Age Output : [[1.8927005e-04 9.7790544e-05 3.0797746e-02 1.0010386e-02 8.8109547e-01
  7.7486336e-02 6.9958980e-05 2.5300312e-04]]
Age : (25-32), conf = 0.881
time : 0.131
Gender : Male, conf = 0.940
Age Output : [[2.64098606e-04 2.35521598e-04 1.11460775e-01 1.98171083e-02
  7.55186081e-01 1.12629510e-01 6.62306193e-05 3.40595667e-04]]
Age : (25-32), conf = 0.755
time : 0.116
Gender : Male, conf = 0.860
Age Output : [[1.1763100e-04 4.3717453e-05 1.7641172e-02 8.0428533e-03 8.8664013e-01
  8.7036461e-02 7.8742771e-05 3.9931596e-04]]
Age : (25-32), conf = 0.887
time : 0.131
Gender : Male, conf = 0.960
Age Output : [[4.3997687e-04 2.6543430e-04 6.9860797e-03 4.2096046e-03 9.7452468e-01
  1.3404794e-02 6.4689033e-05 1.0482027e-04]]
Age : (25-32), conf = 0.975
time : 0.170
Gender : Male, conf = 0.921
Age Output : [[1.7885865e-04 8.2651859e-05 1.6640285e-03 1.8506662e-03 9.7285044e-01
  2.3152489e-02 8.6820706e-05 1.3403253e-04]]
Age : (25-32), conf = 0.973
time : 0.163
Gender : Male, conf = 0.928
Age Output : [[1.66434387e-04 1.47961502e-04 1.25683565e-02 9.26550943e-03
  9.38493550e-01 3.90264317e-02 1.28067448e-04 2.03575328e-04]]
Age : (25-32), conf = 0.938
time : 0.222
Gender : Male, conf = 0.981
Age Output : [[2.0010993e-06 4.1067589e-05 1.6253231e-02 1.8824544e-02 9.6143466e-01
  3.4242515e-03 7.3855808e-06 1.2791710e-05]]
Age : (25-32), conf = 0.961
time : 0.241
Gender : Male, conf = 0.998
Age Output : [[3.9049378e-04 2.0209576e-03 1.8208699e-02 1.2771889e-02 9.6240920e-01
  4.1339053e-03 3.3913566e-05 3.0862375e-05]]
Age : (25-32), conf = 0.962
time : 0.164
Gender : Male, conf = 0.998
Age Output : [[4.5448338e-04 4.6525169e-03 4.1320182e-02 2.8822543e-02 9.2022717e-01
  4.4416981e-03 3.3873705e-05 4.7367332e-05]]
Age : (25-32), conf = 0.920
time : 0.172
Gender : Male, conf = 0.999
Age Output : [[2.16743117e-03 1.12311905e-02 4.33086939e-02 2.61146501e-02
  9.09737766e-01 7.31026521e-03 5.57041421e-05 7.42529664e-05]]
Age : (25-32), conf = 0.910
time : 0.222
Gender : Male, conf = 0.998
Age Output : [[5.3936301e-04 1.0438894e-02 3.9789304e-01 4.8903815e-02 5.3230029e-01
  9.7701950e-03 8.1501334e-05 7.2932984e-05]]
Age : (25-32), conf = 0.532
time : 0.315
Gender : Male, conf = 0.999
Age Output : [[2.9248063e-04 4.1147140e-03 2.9666856e-01 6.3771963e-02 6.2412184e-01
  1.0929667e-02 4.2161533e-05 5.8609796e-05]]
Age : (25-32), conf = 0.624
time : 0.162
Gender : Male, conf = 0.998
Age Output : [[6.7249354e-04 4.6657459e-03 1.4707184e-01 4.0039927e-02 7.9258043e-01
  1.4811828e-02 6.0639104e-05 9.7025390e-05]]
Age : (25-32), conf = 0.793
time : 0.126
Gender : Male, conf = 0.996
Age Output : [[3.0003392e-04 3.9548334e-03 3.6077788e-01 7.6156750e-02 5.4849285e-01
  1.0196035e-02 4.4519576e-05 7.7161858e-05]]
Age : (25-32), conf = 0.548
time : 0.139
Gender : Male, conf = 0.997
Age Output : [[3.0501673e-04 1.6285391e-03 5.7822216e-02 2.0567402e-02 9.1509378e-01
  4.5003872e-03 2.6572623e-05 5.5920846e-05]]
Age : (25-32), conf = 0.915
time : 0.111
Gender : Male, conf = 0.995
Age Output : [[1.9135606e-04 8.1060623e-04 7.2819166e-02 2.0733895e-02 8.9046240e-01
  1.4844301e-02 4.4436849e-05 9.3878960e-05]]
Age : (25-32), conf = 0.890
time : 0.147
Gender : Male, conf = 0.997
Age Output : [[3.1306606e-04 1.4210826e-03 8.3890207e-02 2.4863169e-02 8.7811393e-01
  1.1283245e-02 3.2962951e-05 8.2287661e-05]]
Age : (25-32), conf = 0.878
time : 0.123
Gender : Male, conf = 0.999
Age Output : [[7.2877410e-05 3.7809758e-04 7.0360973e-02 3.0282849e-02 8.8766056e-01
  1.1157816e-02 2.0686561e-05 6.6206390e-05]]
Age : (25-32), conf = 0.888
time : 0.108
Gender : Male, conf = 0.997
Age Output : [[8.5152639e-04 2.9292363e-03 1.6487361e-01 4.1620098e-02 7.7108377e-01
  1.8339569e-02 7.6906552e-05 2.2530511e-04]]
Age : (25-32), conf = 0.771
time : 0.092
Gender : Male, conf = 0.998
Age Output : [[9.1385999e-05 6.8711239e-04 5.3297341e-02 2.8988218e-02 9.0330815e-01
  1.3441805e-02 7.4037431e-05 1.1185950e-04]]
Age : (25-32), conf = 0.903
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[5.8050302e-04 1.5460314e-03 4.0556025e-02 2.0698965e-02 9.2530370e-01
  1.1162996e-02 3.9516981e-05 1.1233693e-04]]
Age : (25-32), conf = 0.925
time : 0.084
Gender : Male, conf = 0.998
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[4.2556432e-05 8.3605258e-04 1.4376122e-01 5.6305852e-02 7.8781474e-01
  1.1132510e-02 3.7263024e-05 6.9918497e-05]]
Age : (25-32), conf = 0.788
time : 0.105
Gender : Male, conf = 0.999
Age Output : [[1.4465667e-05 1.3461443e-04 4.6172153e-02 2.7373882e-02 9.1780347e-01
  8.4485756e-03 1.4306534e-05 3.8560731e-05]]
Age : (25-32), conf = 0.918
time : 0.111
Gender : Male, conf = 0.996
Age Output : [[2.05219767e-05 3.29749630e-04 7.76261464e-02 3.90233360e-02
  8.77194464e-01 5.76224690e-03 1.08950335e-05 3.26909503e-05]]
Age : (25-32), conf = 0.877
time : 0.116
Gender : Male, conf = 0.999
Age Output : [[2.4621448e-04 1.3406648e-03 1.1613846e-01 2.3299137e-02 8.4797096e-01
  1.0881876e-02 3.2861299e-05 8.9729765e-05]]
Age : (25-32), conf = 0.848
time : 0.131
Gender : Male, conf = 0.998
Age Output : [[1.5075922e-04 1.7835565e-03 4.6703720e-01 4.9921714e-02 4.7482988e-01
  6.2075183e-03 1.5023169e-05 5.4234304e-05]]
Age : (25-32), conf = 0.475
time : 0.116
Gender : Male, conf = 0.992
Age Output : [[1.9609383e-03 4.7075581e-03 2.7990979e-01 4.6550237e-02 6.4773053e-01
  1.8812485e-02 8.3477760e-05 2.4504054e-04]]
Age : (25-32), conf = 0.648
time : 0.149
Gender : Male, conf = 0.997
Age Output : [[7.2829821e-06 3.0453069e-04 3.1227648e-01 6.9579422e-02 6.1204559e-01
  5.7462812e-03 1.3438972e-05 2.6988457e-05]]
Age : (25-32), conf = 0.612
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[2.3059405e-05 7.4751704e-04 4.4407701e-01 3.8214214e-02 5.0857973e-01
  8.3221141e-03 1.1779220e-05 2.4618252e-05]]
Age : (25-32), conf = 0.509
time : 0.100
Gender : Male, conf = 0.998
Age Output : [[6.0016896e-06 1.4100139e-04 2.3649669e-01 3.5393726e-02 7.2232866e-01
  5.5914968e-03 1.3037779e-05 2.9348665e-05]]
Age : (25-32), conf = 0.722
time : 0.263
Gender : Male, conf = 0.994
Age Output : [[6.2456907e-05 4.2410544e-04 1.4946657e-01 5.6317698e-02 7.8589940e-01
  7.7518085e-03 1.6771519e-05 6.1156774e-05]]
Age : (25-32), conf = 0.786
time : 0.222
Gender : Male, conf = 0.999
Age Output : [[5.3405820e-05 3.9266309e-04 5.8890626e-02 2.4244867e-02 9.0950400e-01
  6.8587810e-03 1.7687553e-05 3.8070830e-05]]
Age : (25-32), conf = 0.910
time : 0.204
Gender : Male, conf = 0.998
Age Output : [[3.2906672e-05 4.9960590e-04 9.7651616e-02 3.2196607e-02 8.5792464e-01
  1.1606113e-02 4.1517909e-05 4.6985329e-05]]
Age : (25-32), conf = 0.858
time : 0.263
Gender : Male, conf = 0.990
Age Output : [[8.5161002e-05 1.5642832e-03 7.2501928e-01 5.9522945e-02 2.0245297e-01
  1.1282362e-02 2.2854898e-05 5.0220708e-05]]
Age : (8-12), conf = 0.725
time : 0.142
Gender : Male, conf = 0.983
Age Output : [[6.7008354e-05 6.8254786e-04 6.0086650e-01 1.0166898e-01 2.8315875e-01
  1.3484781e-02 1.7060109e-05 5.4382683e-05]]
Age : (8-12), conf = 0.601
time : 0.131
Gender : Male, conf = 0.995
Age Output : [[1.0324233e-04 8.7194104e-04 3.4630039e-01 5.2496977e-02 5.9145457e-01
  8.6825332e-03 1.5984257e-05 7.4338845e-05]]
Age : (25-32), conf = 0.591
time : 0.116
Gender : Male, conf = 0.998
Age Output : [[2.7040087e-04 1.5002979e-03 5.0102180e-01 5.6860812e-02 4.2510545e-01
  1.5134700e-02 2.8483046e-05 7.8027289e-05]]
Age : (8-12), conf = 0.501
time : 0.153
Gender : Male, conf = 0.998
Age Output : [[2.0011321e-05 3.4309889e-04 2.1660782e-01 6.3691162e-02 7.0231652e-01
  1.6912235e-02 4.1052106e-05 6.8110254e-05]]
Age : (25-32), conf = 0.702
time : 0.140
Gender : Male, conf = 0.997
Age Output : [[7.4507603e-05 7.7835546e-04 3.1634781e-01 4.5080822e-02 6.2268877e-01
  1.4911567e-02 4.1021238e-05 7.7043289e-05]]
Age : (25-32), conf = 0.623
time : 0.124
Gender : Male, conf = 0.990
Age Output : [[1.7932896e-04 2.7839164e-03 3.7111470e-01 1.3731523e-01 4.6176964e-01
  2.6687225e-02 5.0701634e-05 9.9196674e-05]]
Age : (25-32), conf = 0.462
time : 0.100
Gender : Male, conf = 0.998
Age Output : [[4.4728149e-05 7.4121641e-04 2.1785469e-01 4.7782585e-02 7.2611278e-01
  7.3986519e-03 2.3678287e-05 4.1634441e-05]]
Age : (25-32), conf = 0.726
time : 0.100
Gender : Male, conf = 0.997
Age Output : [[2.5220745e-05 6.4688252e-04 6.8671292e-01 5.7774004e-02 2.4519114e-01
  9.5826583e-03 2.1205837e-05 4.5976776e-05]]
Age : (8-12), conf = 0.687
time : 0.085
Gender : Male, conf = 0.996
Age Output : [[1.07231172e-04 9.32917348e-04 1.22342855e-01 5.12853004e-02
  8.11171472e-01 1.40150627e-02 2.96777107e-05 1.15414121e-04]]
Age : (25-32), conf = 0.811
time : 0.100
Gender : Male, conf = 0.993
Age Output : [[2.1086189e-05 5.6498731e-04 4.0552178e-01 8.6454384e-02 4.9757099e-01
  9.8192068e-03 1.6557511e-05 3.0959003e-05]]
Age : (25-32), conf = 0.498
time : 0.138
Gender : Male, conf = 0.995
Age Output : [[5.36631014e-05 1.09174161e-03 3.17729354e-01 8.94676149e-02
  5.77445984e-01 1.41189005e-02 2.79778633e-05 6.47805646e-05]]
Age : (25-32), conf = 0.577
time : 0.100
Gender : Male, conf = 0.997
Age Output : [[8.7586654e-05 1.2959099e-03 2.8143209e-01 6.3782163e-02 6.3387603e-01
  1.9419454e-02 2.9096364e-05 7.7691664e-05]]
Age : (25-32), conf = 0.634
time : 0.100
Gender : Male, conf = 0.983
Age Output : [[3.4375093e-04 2.8919359e-03 2.1513128e-01 3.4454361e-02 7.3427695e-01
  1.2775545e-02 3.4769633e-05 9.1387199e-05]]
Age : (25-32), conf = 0.734
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[9.2774724e-05 7.5759634e-04 2.5127205e-01 4.8658669e-02 6.8496650e-01
  1.4149081e-02 3.2331034e-05 7.1001567e-05]]
Age : (25-32), conf = 0.685
time : 0.084
Gender : Male, conf = 0.994
Age Output : [[6.2366460e-05 8.3979400e-04 4.2396575e-01 7.9268202e-02 4.8484462e-01
  1.0941094e-02 2.1045877e-05 5.7233898e-05]]
Age : (25-32), conf = 0.485
time : 0.216
Gender : Male, conf = 0.997
Age Output : [[1.1572592e-04 3.8080697e-04 1.5999429e-01 6.8283506e-02 7.2929114e-01
  4.1725773e-02 4.8704838e-05 1.6004799e-04]]
Age : (25-32), conf = 0.729
time : 0.147
Gender : Male, conf = 0.978
Age Output : [[8.2962782e-05 1.1076339e-04 4.4584580e-02 5.8183083e-03 9.1789055e-01
  3.1344332e-02 5.1745748e-05 1.1675695e-04]]
Age : (25-32), conf = 0.918
time : 0.116
Gender : Male, conf = 0.986
Age Output : [[3.2167644e-03 9.2011580e-04 2.9887389e-02 5.6042843e-03 9.2650729e-01
  3.3435877e-02 8.1325205e-05 3.4707878e-04]]
Age : (25-32), conf = 0.927
time : 0.116
Gender : Male, conf = 0.953
Age Output : [[1.2135045e-03 4.2029814e-04 1.3729054e-02 4.5040953e-03 9.4062328e-01
  3.9069403e-02 8.8475186e-05 3.5196642e-04]]
Age : (25-32), conf = 0.941
time : 0.100
Gender : Male, conf = 0.989
Age Output : [[1.5839299e-02 1.7332865e-03 8.6358478e-03 3.0671756e-03 9.3726236e-01
  3.2702900e-02 1.7516462e-04 5.8392162e-04]]
Age : (25-32), conf = 0.937
time : 0.122
Gender : Male, conf = 0.989
Age Output : [[1.4244963e-03 6.7256554e-04 2.0287363e-02 4.9615931e-03 9.4430012e-01
  2.7924521e-02 1.0168397e-04 3.2772406e-04]]
Age : (25-32), conf = 0.944
time : 0.100
Gender : Male, conf = 0.950
Age Output : [[3.4354374e-04 1.6305690e-04 1.0680265e-02 4.8182746e-03 9.4968700e-01
  3.3913027e-02 9.0845082e-05 3.0397347e-04]]
Age : (25-32), conf = 0.950
time : 0.100
Gender : Male, conf = 0.981
Age Output : [[3.0708218e-03 8.7762432e-04 1.4649458e-02 5.0546103e-03 9.4857949e-01
  2.7404217e-02 9.0037298e-05 2.7380130e-04]]
Age : (25-32), conf = 0.949
time : 0.100
Gender : Male, conf = 0.984
Age Output : [[1.7157837e-04 7.2242867e-05 7.8930631e-03 3.7983984e-03 9.5258433e-01
  3.5107289e-02 8.5632040e-05 2.8754608e-04]]
Age : (25-32), conf = 0.953
time : 0.100
Gender : Male, conf = 0.994
Age Output : [[5.0694733e-03 8.1101950e-04 1.8787501e-02 7.9158954e-03 9.1748142e-01
  4.8662145e-02 1.6026036e-04 1.1123649e-03]]
Age : (25-32), conf = 0.917
time : 0.085
Gender : Male, conf = 0.994
Age Output : [[5.6075398e-05 1.9663792e-05 5.6475182e-03 1.2839963e-03 9.5596206e-01
  3.6782470e-02 4.2303400e-05 2.0591100e-04]]
Age : (25-32), conf = 0.956
time : 0.085
Gender : Male, conf = 0.998
Age Output : [[4.4366915e-04 1.0835874e-04 8.1950603e-03 4.1149347e-03 9.0327728e-01
  8.2951672e-02 1.6300958e-04 7.4599049e-04]]
Age : (25-32), conf = 0.903
time : 0.085
Gender : Male, conf = 0.998
Age Output : [[4.4366915e-04 1.0835874e-04 8.1950603e-03 4.1149347e-03 9.0327728e-01
  8.2951672e-02 1.6300958e-04 7.4599049e-04]]
Age : (25-32), conf = 0.903
time : 0.100
Gender : Male, conf = 0.997
Age Output : [[1.98674345e-04 1.10180175e-04 1.55305257e-02 4.21541883e-03
  9.60083544e-01 1.95969138e-02 4.07353873e-05 2.23981406e-04]]
Age : (25-32), conf = 0.960
time : 0.084
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.993
Age Output : [[8.0117548e-04 1.9428354e-04 1.3862841e-02 5.1497621e-03 8.2207114e-01
  1.5697436e-01 1.7132255e-04 7.7514601e-04]]
Age : (25-32), conf = 0.822
time : 0.085
Gender : Male, conf = 0.995
Age Output : [[7.9483242e-04 9.3062918e-05 3.0060983e-03 1.4043434e-03 8.5791010e-01
  1.3591248e-01 1.8297453e-04 6.9619657e-04]]
Age : (25-32), conf = 0.858
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[8.5037091e-04 1.8151689e-04 6.2273410e-03 1.5037742e-03 9.2189062e-01
  6.8787262e-02 1.3269122e-04 4.2640977e-04]]
Age : (25-32), conf = 0.922
time : 0.116
Gender : Male, conf = 0.996
Age Output : [[1.0427443e-02 1.0924269e-03 5.1489687e-03 2.2029718e-03 9.0409321e-01
  7.5145029e-02 2.6353513e-04 1.6264359e-03]]
Age : (25-32), conf = 0.904
time : 0.100
Gender : Male, conf = 0.998
Age Output : [[1.8955033e-03 3.5097881e-04 3.2800916e-03 1.1378878e-03 9.5254105e-01
  4.0071346e-02 1.3997800e-04 5.8313383e-04]]
Age : (25-32), conf = 0.953
time : 0.116
Gender : Male, conf = 0.999
Age Output : [[1.0289872e-02 1.0356946e-03 2.0487909e-03 8.2739961e-04 9.6610260e-01
  1.8923761e-02 1.6911281e-04 6.0278201e-04]]
Age : (25-32), conf = 0.966
time : 0.122
Gender : Male, conf = 0.995
Age Output : [[9.6433144e-03 1.0835538e-03 2.2392878e-03 1.4417340e-03 9.5273036e-01
  3.1934761e-02 2.4356236e-04 6.8338017e-04]]
Age : (25-32), conf = 0.953
time : 0.084
Gender : Male, conf = 0.997
Age Output : [[8.5059023e-03 8.4233179e-04 2.9229203e-03 1.1823968e-03 9.5251518e-01
  3.2697245e-02 2.8497959e-04 1.0489998e-03]]
Age : (25-32), conf = 0.953
time : 0.100
Gender : Male, conf = 0.998
Age Output : [[0.3174429  0.01010772 0.01040724 0.00249821 0.5927309  0.06205123
  0.00073059 0.00403115]]
Age : (25-32), conf = 0.593
time : 0.100
Gender : Male, conf = 0.995
Age Output : [[5.3485405e-02 3.7898710e-03 6.5004556e-03 1.6306445e-03 9.0248346e-01
  2.9484132e-02 4.0338983e-04 2.2225918e-03]]
Age : (25-32), conf = 0.902
time : 0.085
Gender : Male, conf = 0.995
Age Output : [[5.3485405e-02 3.7898710e-03 6.5004556e-03 1.6306445e-03 9.0248346e-01
  2.9484132e-02 4.0338983e-04 2.2225918e-03]]
Age : (25-32), conf = 0.902
time : 0.085
Gender : Male, conf = 0.992
Age Output : [[4.1714716e-03 5.9178757e-04 3.3725824e-03 1.5532390e-03 9.4970840e-01
  3.9489314e-02 1.9423646e-04 9.1898412e-04]]
Age : (25-32), conf = 0.950
time : 0.085
Gender : Male, conf = 0.989
Age Output : [[1.3656175e-02 1.4625419e-03 3.6767686e-03 1.1863786e-03 9.5565188e-01
  2.3329856e-02 2.6448668e-04 7.7180902e-04]]
Age : (25-32), conf = 0.956
time : 0.085
Gender : Male, conf = 0.982
Age Output : [[1.0846827e-01 5.2227490e-03 7.8115854e-03 1.8224159e-03 8.1840599e-01
  5.4777384e-02 6.2466104e-04 2.8668947e-03]]
Age : (25-32), conf = 0.818
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[5.3244736e-02 4.9124840e-03 7.1073496e-03 2.1334097e-03 8.8667214e-01
  4.3461211e-02 4.7179125e-04 1.9968459e-03]]
Age : (25-32), conf = 0.887
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[0.47959512 0.01331498 0.01238703 0.00187874 0.4351029  0.05272117
  0.00064949 0.00435044]]
Age : (0-2), conf = 0.480
time : 0.100
Gender : Male, conf = 0.989
Age Output : [[1.6251612e-02 9.9026330e-04 4.4080615e-03 1.4070125e-03 9.0404779e-01
  6.9488294e-02 4.3539709e-04 2.9715819e-03]]
Age : (25-32), conf = 0.904
time : 0.100
Gender : Male, conf = 0.995
Age Output : [[1.1020718e-01 5.7367571e-03 6.4556804e-03 1.8094276e-03 8.1303364e-01
  5.8358710e-02 7.2575611e-04 3.6727937e-03]]
Age : (25-32), conf = 0.813
time : 0.084
Gender : Male, conf = 0.995
Age Output : [[1.1020718e-01 5.7367571e-03 6.4556804e-03 1.8094276e-03 8.1303364e-01
  5.8358710e-02 7.2575611e-04 3.6727937e-03]]
Age : (25-32), conf = 0.813
time : 0.116
Gender : Male, conf = 0.997
Age Output : [[0.23126578 0.00967185 0.0112145  0.00310198 0.66548383 0.07269323
  0.00083238 0.00573648]]
Age : (25-32), conf = 0.665
time : 0.084
Gender : Male, conf = 0.983
Age Output : [[8.5797206e-02 3.2756377e-03 3.6759470e-03 1.2231984e-03 8.6723202e-01
  3.6279403e-02 4.6506827e-04 2.0514778e-03]]
Age : (25-32), conf = 0.867
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[0.27528992 0.01228978 0.0145452  0.00269245 0.6160268  0.0737283
  0.00069232 0.00473515]]
Age : (25-32), conf = 0.616
time : 0.100
Gender : Male, conf = 0.997
Age Output : [[5.3998698e-03 7.9180172e-04 3.4364809e-03 1.7923234e-03 9.2947769e-01
  5.6953374e-02 3.5785636e-04 1.7904971e-03]]
Age : (25-32), conf = 0.929
time : 0.085
Gender : Male, conf = 0.996
Age Output : [[1.6327368e-02 1.1317094e-03 3.2260495e-03 1.2602543e-03 9.1042876e-01
  6.4679943e-02 3.4567350e-04 2.6001616e-03]]
Age : (25-32), conf = 0.910
time : 0.084
Gender : Male, conf = 0.997
Age Output : [[7.5182384e-03 8.9080608e-04 4.0207515e-03 2.6415912e-03 8.3095527e-01
  1.4975236e-01 3.4754878e-04 3.8733108e-03]]
Age : (25-32), conf = 0.831
time : 0.085
Gender : Male, conf = 0.994
Age Output : [[3.74568440e-02 2.88280682e-03 1.06833521e-02 2.29318836e-03
  8.36018741e-01 1.05705805e-01 4.35302267e-04 4.52396786e-03]]
Age : (25-32), conf = 0.836
time : 0.085
Gender : Male, conf = 0.994
Age Output : [[3.74568440e-02 2.88280682e-03 1.06833521e-02 2.29318836e-03
  8.36018741e-01 1.05705805e-01 4.35302267e-04 4.52396786e-03]]
Age : (25-32), conf = 0.836
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[9.8535633e-03 1.2146170e-03 2.7227597e-03 2.5712519e-03 9.3310297e-01
  4.8569240e-02 2.4397326e-04 1.7216987e-03]]
Age : (25-32), conf = 0.933
time : 0.106
Gender : Male, conf = 0.993
Age Output : [[1.5322337e-03 3.6679514e-04 3.0456807e-03 3.2652144e-03 9.6604753e-01
  2.4294833e-02 1.8391196e-04 1.2637711e-03]]
Age : (25-32), conf = 0.966
time : 0.085
Gender : Male, conf = 0.992
Age Output : [[7.1499473e-04 2.9078149e-04 9.1976020e-03 1.3127010e-02 8.3750683e-01
  1.3574097e-01 5.9222319e-04 2.8296572e-03]]
Age : (25-32), conf = 0.838
time : 0.084
Gender : Male, conf = 0.971
Age Output : [[0.00775805 0.00196914 0.06649742 0.02716209 0.61747926 0.2683303
  0.00100997 0.00979369]]
Age : (25-32), conf = 0.617
time : 0.085
Gender : Male, conf = 0.988
Age Output : [[1.1775626e-03 6.7978835e-04 4.0471960e-02 2.9187322e-02 7.9152381e-01
  1.3391513e-01 3.0877526e-04 2.7356572e-03]]
Age : (25-32), conf = 0.792
time : 0.085
Gender : Male, conf = 0.988
Age Output : [[1.1775626e-03 6.7978835e-04 4.0471960e-02 2.9187322e-02 7.9152381e-01
  1.3391513e-01 3.0877526e-04 2.7356572e-03]]
Age : (25-32), conf = 0.792
time : 0.100
Gender : Male, conf = 0.971
Age Output : [[4.3188343e-03 1.5028848e-03 4.5313410e-02 1.5612072e-02 7.8459185e-01
  1.4442271e-01 3.9010501e-04 3.8481760e-03]]
Age : (25-32), conf = 0.785
time : 0.100
Gender : Male, conf = 0.998
Age Output : [[0.05972507 0.01663803 0.22772326 0.04985842 0.3426597  0.29105338
  0.00074939 0.0115927 ]]
Age : (25-32), conf = 0.343
time : 0.085
Gender : Male, conf = 0.995
Age Output : [[5.8950181e-03 1.2679254e-03 1.8206857e-02 7.3467582e-03 7.0960528e-01
  2.5336248e-01 5.0688733e-04 3.8088353e-03]]
Age : (25-32), conf = 0.710
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[0.03908599 0.00590556 0.0525266  0.00573177 0.6364332  0.25102144
  0.0006454  0.00865006]]
Age : (25-32), conf = 0.636
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[0.20241524 0.01762724 0.04357954 0.00489167 0.54394335 0.17758562
  0.00084731 0.00910999]]
Age : (25-32), conf = 0.544
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[0.08877039 0.0046007  0.02994095 0.00504833 0.46597642 0.38510665
  0.00110834 0.0194483 ]]
Age : (25-32), conf = 0.466
time : 0.100
Gender : Male, conf = 0.997
Age Output : [[6.2923335e-02 6.2503293e-03 3.3838496e-02 4.1044513e-03 6.8838596e-01
  1.9760655e-01 6.6588778e-04 6.2250267e-03]]
Age : (25-32), conf = 0.688
time : 0.100
Gender : Male, conf = 0.995
Age Output : [[0.39264008 0.02934244 0.06632654 0.00341146 0.42115647 0.08026321
  0.00068044 0.0061794 ]]
Age : (25-32), conf = 0.421
time : 0.100
Gender : Male, conf = 0.992
Age Output : [[0.48485214 0.0258671  0.02348705 0.00230153 0.39170682 0.06520625
  0.00068116 0.00589808]]
Age : (0-2), conf = 0.485
time : 0.100
Gender : Male, conf = 0.992
Age Output : [[0.48485214 0.0258671  0.02348705 0.00230153 0.39170682 0.06520625
  0.00068116 0.00589808]]
Age : (0-2), conf = 0.485
time : 0.100
Gender : Male, conf = 0.998
Age Output : [[0.57405037 0.0220705  0.01201203 0.00192082 0.33849466 0.04541751
  0.00062086 0.00541324]]
Age : (0-2), conf = 0.574
time : 0.085
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.996
Age Output : [[0.28696713 0.01944075 0.03158288 0.00363086 0.53975695 0.11153685
  0.00082771 0.00625683]]
Age : (25-32), conf = 0.540
time : 0.100
Gender : Male, conf = 0.993
Age Output : [[6.2251365e-01 2.4154129e-02 1.5645189e-02 2.2017476e-03 2.8662497e-01
  4.3241553e-02 5.9561338e-04 5.0232024e-03]]
Age : (0-2), conf = 0.623
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[1.2519018e-01 1.5424350e-02 6.7365304e-02 4.0667374e-03 6.6033435e-01
  1.2242598e-01 6.2867068e-04 4.5644236e-03]]
Age : (25-32), conf = 0.660
time : 0.084
Gender : Male, conf = 0.997
Age Output : [[6.5174222e-02 8.3697913e-03 4.7814824e-02 4.3370193e-03 7.7692252e-01
  9.1769494e-02 6.2819815e-04 4.9838945e-03]]
Age : (25-32), conf = 0.777
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[0.20619515 0.01392671 0.02417848 0.00575203 0.61067253 0.13001128
  0.0013731  0.00789077]]
Age : (25-32), conf = 0.611
time : 0.092
Gender : Male, conf = 0.997
Age Output : [[0.20619515 0.01392671 0.02417848 0.00575203 0.61067253 0.13001128
  0.0013731  0.00789077]]
Age : (25-32), conf = 0.611
time : 0.109
Gender : Male, conf = 0.996
Age Output : [[0.3458643  0.02661597 0.07788828 0.00404747 0.43330398 0.10548473
  0.0006808  0.00611452]]
Age : (25-32), conf = 0.433
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[0.36307868 0.02529992 0.07877696 0.00382052 0.35502136 0.16560687
  0.00061375 0.00778187]]
Age : (0-2), conf = 0.363
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[0.11998658 0.00912381 0.02209722 0.00339597 0.7189028  0.11719842
  0.0007262  0.00856894]]
Age : (25-32), conf = 0.719
time : 0.085
Gender : Male, conf = 0.996
Age Output : [[6.5757573e-02 6.3440064e-03 1.9968299e-02 2.9983188e-03 7.7675080e-01
  1.2227254e-01 5.6554709e-04 5.3428486e-03]]
Age : (25-32), conf = 0.777
time : 0.085
Gender : Male, conf = 0.984
Age Output : [[0.15011074 0.00689976 0.02399363 0.00428419 0.62339294 0.17569688
  0.00108384 0.01453798]]
Age : (25-32), conf = 0.623
time : 0.100
Gender : Male, conf = 0.990
Age Output : [[5.6132935e-02 4.6817265e-03 3.5854854e-02 3.9460128e-03 7.5949979e-01
  1.2933615e-01 7.1816152e-04 9.8303808e-03]]
Age : (25-32), conf = 0.759
time : 0.132
Gender : Male, conf = 0.995
Age Output : [[0.3397547  0.01462536 0.03521447 0.00462366 0.38962275 0.20390065
  0.00104434 0.01121421]]
Age : (25-32), conf = 0.390
time : 0.122
Gender : Male, conf = 0.994
Age Output : [[0.18774945 0.02923351 0.22689061 0.00558002 0.35203668 0.17999038
  0.00077022 0.01774912]]
Age : (25-32), conf = 0.352
time : 0.147
Gender : Male, conf = 0.997
Age Output : [[0.04577333 0.00289341 0.01337929 0.00545758 0.58357    0.3349498
  0.00092354 0.01305308]]
Age : (25-32), conf = 0.584
time : 0.185
Gender : Male, conf = 0.997
Age Output : [[0.20085867 0.00647699 0.01600264 0.00348064 0.39500105 0.36345145
  0.00135469 0.01337384]]
Age : (25-32), conf = 0.395
time : 0.176
Gender : Male, conf = 0.993
Age Output : [[0.04682493 0.00306445 0.01247455 0.00686895 0.6532822  0.2555451
  0.00140521 0.02053464]]
Age : (25-32), conf = 0.653
time : 0.444
Gender : Male, conf = 0.981
Age Output : [[8.5930683e-02 3.8030336e-03 1.5075355e-02 3.4933304e-03 7.6516324e-01
  1.1810687e-01 6.0773740e-04 7.8196516e-03]]
Age : (25-32), conf = 0.765
time : 0.230
Gender : Male, conf = 0.993
Age Output : [[0.04177658 0.00324824 0.01100396 0.00470302 0.7587535  0.17169301
  0.0010406  0.00778107]]
Age : (25-32), conf = 0.759
time : 0.143
Gender : Male, conf = 0.992
Age Output : [[4.8611362e-02 3.0948466e-03 8.8125663e-03 4.6296562e-03 8.4619546e-01
  8.1512451e-02 5.9372821e-04 6.5499758e-03]]
Age : (25-32), conf = 0.846
time : 0.154
Gender : Male, conf = 0.993
Age Output : [[0.09243302 0.00588057 0.01807634 0.00509919 0.65854543 0.20115304
  0.00133472 0.01747769]]
Age : (25-32), conf = 0.659
time : 0.133
Gender : Male, conf = 0.995
Age Output : [[0.54338056 0.0145131  0.0165977  0.00419476 0.27513075 0.1275761
  0.00105044 0.01755665]]
Age : (0-2), conf = 0.543
time : 0.121
Gender : Male, conf = 0.998
Age Output : [[2.3425203e-02 1.8395409e-03 7.1590575e-03 3.1062285e-03 8.7309349e-01
  8.6975805e-02 5.1131379e-04 3.8892713e-03]]
Age : (25-32), conf = 0.873
time : 0.133
Gender : Male, conf = 0.989
Age Output : [[0.18816517 0.00743692 0.01703868 0.00439356 0.638109   0.13242117
  0.00122227 0.01121324]]
Age : (25-32), conf = 0.638
time : 0.123
Gender : Male, conf = 0.998
Age Output : [[1.8638866e-02 2.6026990e-03 2.7178798e-02 5.6615067e-03 7.4799454e-01
  1.9290563e-01 4.8627815e-04 4.5316191e-03]]
Age : (25-32), conf = 0.748
time : 0.113
Gender : Male, conf = 0.988
Age Output : [[0.03027828 0.00207735 0.008332   0.00398161 0.72837806 0.21729285
  0.00079478 0.00886508]]
Age : (25-32), conf = 0.728
time : 0.131
Gender : Male, conf = 0.996
Age Output : [[0.34320527 0.01151607 0.04536392 0.00664801 0.29119557 0.28334782
  0.0011714  0.01755192]]
Age : (0-2), conf = 0.343
time : 0.116
Gender : Male, conf = 0.996
Age Output : [[0.47313288 0.01989217 0.03272125 0.00242705 0.38292125 0.08034828
  0.00061853 0.00793865]]
Age : (0-2), conf = 0.473
time : 0.122
Gender : Male, conf = 0.998
Age Output : [[7.4347341e-01 1.8139094e-02 9.6894167e-03 1.7699226e-03 1.9446380e-01
  2.8513053e-02 3.5896589e-04 3.5923184e-03]]
Age : (0-2), conf = 0.743
time : 0.104
Gender : Male, conf = 0.996
Age Output : [[0.38007236 0.00849108 0.01344602 0.0040071  0.32010818 0.23957391
  0.00139543 0.03290597]]
Age : (0-2), conf = 0.380
time : 0.111
Gender : Male, conf = 0.975
Age Output : [[0.10186553 0.00401839 0.01118033 0.00356786 0.77240455 0.09379937
  0.00088946 0.01227444]]
Age : (25-32), conf = 0.772
time : 0.159
Gender : Male, conf = 0.992
Age Output : [[1.2794242e-02 2.2245087e-03 8.9495955e-03 4.8904824e-03 8.8960749e-01
  7.8818969e-02 2.2125809e-04 2.4935112e-03]]
Age : (25-32), conf = 0.890
time : 0.127
Gender : Male, conf = 0.977
Age Output : [[2.8648700e-03 6.5228128e-04 5.4465607e-03 2.4665631e-03 9.4792914e-01
  3.8941275e-02 1.0442704e-04 1.5948602e-03]]
Age : (25-32), conf = 0.948
time : 0.112
Gender : Male, conf = 0.916
Age Output : [[2.40783393e-02 3.00746388e-03 7.24524772e-03 5.57236327e-03
  8.53999376e-01 1.00479975e-01 3.96099756e-04 5.22109540e-03]]
Age : (25-32), conf = 0.854
time : 0.094
Gender : Male, conf = 0.897
Age Output : [[2.4439650e-02 5.4808287e-03 1.8465534e-02 9.3952995e-03 8.4573638e-01
  9.0768859e-02 2.7597370e-04 5.4375073e-03]]
Age : (25-32), conf = 0.846
time : 0.094
Gender : Male, conf = 0.997
Age Output : [[1.7281234e-02 2.2542353e-03 1.1174045e-02 7.3427600e-03 6.1040199e-01
  3.4658480e-01 2.8694927e-04 4.6741148e-03]]
Age : (25-32), conf = 0.610
time : 0.095
Gender : Male, conf = 0.996
Age Output : [[0.36927006 0.01110498 0.01290122 0.00868079 0.24422997 0.3382836
  0.00145092 0.01407856]]
Age : (0-2), conf = 0.369
time : 0.104
Gender : Male, conf = 0.998
Age Output : [[3.9318223e-03 9.5989159e-04 7.2522783e-03 5.4300465e-03 8.9562279e-01
  8.5180193e-02 2.6143805e-04 1.3615926e-03]]
Age : (25-32), conf = 0.896
time : 0.125
Gender : Male, conf = 0.999
Age Output : [[1.1820981e-03 5.0288363e-04 5.0558839e-03 5.7126400e-03 9.4589221e-01
  4.0873028e-02 1.5873740e-04 6.2253088e-04]]
Age : (25-32), conf = 0.946
time : 0.135
Gender : Male, conf = 0.998
Age Output : [[3.1111587e-02 6.5403599e-03 1.7609389e-02 9.5638372e-03 7.2739178e-01
  2.0508972e-01 7.2017824e-04 1.9730956e-03]]
Age : (25-32), conf = 0.727
time : 0.130
Gender : Male, conf = 0.997
Age Output : [[2.6964968e-01 5.3151108e-02 1.6269654e-01 1.7680416e-02 3.8200095e-01
  1.1196664e-01 3.8026911e-04 2.4744265e-03]]
Age : (25-32), conf = 0.382
time : 0.130
Gender : Male, conf = 0.994
Age Output : [[1.2457225e-03 1.1064099e-03 2.2522545e-01 2.3492878e-02 6.2618947e-01
  1.2223399e-01 6.0384638e-05 4.4573806e-04]]
Age : (25-32), conf = 0.626
time : 0.109
Gender : Male, conf = 0.994
Age Output : [[1.2457225e-03 1.1064099e-03 2.2522545e-01 2.3492878e-02 6.2618947e-01
  1.2223399e-01 6.0384638e-05 4.4573806e-04]]
Age : (25-32), conf = 0.626
time : 0.095
Gender : Male, conf = 0.997
Age Output : [[3.63433873e-03 1.46015594e-03 1.20600022e-01 2.51955893e-02
  6.92484915e-01 1.55591786e-01 1.13555434e-04 9.19585465e-04]]
Age : (25-32), conf = 0.692
time : 0.095
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.995
Age Output : [[4.10116836e-02 1.13757979e-02 1.04693234e-01 1.42579935e-02
  7.60674775e-01 6.68110996e-02 2.11991835e-04 9.63354541e-04]]
Age : (25-32), conf = 0.761
time : 0.100
Gender : Male, conf = 0.990
Age Output : [[6.02134131e-02 1.18583096e-02 1.22943364e-01 1.30726229e-02
  6.25772238e-01 1.63918242e-01 3.08919698e-04 1.91290886e-03]]
Age : (25-32), conf = 0.626
time : 0.095
Gender : Male, conf = 0.986
Age Output : [[8.3424849e-03 1.5867946e-03 2.1681186e-02 5.3364150e-03 8.2183492e-01
  1.3970295e-01 2.0813441e-04 1.3070902e-03]]
Age : (25-32), conf = 0.822
time : 0.090
Gender : Male, conf = 0.994
Age Output : [[0.14292827 0.01859289 0.0749185  0.03480431 0.47925866 0.24515498
  0.00048411 0.00385825]]
Age : (25-32), conf = 0.479
time : 0.115
Gender : Male, conf = 0.996
Age Output : [[9.9191554e-02 1.0503903e-02 4.6937477e-02 3.2011047e-02 6.5914732e-01
  1.4586145e-01 4.5956115e-04 5.8876835e-03]]
Age : (25-32), conf = 0.659
time : 0.121
Gender : Male, conf = 0.979
Age Output : [[0.5003476  0.01743913 0.03754628 0.00778926 0.24355972 0.18464357
  0.00065744 0.00801708]]
Age : (0-2), conf = 0.500
time : 0.110
Gender : Male, conf = 0.956
Age Output : [[0.12014691 0.0044338  0.02986271 0.01156193 0.38782388 0.43731105
  0.00071327 0.00814652]]
Age : (38-43), conf = 0.437
time : 0.099
Gender : Male, conf = 0.994
Age Output : [[5.7612681e-01 2.9243298e-02 2.9966488e-02 1.1566415e-02 2.5692177e-01
  9.0569690e-02 4.2884989e-04 5.1766797e-03]]
Age : (0-2), conf = 0.576
time : 0.095
Gender : Male, conf = 0.975
Age Output : [[0.40984806 0.03223979 0.07301085 0.0123785  0.3222676  0.14377621
  0.00058769 0.00589139]]
Age : (0-2), conf = 0.410
time : 0.098
Gender : Male, conf = 0.990
Age Output : [[9.8016197e-03 2.9083465e-03 5.3374890e-02 3.0968936e-02 7.9057133e-01
  1.1031130e-01 1.6529109e-04 1.8982047e-03]]
Age : (25-32), conf = 0.791
time : 0.085
Gender : Male, conf = 0.990
Age Output : [[9.8016197e-03 2.9083465e-03 5.3374890e-02 3.0968936e-02 7.9057133e-01
  1.1031130e-01 1.6529109e-04 1.8982047e-03]]
Age : (25-32), conf = 0.791
time : 0.085
Gender : Male, conf = 0.994
Age Output : [[8.0663526e-01 6.1754394e-02 4.6036799e-02 3.8384034e-03 5.7928961e-02
  2.1298744e-02 2.2678739e-04 2.2808001e-03]]
Age : (0-2), conf = 0.807
time : 0.085
Gender : Male, conf = 0.984
Age Output : [[6.4950776e-01 2.2785068e-02 1.8625220e-02 2.6703272e-03 2.6479369e-01
  3.5678528e-02 5.4275978e-04 5.3966222e-03]]
Age : (0-2), conf = 0.650
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[0.5190283  0.03517299 0.03028701 0.00876721 0.30387554 0.09414437
  0.00072319 0.00800132]]
Age : (0-2), conf = 0.519
time : 0.084
Gender : Male, conf = 0.997
Age Output : [[3.0755186e-03 4.5284932e-04 8.7127592e-03 5.4995012e-03 6.2152255e-01
  3.4513092e-01 3.7696149e-04 1.5228911e-02]]
Age : (25-32), conf = 0.622
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[1.04783624e-02 6.96499413e-03 1.47166485e-02 2.97135510e-03
  9.41841662e-01 2.07333621e-02 2.93431629e-04 2.00024154e-03]]
Age : (25-32), conf = 0.942
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[3.5414884e-03 2.1794902e-03 7.3766517e-03 2.5960850e-03 9.6532458e-01
  1.8201483e-02 9.7303287e-05 6.8287487e-04]]
Age : (25-32), conf = 0.965
time : 0.084
Gender : Male, conf = 0.997
Age Output : [[3.5414884e-03 2.1794902e-03 7.3766517e-03 2.5960850e-03 9.6532458e-01
  1.8201483e-02 9.7303287e-05 6.8287487e-04]]
Age : (25-32), conf = 0.965
time : 0.085
Gender : Male, conf = 0.993
Age Output : [[7.1254587e-03 1.4656153e-02 1.1463691e-01 1.5434242e-02 8.2966119e-01
  1.8038968e-02 5.2508127e-05 3.9450638e-04]]
Age : (25-32), conf = 0.830
time : 0.084
Gender : Male, conf = 0.992
Age Output : [[9.40784886e-02 6.82449117e-02 1.33831859e-01 1.37023665e-02
  6.48395479e-01 3.77715304e-02 2.89139076e-04 3.68615799e-03]]
Age : (25-32), conf = 0.648
time : 0.085
Gender : Male, conf = 0.992
Age Output : [[3.8727745e-01 9.1395430e-02 1.1172040e-01 1.2277716e-02 3.6696270e-01
  2.2374000e-02 3.6644546e-04 7.6257717e-03]]
Age : (0-2), conf = 0.387
time : 0.100
Gender : Male, conf = 0.822
Age Output : [[5.0733566e-01 1.5989093e-01 1.0985755e-01 6.4192554e-03 1.9861653e-01
  1.2180272e-02 2.5181510e-04 5.4479907e-03]]
Age : (0-2), conf = 0.507
time : 0.085
Gender : Male, conf = 0.963
Age Output : [[7.6417136e-01 1.2187173e-01 3.6834352e-02 4.0527708e-03 6.3409358e-02
  6.7059272e-03 1.7575595e-04 2.7787026e-03]]
Age : (0-2), conf = 0.764
time : 0.084
Gender : Male, conf = 0.963
Age Output : [[7.6417136e-01 1.2187173e-01 3.6834352e-02 4.0527708e-03 6.3409358e-02
  6.7059272e-03 1.7575595e-04 2.7787026e-03]]
Age : (0-2), conf = 0.764
time : 0.084
Gender : Male, conf = 0.702
Age Output : [[0.2799795  0.04080184 0.04148281 0.00968882 0.5835374  0.03474662
  0.00064448 0.00911851]]
Age : (25-32), conf = 0.584
time : 0.100
Gender : Male, conf = 0.984
Age Output : [[3.6034113e-01 1.0211725e-01 8.1284061e-02 1.0753516e-02 4.1438243e-01
  2.5902947e-02 3.0839472e-04 4.9101808e-03]]
Age : (25-32), conf = 0.414
time : 0.100
Gender : Male, conf = 0.908
Age Output : [[4.5406776e-03 3.7930009e-03 1.2230017e-02 3.3124215e-03 9.6110666e-01
  1.3952187e-02 1.1155476e-04 9.5342664e-04]]
Age : (25-32), conf = 0.961
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[1.4312214e-01 7.3817261e-02 1.6510336e-01 1.7712822e-02 5.7323635e-01
  2.3256648e-02 2.5333502e-04 3.4981233e-03]]
Age : (25-32), conf = 0.573
time : 0.100
Gender : Male, conf = 0.983
Age Output : [[1.29645625e-02 4.75746840e-02 1.26269460e-01 9.53766517e-03
  7.89235651e-01 1.22371474e-02 1.64857498e-04 2.01605377e-03]]
Age : (25-32), conf = 0.789
time : 0.106
Gender : Male, conf = 0.980
Age Output : [[2.1400292e-01 1.5135616e-01 2.7787182e-01 5.1491293e-03 3.2652542e-01
  2.2286607e-02 2.5955206e-04 2.5483817e-03]]
Age : (25-32), conf = 0.327
time : 0.100
Gender : Male, conf = 0.971
Age Output : [[4.0439904e-02 2.3353625e-02 1.1832981e-01 4.4302838e-03 7.7412438e-01
  3.1290539e-02 3.3133745e-04 7.7002062e-03]]
Age : (25-32), conf = 0.774
time : 0.084
Gender : Male, conf = 0.953
Age Output : [[1.1036401e-02 2.5783973e-02 8.2928553e-02 6.6667916e-03 8.5732508e-01
  1.4834623e-02 1.2463279e-04 1.3000401e-03]]
Age : (25-32), conf = 0.857
time : 0.085
Gender : Male, conf = 0.958
Age Output : [[6.9678456e-02 1.0617359e-01 1.3555279e-01 8.1211114e-03 6.6342843e-01
  1.5303522e-02 1.9884743e-04 1.5431844e-03]]
Age : (25-32), conf = 0.663
time : 0.084
Gender : Male, conf = 0.958
Age Output : [[6.9678456e-02 1.0617359e-01 1.3555279e-01 8.1211114e-03 6.6342843e-01
  1.5303522e-02 1.9884743e-04 1.5431844e-03]]
Age : (25-32), conf = 0.663
time : 0.085
Gender : Male, conf = 0.990
Age Output : [[3.1129872e-02 2.3407524e-02 2.4335023e-02 4.2545870e-03 9.0452456e-01
  1.1240561e-02 2.1946924e-04 8.8839966e-04]]
Age : (25-32), conf = 0.905
time : 0.085
Gender : Male, conf = 0.993
Age Output : [[4.8168960e-01 1.3481133e-01 9.5952891e-02 8.6416723e-03 2.2658479e-01
  4.7370527e-02 4.0291462e-04 4.5463541e-03]]
Age : (0-2), conf = 0.482
time : 0.100
Gender : Male, conf = 0.986
Age Output : [[0.58004683 0.06718832 0.02727304 0.00453663 0.2710999  0.04341678
  0.0006269  0.00581161]]
Age : (0-2), conf = 0.580
time : 0.084
Gender : Male, conf = 0.992
Age Output : [[6.3940197e-02 5.6083985e-02 4.2722911e-02 6.6816080e-03 8.1096971e-01
  1.7550252e-02 2.8358118e-04 1.7678128e-03]]
Age : (25-32), conf = 0.811
time : 0.084
Gender : Male, conf = 0.915
Age Output : [[7.9112083e-02 2.2274179e-02 1.6860789e-02 4.6772826e-03 8.3537430e-01
  3.7509728e-02 4.1047839e-04 3.7810733e-03]]
Age : (25-32), conf = 0.835
time : 0.084
Gender : Male, conf = 0.915
Age Output : [[7.9112083e-02 2.2274179e-02 1.6860789e-02 4.6772826e-03 8.3537430e-01
  3.7509728e-02 4.1047839e-04 3.7810733e-03]]
Age : (25-32), conf = 0.835
time : 0.085
Gender : Male, conf = 0.995
Age Output : [[9.3098702e-03 9.6057095e-03 2.1341847e-02 3.9609829e-03 9.2891079e-01
  2.5352484e-02 1.2068598e-04 1.3975909e-03]]
Age : (25-32), conf = 0.929
time : 0.100
Gender : Male, conf = 0.966
Age Output : [[8.9001535e-03 3.0822910e-03 6.3117668e-03 2.4089580e-03 9.3925136e-01
  3.8158745e-02 1.3342744e-04 1.7532720e-03]]
Age : (25-32), conf = 0.939
time : 0.100
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.998
Age Output : [[9.4239740e-04 2.2616687e-03 1.6546911e-02 1.2956890e-02 9.3026066e-01
  3.6383424e-02 1.1668927e-04 5.3126033e-04]]
Age : (25-32), conf = 0.930
time : 0.107
Gender : Male, conf = 0.998
Age Output : [[3.6200607e-04 5.3845363e-04 9.6859615e-03 8.1462944e-03 9.3003142e-01
  5.0581459e-02 1.0781732e-04 5.4653309e-04]]
Age : (25-32), conf = 0.930
time : 0.100
Gender : Male, conf = 0.987
Age Output : [[5.0895347e-04 3.2141033e-04 5.7718847e-03 2.7069880e-03 9.4734442e-01
  4.2634811e-02 7.1938382e-05 6.3952641e-04]]
Age : (25-32), conf = 0.947
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[1.7527601e-04 1.6084338e-04 3.1027005e-03 1.9807983e-03 9.6543270e-01
  2.8572822e-02 1.0492171e-04 4.6995259e-04]]
Age : (25-32), conf = 0.965
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[2.2442185e-04 1.7970556e-04 2.3253076e-03 1.7666925e-03 9.7481400e-01
  2.0191861e-02 8.5433785e-05 4.1248574e-04]]
Age : (25-32), conf = 0.975
time : 0.084
Gender : Male, conf = 0.984
Age Output : [[4.8109414e-05 1.1073827e-04 7.8028068e-03 6.5779667e-03 9.5968527e-01
  2.5461474e-02 2.7490143e-05 2.8617264e-04]]
Age : (25-32), conf = 0.960
time : 0.085
Gender : Male, conf = 0.984
Age Output : [[4.8109414e-05 1.1073827e-04 7.8028068e-03 6.5779667e-03 9.5968527e-01
  2.5461474e-02 2.7490143e-05 2.8617264e-04]]
Age : (25-32), conf = 0.960
time : 0.084
Gender : Male, conf = 0.980
Age Output : [[1.84935023e-04 1.80696501e-04 2.30943691e-03 1.41953654e-03
  9.84258533e-01 1.12106735e-02 3.74918673e-05 3.98743839e-04]]
Age : (25-32), conf = 0.984
time : 0.084
Gender : Male, conf = 0.994
Age Output : [[4.1081203e-04 1.9339744e-04 4.8858733e-03 1.8716091e-03 9.5307624e-01
  3.8392872e-02 8.6852764e-05 1.0824375e-03]]
Age : (25-32), conf = 0.953
time : 0.084
Gender : Male, conf = 0.987
Age Output : [[5.3893158e-04 3.9582475e-04 4.5295469e-03 2.6565951e-03 9.6638304e-01
  2.4336306e-02 5.6423047e-05 1.1033319e-03]]
Age : (25-32), conf = 0.966
time : 0.084
Gender : Male, conf = 0.976
Age Output : [[1.9826650e-04 1.2347083e-04 2.0050674e-03 7.9739979e-04 9.6959889e-01
  2.6628360e-02 6.1992039e-05 5.8662862e-04]]
Age : (25-32), conf = 0.970
time : 0.100
Gender : Male, conf = 0.963
Age Output : [[1.9174996e-04 1.3121119e-04 7.5509708e-04 8.7880786e-04 9.8959851e-01
  8.0919713e-03 3.2865857e-05 3.1967700e-04]]
Age : (25-32), conf = 0.990
time : 0.085
Gender : Male, conf = 0.975
Age Output : [[5.4002172e-05 7.8751327e-05 1.1234249e-03 6.0297211e-04 9.9055618e-01
  7.3823771e-03 3.4143395e-05 1.6831247e-04]]
Age : (25-32), conf = 0.991
time : 0.084
Gender : Male, conf = 0.956
Age Output : [[4.54448687e-04 1.48179693e-04 1.62278989e-03 1.96498935e-03
  9.53175604e-01 4.09816951e-02 1.06061765e-04 1.54636591e-03]]
Age : (25-32), conf = 0.953
time : 0.084
Gender : Male, conf = 0.989
Age Output : [[2.9801356e-04 1.9763593e-04 2.3805189e-03 2.9327930e-03 9.5231700e-01
  4.0829070e-02 9.0742025e-05 9.5423742e-04]]
Age : (25-32), conf = 0.952
time : 0.085
Gender : Male, conf = 0.974
Age Output : [[2.8057548e-04 1.4034228e-04 3.2696766e-03 2.0367315e-03 9.4789153e-01
  4.5621563e-02 9.0205431e-05 6.6934462e-04]]
Age : (25-32), conf = 0.948
time : 0.084
Gender : Male, conf = 0.993
Age Output : [[4.4124108e-02 7.5129839e-03 5.6315600e-03 4.2429301e-03 8.8109863e-01
  5.3883608e-02 4.2726059e-04 3.0787666e-03]]
Age : (25-32), conf = 0.881
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[2.5129865e-03 7.2710193e-04 3.9428831e-03 2.3635889e-03 9.3407071e-01
  5.4435868e-02 2.2290859e-04 1.7238886e-03]]
Age : (25-32), conf = 0.934
time : 0.084
Gender : Male, conf = 0.990
Age Output : [[5.5037042e-05 4.4100325e-05 1.2885761e-03 1.0413935e-03 9.7348952e-01
  2.3763165e-02 3.2428932e-05 2.8587077e-04]]
Age : (25-32), conf = 0.973
time : 0.084
Gender : Male, conf = 0.990
Age Output : [[5.5037042e-05 4.4100325e-05 1.2885761e-03 1.0413935e-03 9.7348952e-01
  2.3763165e-02 3.2428932e-05 2.8587077e-04]]
Age : (25-32), conf = 0.973
time : 0.084
Gender : Male, conf = 0.984
Age Output : [[1.4534786e-04 6.1560990e-05 1.2584405e-03 1.3904251e-03 9.3860191e-01
  5.7849027e-02 1.1270313e-04 5.8054592e-04]]
Age : (25-32), conf = 0.939
time : 0.085
Gender : Male, conf = 0.984
Age Output : [[1.4534786e-04 6.1560990e-05 1.2584405e-03 1.3904251e-03 9.3860191e-01
  5.7849027e-02 1.1270313e-04 5.8054592e-04]]
Age : (25-32), conf = 0.939
time : 0.084
Gender : Male, conf = 0.989
Age Output : [[4.9721630e-04 3.9294988e-04 6.6056759e-03 3.3399132e-03 9.4810283e-01
  4.0451132e-02 7.0167996e-05 5.4017449e-04]]
Age : (25-32), conf = 0.948
time : 0.083
Gender : Male, conf = 0.988
Age Output : [[2.7467703e-04 1.8624135e-04 2.0562836e-03 1.6041966e-03 9.6663052e-01
  2.8740779e-02 6.5546599e-05 4.4174690e-04]]
Age : (25-32), conf = 0.967
time : 0.123
Gender : Male, conf = 0.982
Age Output : [[2.1872243e-04 1.6790832e-04 1.9437600e-03 1.5624539e-03 9.7807729e-01
  1.7681461e-02 4.8420177e-05 3.0014681e-04]]
Age : (25-32), conf = 0.978
time : 0.084
Gender : Male, conf = 0.995
Age Output : [[3.5459271e-03 2.5569149e-03 1.8945208e-02 4.9354755e-03 9.1333008e-01
  5.5356633e-02 1.7996175e-04 1.1497289e-03]]
Age : (25-32), conf = 0.913
time : 0.084
Gender : Male, conf = 0.995
Age Output : [[3.5459271e-03 2.5569149e-03 1.8945208e-02 4.9354755e-03 9.1333008e-01
  5.5356633e-02 1.7996175e-04 1.1497289e-03]]
Age : (25-32), conf = 0.913
time : 0.084
Gender : Male, conf = 0.997
Age Output : [[5.8639208e-03 1.8650301e-03 1.3123403e-02 8.5870791e-03 7.9243761e-01
  1.7516153e-01 3.2352435e-04 2.6378408e-03]]
Age : (25-32), conf = 0.792
time : 0.085
Gender : Male, conf = 0.991
Age Output : [[1.4238075e-03 5.4497266e-04 7.6900567e-03 5.4549859e-03 8.4814513e-01
  1.3461177e-01 2.5069507e-04 1.8785353e-03]]
Age : (25-32), conf = 0.848
time : 0.085
Gender : Male, conf = 0.991
Age Output : [[1.4238075e-03 5.4497266e-04 7.6900567e-03 5.4549859e-03 8.4814513e-01
  1.3461177e-01 2.5069507e-04 1.8785353e-03]]
Age : (25-32), conf = 0.848
time : 0.085
Gender : Male, conf = 0.988
Age Output : [[5.6721724e-04 3.3392524e-04 4.3732068e-03 1.8379530e-03 9.5688808e-01
  3.5531193e-02 7.9876147e-05 3.8861495e-04]]
Age : (25-32), conf = 0.957
time : 0.084
Gender : Male, conf = 0.986
Age Output : [[4.7023807e-04 2.2956576e-04 1.4911172e-03 1.9617176e-03 9.6885622e-01
  2.6375148e-02 1.0420332e-04 5.1171606e-04]]
Age : (25-32), conf = 0.969
time : 0.084
Gender : Male, conf = 0.989
Age Output : [[3.1051962e-04 2.2559780e-04 4.3085073e-03 2.7185625e-03 9.5830071e-01
  3.3635698e-02 6.6447181e-05 4.3404338e-04]]
Age : (25-32), conf = 0.958
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[1.4330633e-04 1.3773185e-04 2.1189919e-03 1.2727620e-03 9.8032045e-01
  1.5740098e-02 8.4069266e-05 1.8266845e-04]]
Age : (25-32), conf = 0.980
time : 0.084
Gender : Male, conf = 0.996
Age Output : [[1.18756565e-04 8.41405999e-05 2.11546128e-03 1.50790077e-03
  9.71215308e-01 2.45726593e-02 5.36500193e-05 3.32175026e-04]]
Age : (25-32), conf = 0.971
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[2.7833696e-04 2.0131699e-04 2.2439330e-03 1.8927924e-03 9.7522461e-01
  1.9856283e-02 6.1736828e-05 2.4100328e-04]]
Age : (25-32), conf = 0.975
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[3.3120756e-04 2.8748930e-04 1.9301523e-03 1.6078238e-03 9.8866314e-01
  6.9951266e-03 2.5743240e-05 1.5935312e-04]]
Age : (25-32), conf = 0.989
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[5.8171347e-05 8.4546191e-05 2.4117576e-03 1.2578021e-03 9.8719239e-01
  8.8428743e-03 3.1792933e-05 1.2066632e-04]]
Age : (25-32), conf = 0.987
time : 0.085
Gender : Male, conf = 0.995
Age Output : [[4.5829976e-04 4.2905391e-04 5.4141474e-03 2.3428567e-03 9.7590226e-01
  1.5132514e-02 5.7956429e-05 2.6287162e-04]]
Age : (25-32), conf = 0.976
time : 0.084
Gender : Male, conf = 0.995
Age Output : [[4.5829976e-04 4.2905391e-04 5.4141474e-03 2.3428567e-03 9.7590226e-01
  1.5132514e-02 5.7956429e-05 2.6287162e-04]]
Age : (25-32), conf = 0.976
time : 0.085
Gender : Male, conf = 0.996
Age Output : [[4.9173232e-05 7.3808333e-05 1.9762348e-03 1.6048152e-03 9.8312861e-01
  1.2989184e-02 3.2574040e-05 1.4554676e-04]]
Age : (25-32), conf = 0.983
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>time : 0.084
Gender : Male, conf = 0.998
Age Output : [[5.3377461e-04 7.6477003e-04 1.2380600e-02 6.7790551e-03 9.5788556e-01
  2.1280324e-02 6.7267611e-05 3.0868655e-04]]
Age : (25-32), conf = 0.958
time : 0.084
Gender : Male, conf = 0.989
Age Output : [[1.6604905e-04 1.0938757e-04 2.7597100e-03 3.2476524e-03 9.6445960e-01
  2.8753543e-02 7.2181101e-05 4.3187462e-04]]
Age : (25-32), conf = 0.964
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[6.9707661e-05 3.9731152e-05 1.9545821e-03 1.8923290e-03 9.4782084e-01
  4.7778051e-02 7.7274897e-05 3.6738667e-04]]
Age : (25-32), conf = 0.948
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[3.5560588e-04 2.8931870e-04 4.6909521e-03 2.4843267e-03 9.6819478e-01
  2.3371957e-02 1.1053102e-04 5.0238811e-04]]
Age : (25-32), conf = 0.968
time : 0.084
Gender : Male, conf = 0.993
Age Output : [[2.7090887e-04 3.7000631e-04 2.1260174e-02 4.3021869e-03 9.3235493e-01
  4.0935028e-02 8.0022939e-05 4.2665578e-04]]
Age : (25-32), conf = 0.932
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[5.2050305e-05 7.7221805e-05 3.1194361e-03 3.3819235e-03 9.6949434e-01
  2.3647672e-02 4.8745140e-05 1.7851467e-04]]
Age : (25-32), conf = 0.969
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[5.2050305e-05 7.7221805e-05 3.1194361e-03 3.3819235e-03 9.6949434e-01
  2.3647672e-02 4.8745140e-05 1.7851467e-04]]
Age : (25-32), conf = 0.969
time : 0.085
Gender : Male, conf = 0.995
Age Output : [[8.9564850e-04 9.2876912e-04 1.3183172e-02 7.9651820e-03 9.5434952e-01
  2.2295140e-02 5.2972253e-05 3.2957061e-04]]
Age : (25-32), conf = 0.954
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[3.1350038e-04 4.3630230e-04 1.0992102e-02 5.8773477e-03 9.6004105e-01
  2.1918284e-02 6.3832718e-05 3.5750578e-04]]
Age : (25-32), conf = 0.960
time : 0.085
Gender : Male, conf = 0.998
Age Output : [[3.1316784e-05 7.0366601e-05 3.2289121e-03 5.6241401e-03 9.8074394e-01
  1.0111831e-02 2.7693453e-05 1.6168239e-04]]
Age : (25-32), conf = 0.981
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[5.3981381e-05 1.3449791e-04 2.3550976e-03 2.8986339e-03 9.8714918e-01
  7.2999801e-03 1.8844850e-05 8.9823116e-05]]
Age : (25-32), conf = 0.987
time : 0.084
Gender : Male, conf = 0.997
Age Output : [[7.2998540e-05 9.8248805e-05 8.5925488e-03 6.6741239e-03 9.2908674e-01
  5.4835595e-02 8.7439912e-05 5.5228709e-04]]
Age : (25-32), conf = 0.929
time : 0.085
Gender : Male, conf = 0.992
Age Output : [[1.5020920e-03 8.8003051e-04 8.2072467e-03 4.6395343e-03 9.5471185e-01
  2.9253922e-02 9.2340335e-05 7.1303698e-04]]
Age : (25-32), conf = 0.955
time : 0.085
Gender : Male, conf = 0.992
Age Output : [[1.5020920e-03 8.8003051e-04 8.2072467e-03 4.6395343e-03 9.5471185e-01
  2.9253922e-02 9.2340335e-05 7.1303698e-04]]
Age : (25-32), conf = 0.955
time : 0.125
Gender : Male, conf = 0.998
Age Output : [[2.1740758e-04 3.7309391e-04 1.5633438e-02 9.1950186e-03 9.3917489e-01
  3.4958970e-02 6.2172767e-05 3.8501903e-04]]
Age : (25-32), conf = 0.939
time : 0.302
Gender : Male, conf = 0.991
Age Output : [[4.8384638e-05 9.6416137e-05 3.2086542e-03 2.9612528e-03 9.7856438e-01
  1.4884088e-02 3.2055254e-05 2.0473232e-04]]
Age : (25-32), conf = 0.979
time : 0.184
Gender : Male, conf = 0.997
Age Output : [[9.9843205e-04 3.0978178e-04 1.8068997e-03 3.0115584e-03 9.1963005e-01
  7.2730236e-02 2.0128675e-04 1.3117231e-03]]
Age : (25-32), conf = 0.920
time : 0.088
Gender : Male, conf = 0.998
Age Output : [[7.1396452e-04 4.5079575e-04 5.1950710e-03 5.8998181e-03 9.4678748e-01
  4.0063161e-02 1.1007725e-04 7.7970081e-04]]
Age : (25-32), conf = 0.947
time : 0.085
Gender : Male, conf = 0.990
Age Output : [[2.9132864e-04 2.6535767e-04 7.3927552e-03 4.8409090e-03 9.2638510e-01
  5.9955198e-02 8.8035784e-05 7.8135158e-04]]
Age : (25-32), conf = 0.926
time : 0.197
Gender : Male, conf = 0.994
Age Output : [[1.1663939e-03 1.2476147e-03 5.1613795e-03 4.5178086e-03 9.6637118e-01
  2.0927606e-02 8.9965120e-05 5.1805819e-04]]
Age : (25-32), conf = 0.966
time : 0.123
Gender : Male, conf = 0.994
Age Output : [[0.02138706 0.00626327 0.01011775 0.00392892 0.8757769  0.07375133
  0.00091818 0.0078566 ]]
Age : (25-32), conf = 0.876
time : 0.126
Gender : Male, conf = 0.997
Age Output : [[0.53768545 0.07409072 0.08967704 0.0052514  0.16835687 0.11455431
  0.00087667 0.0095075 ]]
Age : (0-2), conf = 0.538
time : 0.131
Gender : Male, conf = 0.998
Age Output : [[0.09804627 0.02516649 0.03856745 0.00783576 0.60226846 0.2209992
  0.00103047 0.00608585]]
Age : (25-32), conf = 0.602
time : 0.138
Gender : Male, conf = 0.999
Age Output : [[0.01084814 0.00831629 0.06226276 0.00790481 0.5831323  0.3236937
  0.00069865 0.00314335]]
Age : (25-32), conf = 0.583
time : 0.131
Gender : Male, conf = 0.999
Age Output : [[0.05042029 0.00824524 0.01249737 0.00698843 0.59735495 0.31826195
  0.00068348 0.00554828]]
Age : (25-32), conf = 0.597
time : 0.124
Gender : Male, conf = 0.999
Age Output : [[4.2193495e-03 2.3266489e-03 2.4347680e-02 4.5139496e-03 7.8659540e-01
  1.7598887e-01 2.2357935e-04 1.7845262e-03]]
Age : (25-32), conf = 0.787
time : 0.123
Gender : Male, conf = 0.999
Age Output : [[6.3364250e-03 1.5131047e-02 9.5616139e-02 9.0049095e-03 8.0222887e-01
  6.9938585e-02 1.6689645e-04 1.5770961e-03]]
Age : (25-32), conf = 0.802
time : 0.126
Gender : Male, conf = 0.998
Age Output : [[2.6257804e-03 1.9065720e-03 2.0389728e-02 3.6541095e-03 8.5553777e-01
  1.1345214e-01 1.9691869e-04 2.2369393e-03]]
Age : (25-32), conf = 0.856
time : 0.128
Gender : Male, conf = 0.999
Age Output : [[3.6708932e-02 7.6901997e-03 1.0024051e-02 3.3442685e-03 8.8002384e-01
  5.9803713e-02 4.3288124e-04 1.9721740e-03]]
Age : (25-32), conf = 0.880
time : 0.119
Gender : Male, conf = 0.996
Age Output : [[2.7799094e-03 5.9515861e-04 2.3992511e-03 2.4344379e-03 9.5932889e-01
  3.1273961e-02 1.5834649e-04 1.0300344e-03]]
Age : (25-32), conf = 0.959
time : 0.116
Gender : Male, conf = 0.997
Age Output : [[1.1501105e-03 5.2536483e-04 5.3598736e-03 2.7922897e-03 9.6376538e-01
  2.5618020e-02 7.9836194e-05 7.0913276e-04]]
Age : (25-32), conf = 0.964
time : 0.116
Gender : Male, conf = 0.991
Age Output : [[7.9853192e-02 7.1174828e-03 1.2047085e-02 6.3094073e-03 7.8892797e-01
  9.8125726e-02 5.3521176e-04 7.0839697e-03]]
Age : (25-32), conf = 0.789
time : 0.131
Gender : Male, conf = 0.996
Age Output : [[1.1949745e-02 1.5763604e-03 6.2003685e-03 2.4835761e-03 9.2541713e-01
  4.9746916e-02 2.2081631e-04 2.4050823e-03]]
Age : (25-32), conf = 0.925
time : 0.138
Gender : Male, conf = 0.989
Age Output : [[2.0553490e-02 5.3665102e-03 2.4767287e-02 5.3950106e-03 8.9232117e-01
  4.8110630e-02 1.5622147e-04 3.3297082e-03]]
Age : (25-32), conf = 0.892
time : 0.116
Gender : Male, conf = 0.994
Age Output : [[1.2669355e-03 1.1674339e-03 8.3017483e-02 7.9409806e-03 6.1098218e-01
  2.9198059e-01 1.4620443e-04 3.4982048e-03]]
Age : (25-32), conf = 0.611
time : 0.131
Gender : Male, conf = 0.993
Age Output : [[6.6102901e-03 2.0014662e-03 2.2337347e-02 4.4971155e-03 8.4882224e-01
  1.1265324e-01 2.0786340e-04 2.8704931e-03]]
Age : (25-32), conf = 0.849
time : 0.107
Gender : Male, conf = 0.993
Age Output : [[6.8548255e-02 1.1737003e-02 5.1262852e-02 1.3742043e-02 7.8654104e-01
  6.5381788e-02 2.2042534e-04 2.5666046e-03]]
Age : (25-32), conf = 0.787
time : 0.224
Gender : Male, conf = 0.976
Age Output : [[2.7109584e-02 4.2784028e-03 4.7155045e-02 8.5196299e-03 6.8020034e-01
  2.2790369e-01 3.3115808e-04 4.5021605e-03]]
Age : (25-32), conf = 0.680
time : 0.176
Gender : Male, conf = 0.988
Age Output : [[1.5231402e-02 5.4363501e-03 3.1419277e-02 6.1603081e-03 9.0741891e-01
  3.3109829e-02 1.4081238e-04 1.0830775e-03]]
Age : (25-32), conf = 0.907
time : 0.132
Gender : Male, conf = 0.993
Age Output : [[0.04168651 0.00418932 0.04020399 0.00494697 0.71912265 0.18145086
  0.00075269 0.00764706]]
Age : (25-32), conf = 0.719
time : 0.113
Gender : Male, conf = 0.957
Age Output : [[3.7915914e-04 2.9014543e-04 2.9489506e-02 3.8150444e-03 9.3013114e-01
  3.5343561e-02 4.3882847e-05 5.0758955e-04]]
Age : (25-32), conf = 0.930
time : 0.102
Gender : Male, conf = 0.983
Age Output : [[3.0668810e-02 4.2572571e-03 5.7703517e-02 6.0858489e-03 8.3590621e-01
  6.2959351e-02 2.4836930e-04 2.1706366e-03]]
Age : (25-32), conf = 0.836
time : 0.113
Gender : Male, conf = 0.985
Age Output : [[2.5497768e-03 2.6709613e-04 9.0042148e-03 1.8534929e-03 9.2410952e-01
  6.0716737e-02 1.4025241e-04 1.3590120e-03]]
Age : (25-32), conf = 0.924
time : 0.125
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.993
Age Output : [[3.2723401e-02 3.0379270e-03 2.8796893e-02 4.5874240e-03 8.4807444e-01
  8.0033481e-02 2.5703217e-04 2.4894520e-03]]
Age : (25-32), conf = 0.848
time : 0.140
Gender : Male, conf = 0.990
Age Output : [[0.24378532 0.02288919 0.04339141 0.01810843 0.287415   0.367503
  0.00127878 0.01562888]]
Age : (38-43), conf = 0.368
time : 0.116
Gender : Male, conf = 0.990
Age Output : [[0.24378532 0.02288919 0.04339141 0.01810843 0.287415   0.367503
  0.00127878 0.01562888]]
Age : (38-43), conf = 0.368
time : 0.126
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.995
Age Output : [[7.9608790e-04 2.9810591e-02 8.6290184e-03 1.8269377e-02 8.3966249e-01
  1.0180991e-01 6.2278804e-04 3.9972534e-04]]
Age : (25-32), conf = 0.840
time : 0.085
Gender : Male, conf = 0.996
Age Output : [[2.8866701e-04 1.8354202e-02 4.2034634e-03 1.1037749e-02 9.2253757e-01
  4.2570349e-02 6.5977609e-04 3.4825597e-04]]
Age : (25-32), conf = 0.923
time : 0.103
Gender : Male, conf = 0.998
Age Output : [[0.00423878 0.24055815 0.01459711 0.02456891 0.5940461  0.11648136
  0.00359246 0.00191711]]
Age : (25-32), conf = 0.594
time : 0.099
Gender : Male, conf = 0.989
Age Output : [[0.0041816  0.5496569  0.01278    0.02042295 0.3890626  0.01083549
  0.01170047 0.00135999]]
Age : (4-6), conf = 0.550
time : 0.087
Gender : Male, conf = 0.842
Age Output : [[0.02169885 0.49050868 0.04510931 0.0940639  0.27050307 0.02669902
  0.04485238 0.00656479]]
Age : (4-6), conf = 0.491
time : 0.097
No face Detected, Checking next frame
Gender : Male, conf = 0.663
Age Output : [[0.00826657 0.5582322  0.02878121 0.16779503 0.19518147 0.00613434
  0.03005128 0.005558  ]]
Age : (4-6), conf = 0.558
time : 0.084
Gender : Male, conf = 0.554
Age Output : [[3.2513186e-03 9.2920810e-01 1.2506251e-02 3.2525189e-02 1.9535618e-02
  3.1532027e-04 2.2451093e-03 4.1295393e-04]]
Age : (4-6), conf = 0.929
time : 0.103
Gender : Male, conf = 0.920
Age Output : [[0.07898982 0.8243414  0.00808487 0.0057963  0.06456348 0.00180671
  0.01474813 0.00166919]]
Age : (4-6), conf = 0.824
time : 0.097
Gender : Male, conf = 0.952
Age Output : [[1.9443840e-01 7.8969598e-01 2.7856117e-03 2.2046722e-03 7.9156030e-03
  5.2920438e-04 2.1314176e-03 2.9919529e-04]]
Age : (4-6), conf = 0.790
time : 0.083
Gender : Male, conf = 0.961
Age Output : [[1.4834999e-02 9.7240126e-01 2.9938472e-03 2.1921392e-03 6.0727801e-03
  2.6281111e-04 1.1036532e-03 1.3853516e-04]]
Age : (4-6), conf = 0.972
time : 0.100
Gender : Male, conf = 0.961
Age Output : [[1.4834999e-02 9.7240126e-01 2.9938472e-03 2.1921392e-03 6.0727801e-03
  2.6281111e-04 1.1036532e-03 1.3853516e-04]]
Age : (4-6), conf = 0.972
time : 0.084
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.975
Age Output : [[0.00135975 0.15426682 0.22329152 0.23224796 0.2432582  0.14346357
  0.00109463 0.00101746]]
Age : (25-32), conf = 0.243
time : 0.096
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.958
Age Output : [[1.2490720e-03 3.9300519e-01 1.2304112e-01 2.3313412e-01 2.1862713e-01
  3.0588096e-02 1.9186862e-04 1.6343745e-04]]
Age : (4-6), conf = 0.393
time : 0.085
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.998
Age Output : [[3.9224070e-04 1.4215937e-02 2.4338830e-02 4.0110040e-01 5.1708605e-02
  5.0620037e-01 1.6279273e-03 4.1564889e-04]]
Age : (38-43), conf = 0.506
time : 0.093
Gender : Male, conf = 0.999
Age Output : [[3.86947475e-04 1.19325586e-01 1.53052852e-01 2.37278014e-01
  4.44528610e-01 4.49749045e-02 2.92928715e-04 1.60173295e-04]]
Age : (25-32), conf = 0.445
time : 0.102
Gender : Male, conf = 0.998
Age Output : [[4.5584285e-04 1.4552901e-02 2.1814020e-02 6.6488519e-02 5.5788785e-01
  3.3754429e-01 8.1237603e-04 4.4416718e-04]]
Age : (25-32), conf = 0.558
time : 0.083
Gender : Male, conf = 0.998
Age Output : [[4.5584285e-04 1.4552901e-02 2.1814020e-02 6.6488519e-02 5.5788785e-01
  3.3754429e-01 8.1237603e-04 4.4416718e-04]]
Age : (25-32), conf = 0.558
time : 0.084
Gender : Male, conf = 0.995
Age Output : [[0.00091145 0.0095554  0.02160819 0.13704033 0.45060098 0.378554
  0.00100848 0.00072114]]
Age : (25-32), conf = 0.451
time : 0.085
Gender : Male, conf = 0.993
Age Output : [[1.5396869e-04 9.3887076e-03 2.4827434e-02 3.3263631e-02 5.5522915e-02
  8.7641174e-01 2.9060643e-04 1.4103331e-04]]
Age : (38-43), conf = 0.876
time : 0.106
Gender : Male, conf = 1.000
Age Output : [[0.00252968 0.11153976 0.06666245 0.05634521 0.3813812  0.37963495
  0.00140674 0.00050002]]
Age : (25-32), conf = 0.381
time : 0.079
Gender : Male, conf = 0.999
Age Output : [[0.00330697 0.15878902 0.07607625 0.10472566 0.37998456 0.27515623
  0.00145609 0.00050522]]
Age : (25-32), conf = 0.380
time : 0.100
Gender : Male, conf = 0.998
Age Output : [[4.8067788e-05 3.1156901e-03 2.7029293e-02 5.7638988e-02 1.6828948e-01
  7.4343854e-01 3.0487674e-04 1.3506967e-04]]
Age : (38-43), conf = 0.743
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[1.3864519e-03 1.3302247e-01 1.9332433e-01 1.3533460e-01 3.7799183e-01
  1.5818503e-01 5.1110669e-04 2.4414941e-04]]
Age : (25-32), conf = 0.378
time : 0.101
Gender : Male, conf = 0.999
Age Output : [[0.00721702 0.26760453 0.06001118 0.12454113 0.3459588  0.19273877
  0.00145823 0.00047034]]
Age : (25-32), conf = 0.346
time : 0.089
Gender : Male, conf = 0.999
Age Output : [[2.0091003e-03 2.4251281e-01 9.1266245e-02 2.0451036e-01 3.1259853e-01
  1.4574896e-01 1.0461824e-03 3.0789609e-04]]
Age : (25-32), conf = 0.313
time : 0.108
No face Detected, Checking next frame
Gender : Male, conf = 0.999
Age Output : [[1.9746989e-03 1.3922800e-01 5.1955022e-02 8.2011640e-02 1.0157675e-01
  6.2068737e-01 2.0925065e-03 4.7407739e-04]]
Age : (38-43), conf = 0.621
time : 0.077
Gender : Male, conf = 0.997
Age Output : [[0.00582109 0.30725127 0.10368657 0.06649728 0.13996637 0.37421635
  0.00204417 0.00051684]]
Age : (38-43), conf = 0.374
time : 0.094
Gender : Male, conf = 0.999
Age Output : [[0.00398379 0.2748124  0.11425668 0.04632187 0.4260777  0.13173635
  0.00194145 0.00086973]]
Age : (25-32), conf = 0.426
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[0.01314647 0.45157543 0.0593251  0.02304661 0.3679066  0.08067543
  0.00319423 0.00113015]]
Age : (4-6), conf = 0.452
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[0.01314647 0.45157543 0.0593251  0.02304661 0.3679066  0.08067543
  0.00319423 0.00113015]]
Age : (4-6), conf = 0.452
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[1.6213488e-02 8.4120321e-01 3.7502524e-02 6.4402595e-03 7.5953305e-02
  2.0973388e-02 1.3213919e-03 3.9254283e-04]]
Age : (4-6), conf = 0.841
time : 0.100
Gender : Male, conf = 1.000
Age Output : [[2.2487792e-03 1.5699553e-01 3.4966961e-02 2.8709944e-02 7.3621255e-01
  3.9498117e-02 7.1185722e-04 6.5629097e-04]]
Age : (25-32), conf = 0.736
time : 0.087
Gender : Male, conf = 0.999
Age Output : [[0.10723459 0.5753357  0.02087534 0.00444368 0.2650656  0.02491355
  0.00130454 0.00082704]]
Age : (4-6), conf = 0.575
time : 0.103
Gender : Male, conf = 1.000
Age Output : [[7.3066640e-01 2.6175690e-01 2.7169744e-03 2.2759767e-04 3.5650053e-03
  9.1128447e-04 7.2330622e-05 8.3535480e-05]]
Age : (0-2), conf = 0.731
time : 0.087
Gender : Male, conf = 1.000
Age Output : [[6.4585286e-01 3.2844248e-01 1.3540544e-02 6.9931871e-04 5.3128274e-03
  5.8518378e-03 6.1797909e-05 2.3837457e-04]]
Age : (0-2), conf = 0.646
time : 0.103
Gender : Male, conf = 1.000
Age Output : [[1.8672712e-01 5.3989273e-01 3.9484613e-02 3.0471785e-03 2.1177629e-01
  1.8162591e-02 3.4186358e-04 5.6758313e-04]]
Age : (4-6), conf = 0.540
time : 0.081
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 1.000
Age Output : [[2.4312958e-01 7.4852723e-01 4.8303455e-03 2.0900351e-04 2.5832278e-03
  6.6438253e-04 2.4652893e-05 3.1536827e-05]]
Age : (4-6), conf = 0.749
time : 0.099
Gender : Male, conf = 1.000
Age Output : [[2.4312958e-01 7.4852723e-01 4.8303455e-03 2.0900351e-04 2.5832278e-03
  6.6438253e-04 2.4652893e-05 3.1536827e-05]]
Age : (4-6), conf = 0.749
time : 0.086
Gender : Male, conf = 1.000
Age Output : [[6.4538366e-01 3.4030905e-01 4.3465770e-03 3.1405722e-04 7.4687507e-03
  1.9250525e-03 1.0034121e-04 1.5247418e-04]]
Age : (0-2), conf = 0.645
time : 0.100
Gender : Male, conf = 0.996
Age Output : [[0.7154363  0.06168601 0.0131059  0.00138602 0.12341153 0.08245766
  0.00073172 0.00178488]]
Age : (0-2), conf = 0.715
time : 0.081
Gender : Male, conf = 0.999
Age Output : [[9.2005408e-01 6.5564707e-02 4.1154013e-03 2.5366657e-04 6.5301978e-03
  3.2424424e-03 9.1375812e-05 1.4822582e-04]]
Age : (0-2), conf = 0.920
time : 0.098
Gender : Male, conf = 0.999
Age Output : [[0.34502003 0.03756002 0.02821898 0.00348865 0.43623912 0.14643005
  0.00076564 0.00227753]]
Age : (25-32), conf = 0.436
time : 0.079
Gender : Male, conf = 1.000
Age Output : [[6.4107800e-01 1.3549298e-01 2.6680792e-02 1.9873178e-03 1.2966561e-01
  6.3509315e-02 4.9972191e-04 1.0863214e-03]]
Age : (0-2), conf = 0.641
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[0.45451388 0.11282383 0.02615994 0.00330418 0.31917557 0.08211923
  0.00069561 0.00120788]]
Age : (0-2), conf = 0.455
time : 0.094
Gender : Male, conf = 0.999
Age Output : [[0.422493   0.06858557 0.01445096 0.00292478 0.4170218  0.07190441
  0.00089851 0.00172089]]
Age : (0-2), conf = 0.422
time : 0.085
Gender : Male, conf = 1.000
Age Output : [[7.9456550e-01 1.2843481e-01 7.9014953e-03 7.3991081e-04 4.9641214e-02
  1.7391218e-02 5.5577175e-04 7.6993968e-04]]
Age : (0-2), conf = 0.795
time : 0.084
Gender : Male, conf = 1.000
Age Output : [[0.7175809  0.15946165 0.01404951 0.00139551 0.06123944 0.04412679
  0.00079097 0.00135523]]
Age : (0-2), conf = 0.718
time : 0.098
Gender : Male, conf = 0.997
Age Output : [[8.8763416e-01 8.6404786e-02 6.0687857e-03 4.7620587e-04 1.2544607e-02
  6.2063397e-03 3.2438705e-04 3.4079267e-04]]
Age : (0-2), conf = 0.888
time : 0.089
Gender : Male, conf = 0.997
Age Output : [[8.8763416e-01 8.6404786e-02 6.0687857e-03 4.7620587e-04 1.2544607e-02
  6.2063397e-03 3.2438705e-04 3.4079267e-04]]
Age : (0-2), conf = 0.888
time : 0.100
No face Detected, Checking next frame
Gender : Male, conf = 0.999
Age Output : [[9.3559182e-01 5.3194363e-02 1.2257363e-03 2.7659271e-04 7.1531008e-03
  2.1941583e-03 1.8735038e-04 1.7685076e-04]]
Age : (0-2), conf = 0.936
time : 0.093
Gender : Male, conf = 1.000
Age Output : [[8.4847528e-01 7.4589439e-02 3.4921586e-03 5.7738635e-04 6.1598163e-02
  1.0413866e-02 4.2405276e-04 4.2964015e-04]]
Age : (0-2), conf = 0.848
time : 0.093
Gender : Male, conf = 0.990
Age Output : [[3.5032369e-02 1.8677995e-02 1.5868587e-02 3.8848021e-03 9.0623158e-01
  1.9505626e-02 2.4287493e-04 5.5624382e-04]]
Age : (25-32), conf = 0.906
time : 0.085
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 1.000
Age Output : [[0.03334008 0.02577456 0.00555953 0.00818799 0.86619186 0.05899245
  0.00097749 0.00097608]]
Age : (25-32), conf = 0.866
time : 0.079
Gender : Male, conf = 0.999
Age Output : [[2.6095915e-04 7.5149070e-04 1.5290614e-03 3.0133838e-03 9.8772836e-01
  6.5404903e-03 7.1941999e-05 1.0436648e-04]]
Age : (25-32), conf = 0.988
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[2.6095915e-04 7.5149070e-04 1.5290614e-03 3.0133838e-03 9.8772836e-01
  6.5404903e-03 7.1941999e-05 1.0436648e-04]]
Age : (25-32), conf = 0.988
time : 0.085
No face Detected, Checking next frame
Gender : Male, conf = 1.000
Age Output : [[5.7325317e-03 6.2431800e-01 7.5704828e-02 3.1245274e-02 1.6363181e-01
  9.8849662e-02 2.9445181e-04 2.2339272e-04]]
Age : (4-6), conf = 0.624
time : 0.088
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 1.000
Age Output : [[5.2750931e-04 3.6459368e-02 3.0115681e-02 4.8505135e-02 5.7870853e-01
  3.0469176e-01 6.2507426e-04 3.6693839e-04]]
Age : (25-32), conf = 0.579
time : 0.094
Gender : Male, conf = 1.000
Age Output : [[5.2750931e-04 3.6459368e-02 3.0115681e-02 4.8505135e-02 5.7870853e-01
  3.0469176e-01 6.2507426e-04 3.6693839e-04]]
Age : (25-32), conf = 0.579
time : 0.090
Gender : Male, conf = 0.998
Age Output : [[3.7383259e-04 8.2231015e-03 8.7593962e-03 2.1293659e-02 3.3436111e-01
  6.2507761e-01 1.3454701e-03 5.6583853e-04]]
Age : (38-43), conf = 0.625
time : 0.078
Gender : Male, conf = 0.996
Age Output : [[0.00151496 0.01423805 0.01086883 0.02393061 0.32387453 0.6205124
  0.0039752  0.00108543]]
Age : (38-43), conf = 0.621
time : 0.093
No face Detected, Checking next frame
Gender : Male, conf = 0.997
Age Output : [[8.4027983e-05 1.7693881e-03 4.1368799e-03 3.4648143e-02 4.5909759e-01
  4.9795952e-01 1.8102333e-03 4.9415807e-04]]
Age : (38-43), conf = 0.498
time : 0.080
Gender : Male, conf = 0.997
Age Output : [[8.4027983e-05 1.7693881e-03 4.1368799e-03 3.4648143e-02 4.5909759e-01
  4.9795952e-01 1.8102333e-03 4.9415807e-04]]
Age : (38-43), conf = 0.498
time : 0.088
Gender : Male, conf = 0.987
Age Output : [[0.00165723 0.00915223 0.0098442  0.05684187 0.44269666 0.47405612
  0.00456144 0.00119025]]
Age : (38-43), conf = 0.474
time : 0.081
Gender : Male, conf = 0.994
Age Output : [[0.00096316 0.00707327 0.00887961 0.05005198 0.35881457 0.56932664
  0.00394727 0.0009436 ]]
Age : (38-43), conf = 0.569
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[5.2038813e-06 8.9282221e-05 2.0725850e-03 5.3369924e-02 4.4292274e-01
  5.0120491e-01 2.0128961e-04 1.3408613e-04]]
Age : (38-43), conf = 0.501
time : 0.084
Gender : Male, conf = 0.994
Age Output : [[3.9403153e-06 1.4240382e-04 6.2489910e-03 1.6435748e-01 5.6022543e-01
  2.6870185e-01 1.9194242e-04 1.2788440e-04]]
Age : (25-32), conf = 0.560
time : 0.104
Gender : Male, conf = 0.998
Age Output : [[8.4931060e-05 6.6573930e-04 2.0588564e-03 9.8245870e-03 6.4336020e-01
  3.4228089e-01 1.3797939e-03 3.4498691e-04]]
Age : (25-32), conf = 0.643
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[0.00133495 0.00421129 0.00373284 0.01711334 0.7171308  0.24845941
  0.00594818 0.00206916]]
Age : (25-32), conf = 0.717
time : 0.098
Gender : Male, conf = 0.997
Age Output : [[0.00133495 0.00421129 0.00373284 0.01711334 0.7171308  0.24845941
  0.00594818 0.00206916]]
Age : (25-32), conf = 0.717
time : 0.087
Gender : Male, conf = 0.999
Age Output : [[1.6572217e-04 5.4870434e-03 1.2427100e-02 1.2391704e-01 7.1276903e-01
  1.4429647e-01 5.2678154e-04 4.1071625e-04]]
Age : (25-32), conf = 0.713
time : 0.100
Gender : Male, conf = 0.999
Age Output : [[0.00817395 0.13195264 0.04080177 0.0581917  0.5383126  0.21824874
  0.00278308 0.00153552]]
Age : (25-32), conf = 0.538
time : 0.086
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Female, conf = 0.551
Age Output : [[1.5256574e-04 4.0045404e-03 3.1726205e-01 1.0865741e-01 4.8980317e-01
  7.9478420e-02 6.6251014e-05 5.7559332e-04]]
Age : (25-32), conf = 0.490
time : 0.087
No face Detected, Checking next frame
No face Detected, Checking next frame
Gender : Male, conf = 0.898
Age Output : [[0.00142394 0.03007065 0.16596946 0.00729203 0.6432369  0.12579393
  0.00683889 0.01937417]]
Age : (25-32), conf = 0.643
time : 0.100
No face Detected, Checking next frame
Gender : Male, conf = 0.770
Age Output : [[6.39950274e-04 2.36066747e-02 7.48356164e-01 8.26526731e-02
  1.01140045e-01 2.96958294e-02 1.04912254e-03 1.28594646e-02]]
Age : (8-12), conf = 0.748
time : 0.088
Gender : Male, conf = 0.770
Age Output : [[6.39950274e-04 2.36066747e-02 7.48356164e-01 8.26526731e-02
  1.01140045e-01 2.96958294e-02 1.04912254e-03 1.28594646e-02]]
Age : (8-12), conf = 0.748
time : 0.118
Gender : Male, conf = 0.877
Age Output : [[1.3792136e-03 1.2366990e-01 6.8166763e-01 1.7050730e-01 2.0412782e-02
  8.0360950e-04 7.5651144e-05 1.4838984e-03]]
Age : (8-12), conf = 0.682
time : 0.104
Gender : Male, conf = 0.884
Age Output : [[1.2470610e-03 2.1915725e-01 6.6724241e-01 9.9159487e-02 1.1971744e-02
  4.5307487e-04 7.5961805e-05 6.9305673e-04]]
Age : (8-12), conf = 0.667
time : 0.098
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.955
Age Output : [[1.1544037e-03 2.2514583e-01 6.6911656e-01 8.6026452e-02 1.7429721e-02
  4.5311099e-04 7.8694327e-05 5.9511967e-04]]
Age : (8-12), conf = 0.669
time : 0.103
Gender : Male, conf = 0.965
Age Output : [[2.4962780e-04 5.0240956e-02 8.0345386e-01 7.8122310e-02 6.6367626e-02
  7.9870346e-04 7.3931435e-05 6.9306249e-04]]
Age : (8-12), conf = 0.803
time : 0.083
Gender : Male, conf = 0.917
Age Output : [[3.66148626e-04 1.18529834e-01 7.39990234e-01 4.06121649e-02
  9.95400324e-02 8.10309022e-04 4.74958251e-05 1.03698883e-04]]
Age : (8-12), conf = 0.740
time : 0.106
Gender : Male, conf = 0.971
Age Output : [[6.4781103e-03 4.6456724e-01 1.6891845e-01 4.1427892e-02 3.1793204e-01
  3.0480186e-04 9.0438174e-05 2.8095051e-04]]
Age : (4-6), conf = 0.465
time : 0.094
Gender : Male, conf = 0.987
Age Output : [[2.0295342e-03 3.4847474e-01 2.6140764e-01 8.4545232e-02 3.0253163e-01
  7.6872361e-04 4.7445283e-05 1.9507518e-04]]
Age : (4-6), conf = 0.348
time : 0.125
Gender : Male, conf = 0.991
Age Output : [[2.7679794e-03 5.2551544e-01 2.8469712e-01 2.7857831e-02 1.5811805e-01
  7.6889928e-04 5.9596758e-05 2.1514467e-04]]
Age : (4-6), conf = 0.526
time : 0.098
Gender : Male, conf = 0.995
Age Output : [[2.0805647e-04 1.2101958e-01 3.9010537e-01 6.8114288e-02 4.1864631e-01
  1.7395701e-03 5.3227010e-05 1.1358062e-04]]
Age : (25-32), conf = 0.419
time : 0.130
Gender : Male, conf = 0.993
Age Output : [[3.0405069e-04 1.2446248e-01 3.7312645e-01 1.2641613e-01 3.7392583e-01
  1.4499528e-03 8.1892445e-05 2.3321362e-04]]
Age : (25-32), conf = 0.374
time : 0.118
Gender : Male, conf = 0.987
Age Output : [[2.1155534e-05 2.4895929e-02 5.2362746e-01 1.4593600e-01 3.0364653e-01
  1.6389636e-03 6.6802269e-05 1.6714774e-04]]
Age : (8-12), conf = 0.524
time : 0.132
Gender : Male, conf = 0.994
Age Output : [[6.9328060e-05 9.7810067e-02 7.5371832e-01 1.0087052e-01 4.6900183e-02
  3.7588552e-04 5.0355764e-05 2.0541086e-04]]
Age : (8-12), conf = 0.754
time : 0.116
Gender : Male, conf = 0.995
Age Output : [[1.6787027e-06 2.1443002e-04 4.0651098e-02 3.2697111e-02 9.2064583e-01
  5.5684708e-03 8.3387378e-05 1.3798483e-04]]
Age : (25-32), conf = 0.921
time : 0.129
Gender : Male, conf = 0.996
Age Output : [[4.9694239e-07 3.6890309e-05 1.6397875e-02 1.6308263e-02 9.6514690e-01
  1.9489874e-03 5.7688296e-05 1.0289642e-04]]
Age : (25-32), conf = 0.965
time : 0.113
Gender : Male, conf = 0.970
Age Output : [[2.8308256e-07 5.8992864e-06 3.5392663e-03 1.4132305e-02 9.7551936e-01
  6.5999883e-03 7.1069757e-05 1.3186608e-04]]
Age : (25-32), conf = 0.976
time : 0.116
Gender : Male, conf = 0.950
Age Output : [[2.1895185e-06 2.7178110e-05 1.6215766e-02 1.5624895e-02 9.5628101e-01
  9.7835660e-03 5.2612432e-04 1.5391905e-03]]
Age : (25-32), conf = 0.956
time : 0.136
Gender : Male, conf = 0.907
Age Output : [[8.7907029e-05 3.9952970e-03 2.3529655e-01 4.7174383e-02 6.7879438e-01
  1.4107068e-02 2.3691955e-03 1.8175200e-02]]
Age : (25-32), conf = 0.679
time : 0.116
Gender : Male, conf = 0.958
Age Output : [[3.40081851e-06 1.11829904e-04 6.22313246e-02 3.91969830e-02
  8.86587501e-01 9.54621471e-03 4.84783959e-04 1.83804007e-03]]
Age : (25-32), conf = 0.887
time : 0.116
Gender : Male, conf = 0.945
Age Output : [[4.4273602e-06 4.4820231e-04 9.2885450e-02 6.9136046e-02 8.2828814e-01
  8.2432674e-03 2.9590132e-04 6.9857517e-04]]
Age : (25-32), conf = 0.828
time : 0.121
Gender : Male, conf = 0.873
Age Output : [[3.2711791e-06 6.1707007e-04 3.1618068e-01 6.1722755e-02 6.1316878e-01
  7.6253740e-03 2.3965555e-04 4.4241510e-04]]
Age : (25-32), conf = 0.613
time : 0.117
Gender : Male, conf = 0.825
Age Output : [[5.2364303e-06 4.0528763e-04 5.0720226e-02 7.5170018e-02 8.6829782e-01
  4.3841279e-03 3.9453400e-04 6.2271277e-04]]
Age : (25-32), conf = 0.868
time : 0.133
Gender : Male, conf = 0.909
Age Output : [[1.1422124e-05 1.1940720e-03 1.6361329e-01 1.1469965e-01 7.1325886e-01
  5.7496224e-03 3.2888126e-04 1.1442343e-03]]
Age : (25-32), conf = 0.713
time : 0.114
Gender : Male, conf = 0.987
Age Output : [[1.3408882e-06 1.4475138e-04 9.8396219e-02 1.9108001e-02 8.4757549e-01
  3.4291647e-02 1.5901349e-04 3.2354868e-04]]
Age : (25-32), conf = 0.848
time : 0.122
Gender : Male, conf = 0.866
Age Output : [[2.4432229e-06 8.1102633e-05 8.5409164e-02 7.0104804e-03 7.9114437e-01
  1.1567351e-01 2.9965330e-04 3.7921741e-04]]
Age : (25-32), conf = 0.791
time : 0.116
Gender : Male, conf = 0.901
Age Output : [[2.5110949e-06 8.7307671e-05 1.6710743e-01 9.9520059e-03 7.6643711e-01
  5.5742413e-02 1.7658649e-04 4.9466873e-04]]
Age : (25-32), conf = 0.766
time : 0.119
Gender : Male, conf = 0.970
Age Output : [[2.8956415e-06 1.2753705e-04 1.9099748e-01 1.9840987e-02 7.0025307e-01
  8.7938771e-02 2.5359829e-04 5.8570458e-04]]
Age : (25-32), conf = 0.700
time : 0.119
Gender : Male, conf = 0.894
Age Output : [[3.2943740e-06 1.6699151e-04 2.5087413e-01 5.0572202e-02 6.7001629e-01
  2.7506392e-02 2.0403272e-04 6.5668765e-04]]
Age : (25-32), conf = 0.670
time : 0.117
Gender : Female, conf = 0.720
Age Output : [[6.0781832e-07 1.2086135e-04 1.1332093e-01 2.7158896e-02 8.5444432e-01
  4.8277099e-03 2.9942139e-05 9.6695534e-05]]
Age : (25-32), conf = 0.854
time : 0.115
No face Detected, Checking next frame
Gender : Female, conf = 0.598
Age Output : [[1.1800552e-06 2.6972510e-05 6.9497295e-02 8.0376826e-02 8.2394093e-01
  2.5918512e-02 9.1994327e-05 1.4625225e-04]]
Age : (25-32), conf = 0.824
time : 0.096
Gender : Male, conf = 0.556
Age Output : [[2.5228939e-05 2.1427511e-03 7.4420202e-01 2.7161393e-02 2.2303450e-01
  3.1961056e-03 4.6748872e-05 1.9123744e-04]]
Age : (8-12), conf = 0.744
time : 0.102
Gender : Male, conf = 0.556
Age Output : [[2.5228939e-05 2.1427511e-03 7.4420202e-01 2.7161393e-02 2.2303450e-01
  3.1961056e-03 4.6748872e-05 1.9123744e-04]]
Age : (8-12), conf = 0.744
time : 0.085
Gender : Male, conf = 0.778
Age Output : [[5.2884589e-05 2.5954312e-03 9.1027874e-01 2.2528781e-02 6.3478246e-02
  8.8531245e-04 2.4483721e-05 1.5616762e-04]]
Age : (8-12), conf = 0.910
time : 0.103
No face Detected, Checking next frame
Gender : Male, conf = 0.934
Age Output : [[8.6912729e-07 6.4418663e-04 9.8338449e-01 1.5168785e-03 1.2816360e-02
  1.6071423e-03 1.4007647e-05 1.6206008e-05]]
Age : (8-12), conf = 0.983
time : 0.120
No face Detected, Checking next frame
Gender : Male, conf = 0.952
Age Output : [[4.6807156e-05 6.2262584e-03 9.7727889e-01 1.6186838e-03 6.6291862e-03
  8.1383912e-03 1.4915818e-05 4.6803318e-05]]
Age : (8-12), conf = 0.977
time : 0.123
Gender : Male, conf = 0.981
Age Output : [[8.9731179e-02 5.1680636e-01 3.6458564e-01 1.2762343e-02 1.2692604e-02
  1.2015953e-03 3.6632194e-04 1.8539159e-03]]
Age : (4-6), conf = 0.517
time : 0.124
Gender : Male, conf = 0.970
Age Output : [[4.6046916e-03 9.9099781e-03 8.9671308e-01 1.6093984e-02 5.6460939e-02
  1.1305933e-02 2.0756909e-04 4.7038449e-03]]
Age : (8-12), conf = 0.897
time : 0.125
Gender : Male, conf = 0.987
Age Output : [[6.3188246e-04 1.6989670e-03 9.7069228e-01 4.4953101e-03 1.5271655e-02
  5.0416975e-03 8.1646445e-05 2.0865120e-03]]
Age : (8-12), conf = 0.971
time : 0.097
Gender : Male, conf = 0.986
Age Output : [[5.0126959e-04 2.7363966e-03 6.0181594e-01 1.8196531e-01 1.8537155e-01
  2.2745881e-02 2.5129272e-04 4.6123639e-03]]
Age : (8-12), conf = 0.602
time : 0.098
Gender : Male, conf = 0.991
Age Output : [[0.00240011 0.00743799 0.34969282 0.31672937 0.29388508 0.01449915
  0.00044157 0.01491394]]
Age : (8-12), conf = 0.350
time : 0.087
Gender : Male, conf = 0.991
Age Output : [[0.00240011 0.00743799 0.34969282 0.31672937 0.29388508 0.01449915
  0.00044157 0.01491394]]
Age : (8-12), conf = 0.350
time : 0.104
Gender : Male, conf = 0.995
Age Output : [[0.01263597 0.01654623 0.33361676 0.2562016  0.32192713 0.01214295
  0.00108672 0.04584259]]
Age : (8-12), conf = 0.334
time : 0.086
Gender : Male, conf = 0.994
Age Output : [[0.00228546 0.0103029  0.39478767 0.2798634  0.29167745 0.01000075
  0.00040108 0.01068137]]
Age : (8-12), conf = 0.395
time : 0.101
Gender : Male, conf = 0.993
Age Output : [[1.04018580e-03 6.11957209e-03 4.34473962e-01 1.95829824e-01
  3.40902567e-01 1.51875345e-02 3.23422370e-04 6.12288481e-03]]
Age : (8-12), conf = 0.434
time : 0.081
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.998
Age Output : [[2.5133460e-04 1.9268912e-03 3.7106085e-01 1.4776511e-01 4.7069618e-01
  6.6976333e-03 8.6255997e-05 1.5156924e-03]]
Age : (25-32), conf = 0.471
time : 0.100
Gender : Male, conf = 0.992
Age Output : [[7.8863243e-04 3.1603323e-03 1.1853202e-01 3.4734914e-01 5.1726961e-01
  4.9773231e-03 2.8557223e-04 7.6373522e-03]]
Age : (25-32), conf = 0.517
time : 0.081
Gender : Male, conf = 0.992
Age Output : [[7.8863243e-04 3.1603323e-03 1.1853202e-01 3.4734914e-01 5.1726961e-01
  4.9773231e-03 2.8557223e-04 7.6373522e-03]]
Age : (25-32), conf = 0.517
time : 0.105
Gender : Male, conf = 0.992
Age Output : [[1.2745913e-03 6.6259261e-03 6.7005664e-01 6.9446988e-02 2.3935813e-01
  7.5470102e-03 1.7103250e-04 5.5196756e-03]]
Age : (8-12), conf = 0.670
time : 0.082
Gender : Male, conf = 0.998
Age Output : [[6.1151799e-04 3.8237392e-03 3.6740014e-01 1.5424734e-01 4.6268439e-01
  6.3477261e-03 1.4572214e-04 4.7394112e-03]]
Age : (25-32), conf = 0.463
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[0.00683101 0.01569833 0.36405957 0.2184599  0.37029928 0.01248551
  0.00046597 0.01170044]]
Age : (25-32), conf = 0.370
time : 0.090
Gender : Male, conf = 0.991
Age Output : [[1.4948600e-03 6.2414035e-03 2.2498742e-01 2.6984665e-01 4.7738227e-01
  1.2037392e-02 4.0985440e-04 7.6001571e-03]]
Age : (25-32), conf = 0.477
time : 0.085
Gender : Male, conf = 0.996
Age Output : [[6.3712429e-04 3.4232764e-03 4.3107578e-01 1.6869439e-01 3.7757811e-01
  1.5587235e-02 1.8920224e-04 2.8148605e-03]]
Age : (8-12), conf = 0.431
time : 0.087
Gender : Male, conf = 0.987
Age Output : [[1.5342480e-03 1.3811222e-02 5.8819401e-01 2.4570689e-01 1.3733433e-01
  7.6680500e-03 1.9620812e-04 5.5550165e-03]]
Age : (8-12), conf = 0.588
time : 0.101
Gender : Male, conf = 0.987
Age Output : [[1.5342480e-03 1.3811222e-02 5.8819401e-01 2.4570689e-01 1.3733433e-01
  7.6680500e-03 1.9620812e-04 5.5550165e-03]]
Age : (8-12), conf = 0.588
time : 0.086
Gender : Male, conf = 0.991
Age Output : [[3.64660082e-04 2.89666187e-03 6.36332572e-01 1.42312229e-01
  2.04178289e-01 1.19153764e-02 1.01700396e-04 1.89850735e-03]]
Age : (8-12), conf = 0.636
time : 0.102
Gender : Male, conf = 0.996
Age Output : [[7.6548377e-04 2.4724945e-03 6.8116504e-01 7.5709797e-02 2.1168174e-01
  2.3307063e-02 2.0420698e-04 4.6941387e-03]]
Age : (8-12), conf = 0.681
time : 0.082
Gender : Male, conf = 0.991
Age Output : [[7.1723649e-04 3.6774394e-03 8.0054319e-01 5.9490461e-02 1.2370788e-01
  8.7914495e-03 9.2548813e-05 2.9798283e-03]]
Age : (8-12), conf = 0.801
time : 0.111
Gender : Male, conf = 0.997
Age Output : [[7.3745637e-04 6.3230186e-03 7.3171020e-01 6.9452003e-02 1.8339305e-01
  5.6540263e-03 1.7469947e-04 2.5555186e-03]]
Age : (8-12), conf = 0.732
time : 0.086
Gender : Male, conf = 0.992
Age Output : [[1.7735020e-04 1.9199781e-03 6.1865753e-01 6.4541869e-02 3.0717483e-01
  5.5683125e-03 1.2705677e-04 1.8331292e-03]]
Age : (8-12), conf = 0.619
time : 0.102
Gender : Male, conf = 0.989
Age Output : [[3.8354780e-04 1.0753131e-03 5.6377101e-01 3.9416004e-02 3.6126411e-01
  2.6197726e-02 3.0587395e-04 7.5864182e-03]]
Age : (8-12), conf = 0.564
time : 0.087
Gender : Male, conf = 0.996
Age Output : [[0.00277786 0.0130146  0.6869991  0.04903382 0.21211301 0.01405468
  0.00259628 0.01941057]]
Age : (8-12), conf = 0.687
time : 0.102
Gender : Male, conf = 0.998
Age Output : [[0.01163043 0.05216479 0.73409456 0.03211931 0.15443371 0.00585114
  0.00125067 0.00845528]]
Age : (8-12), conf = 0.734
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[0.18024705 0.0763674  0.4359357  0.01577068 0.2676465  0.0173373
  0.00094166 0.00575377]]
Age : (8-12), conf = 0.436
time : 0.102
Gender : Male, conf = 0.999
Age Output : [[9.6064061e-03 1.9712683e-02 4.2907700e-01 3.3801887e-02 4.8966768e-01
  1.6271174e-02 2.9782951e-04 1.5651972e-03]]
Age : (25-32), conf = 0.490
time : 0.085
Gender : Male, conf = 1.000
Age Output : [[2.57219101e-04 1.64273792e-04 1.47929415e-02 9.87850875e-03
  9.11649227e-01 6.26455620e-02 2.71402241e-04 3.40777508e-04]]
Age : (25-32), conf = 0.912
time : 0.101
Gender : Male, conf = 1.000
Age Output : [[0.05626402 0.00430035 0.01666862 0.00786879 0.81934226 0.09277955
  0.00138578 0.0013906 ]]
Age : (25-32), conf = 0.819
time : 0.083
Gender : Male, conf = 1.000
Age Output : [[0.05626402 0.00430035 0.01666862 0.00786879 0.81934226 0.09277955
  0.00138578 0.0013906 ]]
Age : (25-32), conf = 0.819
time : 0.084
Gender : Male, conf = 1.000
Age Output : [[8.5985499e-05 6.0668037e-05 1.0055522e-03 8.4214853e-03 9.4803411e-01
  4.1763593e-02 3.8780525e-04 2.4085626e-04]]
Age : (25-32), conf = 0.948
time : 0.081
Gender : Male, conf = 1.000
Age Output : [[2.6453435e-04 1.4213541e-04 1.7612589e-03 1.1990418e-02 9.5987260e-01
  2.5673492e-02 1.8456559e-04 1.1103974e-04]]
Age : (25-32), conf = 0.960
time : 0.089
Gender : Male, conf = 1.000
Age Output : [[6.0330553e-04 1.1125971e-04 8.3970465e-04 4.2659198e-03 9.0110922e-01
  9.2295446e-02 4.1897994e-04 3.5615536e-04]]
Age : (25-32), conf = 0.901
time : 0.084
Gender : Male, conf = 1.000
Age Output : [[4.1290376e-04 8.4376836e-05 8.7915343e-04 1.0795349e-02 8.8079500e-01
  1.0597760e-01 5.4458750e-04 5.1095308e-04]]
Age : (25-32), conf = 0.881
time : 0.090
Gender : Male, conf = 1.000
Age Output : [[4.1290376e-04 8.4376836e-05 8.7915343e-04 1.0795349e-02 8.8079500e-01
  1.0597760e-01 5.4458750e-04 5.1095308e-04]]
Age : (25-32), conf = 0.881
time : 0.083
Gender : Male, conf = 1.000
Age Output : [[0.08565107 0.00266093 0.00719759 0.00499897 0.8048087  0.0915104
  0.00127901 0.00189325]]
Age : (25-32), conf = 0.805
time : 0.091
Gender : Male, conf = 1.000
Age Output : [[3.3274002e-04 6.3480627e-05 2.6876149e-03 4.6199001e-03 9.4901657e-01
  4.2924479e-02 2.0688609e-04 1.4831990e-04]]
Age : (25-32), conf = 0.949
time : 0.084
Gender : Male, conf = 1.000
Age Output : [[2.0656164e-04 5.6052198e-05 2.8320537e-03 3.9943322e-03 9.5800281e-01
  3.4378059e-02 3.5697091e-04 1.7314563e-04]]
Age : (25-32), conf = 0.958
time : 0.090
Gender : Male, conf = 1.000
Age Output : [[2.7715313e-04 3.6519366e-05 5.8594375e-04 2.3607500e-03 7.9939568e-01
  1.9545312e-01 1.4689392e-03 4.2191704e-04]]
Age : (25-32), conf = 0.799
time : 0.083
Gender : Male, conf = 0.997
Age Output : [[0.09540223 0.00440794 0.00397098 0.00602646 0.8347125  0.05159061
  0.00213285 0.00175632]]
Age : (25-32), conf = 0.835
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[3.6006823e-02 1.5710468e-03 1.1132638e-02 2.5567212e-03 8.9166701e-01
  5.5909757e-02 5.4735423e-04 6.0862070e-04]]
Age : (25-32), conf = 0.892
time : 0.083
Gender : Male, conf = 0.999
Age Output : [[3.6006823e-02 1.5710468e-03 1.1132638e-02 2.5567212e-03 8.9166701e-01
  5.5909757e-02 5.4735423e-04 6.0862070e-04]]
Age : (25-32), conf = 0.892
time : 0.091
Gender : Male, conf = 1.000
Age Output : [[3.0059204e-03 8.9138566e-04 1.1537231e-03 1.4369357e-03 9.8849607e-01
  4.6767113e-03 2.1135951e-04 1.2789294e-04]]
Age : (25-32), conf = 0.988
time : 0.082
Gender : Male, conf = 0.999
Age Output : [[6.1091413e-03 2.8545382e-03 2.3159948e-03 2.5122380e-03 9.8294419e-01
  2.9091155e-03 2.0091643e-04 1.5389058e-04]]
Age : (25-32), conf = 0.983
time : 0.091
Gender : Male, conf = 1.000
Age Output : [[3.0464847e-03 8.0488302e-04 7.5785647e-04 1.1365932e-03 9.9110341e-01
  2.9546584e-03 8.8632987e-05 1.0751318e-04]]
Age : (25-32), conf = 0.991
time : 0.082
Gender : Male, conf = 1.000
Age Output : [[2.0766040e-04 3.2159776e-05 1.5833630e-04 8.5485488e-04 9.9078184e-01
  7.8114998e-03 6.5762419e-05 8.7815744e-05]]
Age : (25-32), conf = 0.991
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[1.3913861e-02 7.8859675e-04 8.9243473e-04 1.7886788e-03 9.6462226e-01
  1.7215973e-02 3.6585794e-04 4.1219607e-04]]
Age : (25-32), conf = 0.965
time : 0.082
Gender : Male, conf = 0.999
Age Output : [[1.3913861e-02 7.8859675e-04 8.9243473e-04 1.7886788e-03 9.6462226e-01
  1.7215973e-02 3.6585794e-04 4.1219607e-04]]
Age : (25-32), conf = 0.965
time : 0.107
Gender : Male, conf = 1.000
Age Output : [[0.3162038  0.01040595 0.00278272 0.00174039 0.6470338  0.01899003
  0.0016054  0.00123799]]
Age : (25-32), conf = 0.647
time : 0.076
Gender : Male, conf = 0.999
Age Output : [[5.6922100e-02 2.2375428e-03 1.6953398e-03 2.6545261e-03 9.1335148e-01
  2.1937015e-02 5.7326531e-04 6.2881986e-04]]
Age : (25-32), conf = 0.913
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>time : 0.091
Gender : Male, conf = 0.999
Age Output : [[0.04399471 0.00121649 0.00260316 0.00257402 0.8735853  0.0740004
  0.00091863 0.00110734]]
Age : (25-32), conf = 0.874
time : 0.082
Gender : Male, conf = 0.999
Age Output : [[8.4096187e-01 1.2870347e-02 5.6615300e-03 9.9571305e-04 1.3154480e-01
  6.9497391e-03 4.9358449e-04 5.2235287e-04]]
Age : (0-2), conf = 0.841
time : 0.091
Gender : Male, conf = 0.996
Age Output : [[1.4458587e-02 8.4610772e-04 1.4550755e-03 1.1829302e-03 9.6669888e-01
  1.4332490e-02 5.6692527e-04 4.5896869e-04]]
Age : (25-32), conf = 0.967
time : 0.086
Gender : Male, conf = 0.996
Age Output : [[1.4458587e-02 8.4610772e-04 1.4550755e-03 1.1829302e-03 9.6669888e-01
  1.4332490e-02 5.6692527e-04 4.5896869e-04]]
Age : (25-32), conf = 0.967
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[4.1432656e-02 8.9830573e-04 4.1004908e-03 1.9074130e-03 9.1013038e-01
  3.9458483e-02 1.2883409e-03 7.8387791e-04]]
Age : (25-32), conf = 0.910
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[1.5085225e-02 4.5994215e-04 2.3253486e-03 2.4235242e-03 7.8716558e-01
  1.9029030e-01 1.2048630e-03 1.0451751e-03]]
Age : (25-32), conf = 0.787
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[1.8188464e-03 1.3538735e-04 1.2620325e-03 2.1839961e-03 7.9908949e-01
  1.9040374e-01 3.5084954e-03 1.5980470e-03]]
Age : (25-32), conf = 0.799
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[1.7073214e-04 7.0340291e-05 3.8379247e-03 4.7006183e-03 8.9910942e-01
  9.1079764e-02 5.7682942e-04 4.5435614e-04]]
Age : (25-32), conf = 0.899
time : 0.091
Gender : Male, conf = 0.998
Age Output : [[3.4101156e-03 4.3901007e-04 5.2431580e-03 2.3228936e-02 8.3310628e-01
  1.3167694e-01 1.8528431e-03 1.0427131e-03]]
Age : (25-32), conf = 0.833
time : 0.085
Gender : Male, conf = 0.999
Age Output : [[0.38557118 0.00452255 0.02311859 0.00761    0.24826324 0.31600255
  0.01052145 0.00439049]]
Age : (0-2), conf = 0.386
time : 0.091
Gender : Male, conf = 0.998
Age Output : [[0.40597993 0.00944181 0.01150877 0.00946757 0.43224317 0.11698719
  0.00578471 0.00858686]]
Age : (25-32), conf = 0.432
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[6.7077373e-04 2.9034342e-04 2.3459005e-03 5.1245023e-03 9.7922015e-01
  1.1833067e-02 1.9714516e-04 3.1804742e-04]]
Age : (25-32), conf = 0.979
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[8.6835558e-03 9.3905278e-04 2.0616648e-03 4.8797424e-03 9.4960034e-01
  3.3004802e-02 3.3644811e-04 4.9432809e-04]]
Age : (25-32), conf = 0.950
time : 0.086
Gender : Male, conf = 0.999
Age Output : [[6.3778823e-03 1.7940422e-03 2.0919014e-03 1.8188938e-03 9.7444993e-01
  1.3009781e-02 2.2742232e-04 2.3008842e-04]]
Age : (25-32), conf = 0.974
time : 0.095
Gender : Male, conf = 1.000
Age Output : [[5.4873090e-04 1.7224111e-04 5.1982590e-04 8.7812729e-04 9.9148327e-01
  6.0194223e-03 1.3361574e-04 2.4483344e-04]]
Age : (25-32), conf = 0.991
time : 0.082
Gender : Male, conf = 1.000
Age Output : [[5.4873090e-04 1.7224111e-04 5.1982590e-04 8.7812729e-04 9.9148327e-01
  6.0194223e-03 1.3361574e-04 2.4483344e-04]]
Age : (25-32), conf = 0.991
time : 0.098
Gender : Male, conf = 0.995
Age Output : [[1.5892070e-03 6.9341826e-04 1.4223842e-03 3.6796411e-03 9.7747791e-01
  3.3848709e-03 1.7568612e-03 9.9956952e-03]]
Age : (25-32), conf = 0.977
time : 0.081
Gender : Male, conf = 0.994
Age Output : [[0.00574825 0.00121079 0.0016096  0.005761   0.95253    0.00794516
  0.00260162 0.0225936 ]]
Age : (25-32), conf = 0.953
time : 0.077
Gender : Male, conf = 0.998
Age Output : [[0.06896763 0.00972704 0.00759014 0.01117489 0.6725883  0.03214973
  0.02213611 0.17566614]]
Age : (25-32), conf = 0.673
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[0.09137364 0.01364683 0.00693363 0.00773401 0.5577681  0.02418413
  0.04146366 0.25689596]]
Age : (25-32), conf = 0.558
time : 0.078
Gender : Male, conf = 0.998
Age Output : [[0.04330552 0.01408979 0.00571896 0.00761703 0.7933054  0.04491832
  0.02385367 0.06719136]]
Age : (25-32), conf = 0.793
time : 0.084
Gender : Male, conf = 0.998
Age Output : [[0.01183666 0.00520011 0.01337026 0.00446242 0.72402906 0.0466213
  0.04328014 0.15120006]]
Age : (25-32), conf = 0.724
time : 0.091
Gender : Male, conf = 0.998
Age Output : [[0.00777311 0.01048859 0.01777741 0.00517261 0.74741155 0.04039729
  0.07569765 0.0952817 ]]
Age : (25-32), conf = 0.747
time : 0.083
Gender : Male, conf = 0.998
Age Output : [[0.01178275 0.0204404  0.0087074  0.00859925 0.92749757 0.0029177
  0.00741848 0.01263649]]
Age : (25-32), conf = 0.927
time : 0.092
Gender : Male, conf = 0.999
Age Output : [[6.7582150e-04 1.9763457e-03 5.6563653e-03 5.4557621e-03 9.7348988e-01
  2.9587711e-03 3.8790519e-03 5.9079756e-03]]
Age : (25-32), conf = 0.973
time : 0.084
Gender : Male, conf = 0.999
Age Output : [[9.1192924e-06 8.2022241e-05 1.6680759e-03 3.2878362e-03 9.9389368e-01
  7.1250810e-04 9.6215052e-05 2.5041826e-04]]
Age : (25-32), conf = 0.994
time : 0.092
Gender : Male, conf = 0.999
Age Output : [[0.05324698 0.04419291 0.0407287  0.01201006 0.72336376 0.01772332
  0.02598935 0.08274499]]
Age : (25-32), conf = 0.723
time : 0.083
Gender : Male, conf = 0.999
Age Output : [[0.05324698 0.04419291 0.0407287  0.01201006 0.72336376 0.01772332
  0.02598935 0.08274499]]
Age : (25-32), conf = 0.723
time : 0.098
Gender : Male, conf = 1.000
Age Output : [[0.00172542 0.00204456 0.00671058 0.00282498 0.96664065 0.00679895
  0.00280298 0.01045185]]
Age : (25-32), conf = 0.967
time : 0.079
Gender : Male, conf = 0.998
Age Output : [[1.9717099e-04 1.6406584e-04 3.6019474e-04 2.1329557e-03 9.8884892e-01
  4.3298244e-03 1.1072158e-03 2.8596856e-03]]
Age : (25-32), conf = 0.989
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[1.3901029e-05 1.9113042e-05 2.9180662e-04 1.5241778e-03 9.9653399e-01
  1.4175542e-03 3.8717408e-05 1.6076473e-04]]
Age : (25-32), conf = 0.997
time : 0.081
Gender : Male, conf = 0.999
Age Output : [[7.4734591e-05 1.9548177e-04 2.9471330e-03 4.7056507e-03 9.8796833e-01
  3.2101148e-03 1.6991200e-04 7.2872086e-04]]
Age : (25-32), conf = 0.988
time : 0.093
Gender : Male, conf = 0.999
Age Output : [[0.6144355  0.01392254 0.0073153  0.00389418 0.22770073 0.06898109
  0.01287363 0.05087705]]
Age : (0-2), conf = 0.614
time : 0.082
Gender : Male, conf = 0.999
Age Output : [[0.6144355  0.01392254 0.0073153  0.00389418 0.22770073 0.06898109
  0.01287363 0.05087705]]
Age : (0-2), conf = 0.614
time : 0.078
Gender : Male, conf = 0.998
Age Output : [[0.871198   0.02093245 0.00464561 0.00208414 0.06809812 0.01321275
  0.00490415 0.01492463]]
Age : (0-2), conf = 0.871
time : 0.101
Gender : Male, conf = 0.998
Age Output : [[0.11172234 0.01663686 0.01879137 0.00838997 0.7731694  0.0274853
  0.01050898 0.03329577]]
Age : (25-32), conf = 0.773
time : 0.091
Gender : Male, conf = 0.999
Age Output : [[0.70392066 0.05922639 0.01287607 0.00784553 0.20210162 0.0066851
  0.00240254 0.00494202]]
Age : (0-2), conf = 0.704
time : 0.103
Gender : Male, conf = 0.999
Age Output : [[0.01844909 0.01063791 0.02760672 0.00720446 0.9118839  0.01486335
  0.00153501 0.00781955]]
Age : (25-32), conf = 0.912
time : 0.085
Gender : Male, conf = 0.997
Age Output : [[0.5843498  0.0430515  0.02029141 0.00758338 0.28272355 0.02390627
  0.00794531 0.03014878]]
Age : (0-2), conf = 0.584
time : 0.101
Gender : Male, conf = 0.998
Age Output : [[0.8197568  0.04798599 0.01146047 0.00320413 0.10871866 0.00338666
  0.0015208  0.00396653]]
Age : (0-2), conf = 0.820
time : 0.087
Gender : Male, conf = 0.998
Age Output : [[0.8197568  0.04798599 0.01146047 0.00320413 0.10871866 0.00338666
  0.0015208  0.00396653]]
Age : (0-2), conf = 0.820
time : 0.092
Gender : Male, conf = 0.999
Age Output : [[0.5873732  0.0330863  0.03489605 0.00904476 0.2796545  0.02631178
  0.0051243  0.02450925]]
Age : (0-2), conf = 0.587
time : 0.093
Gender : Male, conf = 0.998
Age Output : [[0.8638045  0.03649124 0.00915845 0.00208932 0.07374788 0.0050001
  0.00209674 0.00761168]]
Age : (0-2), conf = 0.864
time : 0.103
Gender : Male, conf = 0.995
Age Output : [[0.91524833 0.02283643 0.00761811 0.00237519 0.02811324 0.00749945
  0.00208861 0.01422052]]
Age : (0-2), conf = 0.915
time : 0.082
Gender : Male, conf = 0.999
Age Output : [[0.20170693 0.01031878 0.03567834 0.03916128 0.45604578 0.1177643
  0.007501   0.13182357]]
Age : (25-32), conf = 0.456
time : 0.103
Gender : Male, conf = 0.996
Age Output : [[0.28836024 0.00737553 0.01612043 0.01356487 0.5407157  0.10356151
  0.00289537 0.02740647]]
Age : (25-32), conf = 0.541
time : 0.089
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.999
Age Output : [[8.7311882e-01 2.9339833e-02 2.5135789e-03 2.3747899e-03 8.9349054e-02
  2.0042567e-03 2.8780723e-04 1.0119014e-03]]
Age : (0-2), conf = 0.873
time : 0.103
Gender : Male, conf = 0.999
Age Output : [[0.4457687  0.01977144 0.00288535 0.00203304 0.5245601  0.00352557
  0.00059212 0.00086364]]
Age : (25-32), conf = 0.525
time : 0.080
Gender : Male, conf = 0.998
Age Output : [[2.1055646e-03 1.9011962e-04 4.0320758e-04 1.0010754e-03 9.8298001e-01
  1.2242872e-02 2.4984055e-04 8.2731206e-04]]
Age : (25-32), conf = 0.983
time : 0.097
Gender : Male, conf = 0.998
Age Output : [[2.1055646e-03 1.9011962e-04 4.0320758e-04 1.0010754e-03 9.8298001e-01
  1.2242872e-02 2.4984055e-04 8.2731206e-04]]
Age : (25-32), conf = 0.983
time : 0.078
Gender : Male, conf = 0.999
Age Output : [[2.6769359e-05 1.6245246e-04 2.0108331e-04 3.7936466e-03 9.9542713e-01
  2.9046467e-04 3.3697332e-05 6.4675769e-05]]
Age : (25-32), conf = 0.995
time : 0.084
Gender : Male, conf = 0.863
Age Output : [[0.05333002 0.50783694 0.34353048 0.03094499 0.05473686 0.00482423
  0.00180609 0.00299043]]
Age : (4-6), conf = 0.508
time : 0.085
Gender : Male, conf = 0.986
Age Output : [[0.12628148 0.28676546 0.1661597  0.0474998  0.35613865 0.00836143
  0.00311672 0.00567677]]
Age : (25-32), conf = 0.356
time : 0.100
Gender : Male, conf = 0.871
Age Output : [[0.16453436 0.18542257 0.05694681 0.04067931 0.5367326  0.00834115
  0.00314643 0.00419673]]
Age : (25-32), conf = 0.537
time : 0.085
Gender : Male, conf = 0.719
Age Output : [[0.23553382 0.15834002 0.04138727 0.01514329 0.5284735  0.01157642
  0.0041019  0.00544371]]
Age : (25-32), conf = 0.528
time : 0.100
Gender : Male, conf = 0.719
Age Output : [[0.23553382 0.15834002 0.04138727 0.01514329 0.5284735  0.01157642
  0.0041019  0.00544371]]
Age : (25-32), conf = 0.528
time : 0.089
Gender : Female, conf = 0.598
Age Output : [[0.36903164 0.3917685  0.05404542 0.00411007 0.16902481 0.00456597
  0.00373801 0.00371559]]
Age : (4-6), conf = 0.392
time : 0.081
Gender : Male, conf = 0.793
Age Output : [[9.6187246e-01 2.8736662e-02 1.5944646e-03 3.3373857e-04 5.5319327e-03
  8.6628058e-04 6.0823956e-04 4.5605266e-04]]
Age : (0-2), conf = 0.962
time : 0.085
Gender : Female, conf = 0.781
Age Output : [[0.51243937 0.28881803 0.06394365 0.00885017 0.10005423 0.01107226
  0.00674433 0.00807789]]
Age : (0-2), conf = 0.512
time : 0.099
Gender : Female, conf = 0.549
Age Output : [[9.84435380e-01 1.22537855e-02 8.12372484e-04 1.26096958e-04
  1.20427785e-03 4.68400714e-04 2.93467310e-04 4.06231789e-04]]
Age : (0-2), conf = 0.984
time : 0.088
Gender : Female, conf = 0.648
Age Output : [[0.8719863  0.09857254 0.01256511 0.00108134 0.01037581 0.00245289
  0.00132962 0.00163636]]
Age : (0-2), conf = 0.872
time : 0.101
Gender : Female, conf = 0.701
Age Output : [[0.81518036 0.11877395 0.02053261 0.0020133  0.02725484 0.00596801
  0.00418828 0.00608865]]
Age : (0-2), conf = 0.815
time : 0.123
Gender : Female, conf = 0.614
Age Output : [[0.725453   0.12549049 0.01453502 0.002428   0.11715741 0.00687887
  0.00478411 0.00327301]]
Age : (0-2), conf = 0.725
time : 0.100
Gender : Male, conf = 0.855
Age Output : [[0.6560443  0.13190241 0.01707746 0.00624563 0.1716528  0.0072977
  0.00412443 0.00565523]]
Age : (0-2), conf = 0.656
time : 0.082
Gender : Male, conf = 0.855
Age Output : [[0.6560443  0.13190241 0.01707746 0.00624563 0.1716528  0.0072977
  0.00412443 0.00565523]]
Age : (0-2), conf = 0.656
time : 0.100
Gender : Female, conf = 0.551
Age Output : [[8.9503020e-01 7.9911008e-02 3.2427870e-03 7.8208128e-04 1.8471200e-02
  1.2462774e-03 8.0842653e-04 5.0799549e-04]]
Age : (0-2), conf = 0.895
time : 0.105
Gender : Male, conf = 0.647
Age Output : [[0.76879454 0.17079903 0.01195299 0.00140215 0.04206578 0.00230456
  0.00160841 0.00107244]]
Age : (0-2), conf = 0.769
time : 0.119
Gender : Male, conf = 0.963
Age Output : [[0.61325145 0.20657918 0.02022075 0.0044458  0.14580198 0.00404638
  0.00216621 0.00348824]]
Age : (0-2), conf = 0.613
time : 0.119
Gender : Male, conf = 0.834
Age Output : [[0.56397116 0.11093976 0.01558025 0.00384213 0.29088473 0.00661727
  0.00356985 0.00459481]]
Age : (0-2), conf = 0.564
time : 0.131
Gender : Male, conf = 0.512
Age Output : [[0.4989883  0.16236487 0.01873881 0.00402253 0.30606747 0.00590458
  0.00235466 0.00155878]]
Age : (0-2), conf = 0.499
time : 0.122
Gender : Male, conf = 0.661
Age Output : [[0.34957135 0.29824576 0.02986655 0.01275936 0.30153373 0.00489608
  0.00135978 0.00176743]]
Age : (0-2), conf = 0.350
time : 0.116
Gender : Male, conf = 0.625
Age Output : [[2.6124537e-02 4.0495083e-02 7.9494510e-03 5.7374784e-03 9.1613322e-01
  2.3906105e-03 4.9552758e-04 6.7400595e-04]]
Age : (25-32), conf = 0.916
time : 0.116
Gender : Male, conf = 0.640
Age Output : [[3.8739990e-03 1.0267118e-02 3.2497186e-03 4.2135958e-03 9.7618890e-01
  1.6260491e-03 2.7978828e-04 3.0079662e-04]]
Age : (25-32), conf = 0.976
time : 0.122
Gender : Male, conf = 0.774
Age Output : [[4.8765833e-03 2.1930385e-02 8.1759887e-03 9.0392521e-03 9.5376575e-01
  1.6569899e-03 2.2580722e-04 3.2922611e-04]]
Age : (25-32), conf = 0.954
time : 0.116
Gender : Male, conf = 0.789
Age Output : [[6.8955366e-03 2.1448890e-02 6.5954980e-03 8.6906860e-03 9.5403385e-01
  1.6331800e-03 2.7692632e-04 4.2550426e-04]]
Age : (25-32), conf = 0.954
time : 0.116
Gender : Female, conf = 0.593
Age Output : [[1.09992114e-04 7.19616190e-04 5.97070262e-04 1.73028267e-03
  9.96220052e-01 4.74690140e-04 7.08757798e-05 7.74801010e-05]]
Age : (25-32), conf = 0.996
time : 0.123
Gender : Female, conf = 0.593
Age Output : [[1.09992114e-04 7.19616190e-04 5.97070262e-04 1.73028267e-03
  9.96220052e-01 4.74690140e-04 7.08757798e-05 7.74801010e-05]]
Age : (25-32), conf = 0.996
time : 0.115
Gender : Female, conf = 0.506
Age Output : [[1.8004086e-02 5.4403424e-02 1.3203555e-02 9.8379795e-03 9.0085346e-01
  2.4628101e-03 5.2319345e-04 7.1147690e-04]]
Age : (25-32), conf = 0.901
time : 0.116
Gender : Female, conf = 0.665
Age Output : [[2.0768726e-02 1.9156229e-01 6.0906824e-02 2.5330355e-02 6.9743204e-01
  2.4121103e-03 5.1146554e-04 1.0761602e-03]]
Age : (25-32), conf = 0.697
time : 0.122
Gender : Male, conf = 0.587
Age Output : [[0.06725793 0.3137701  0.04084191 0.02518866 0.54642415 0.00364924
  0.00086469 0.00200331]]
Age : (25-32), conf = 0.546
time : 0.131
Gender : Male, conf = 0.569
Age Output : [[0.04401917 0.08522712 0.01618762 0.0107266  0.83796847 0.0037543
  0.00099767 0.0011191 ]]
Age : (25-32), conf = 0.838
time : 0.168
Gender : Male, conf = 0.784
Age Output : [[1.8836062e-01 5.4393905e-01 3.4794122e-02 1.0072678e-02 2.2022574e-01
  1.2818226e-03 4.9925619e-04 8.2674070e-04]]
Age : (4-6), conf = 0.544
time : 0.121
Gender : Male, conf = 0.736
Age Output : [[0.19284981 0.31793076 0.03032801 0.01330275 0.4396491  0.00322559
  0.0010621  0.00165183]]
Age : (25-32), conf = 0.440
time : 0.132
Gender : Male, conf = 0.675
Age Output : [[0.08534306 0.2192187  0.03497073 0.01098392 0.644249   0.00293883
  0.00068175 0.00161393]]
Age : (25-32), conf = 0.644
time : 0.100
Gender : Male, conf = 0.906
Age Output : [[1.6506020e-02 1.6469927e-01 3.3996407e-02 5.0822645e-03 7.7741599e-01
  1.2851013e-03 3.0442231e-04 7.1047980e-04]]
Age : (25-32), conf = 0.777
time : 0.125
Gender : Male, conf = 0.891
Age Output : [[2.7618319e-02 1.8407854e-01 2.7536225e-02 4.2554582e-03 7.5308901e-01
  1.7685663e-03 5.3249969e-04 1.1213500e-03]]
Age : (25-32), conf = 0.753
time : 0.091
Gender : Male, conf = 0.921
Age Output : [[7.5025149e-03 1.5198715e-01 4.7537569e-02 3.4348278e-03 7.8754842e-01
  1.0591079e-03 2.7230554e-04 6.5823714e-04]]
Age : (25-32), conf = 0.788
time : 0.113
Gender : Male, conf = 0.516
Age Output : [[4.7414429e-02 7.1851611e-01 6.0863793e-02 2.4198757e-03 1.6911526e-01
  8.5969159e-04 2.5618123e-04 5.5464642e-04]]
Age : (4-6), conf = 0.719
time : 0.083
Gender : Male, conf = 0.804
Age Output : [[4.4234648e-02 5.0485677e-01 1.1720816e-01 1.0010737e-02 3.1977424e-01
  1.9785808e-03 3.4994737e-04 1.5868351e-03]]
Age : (4-6), conf = 0.505
time : 0.103
Gender : Male, conf = 0.689
Age Output : [[3.2729790e-02 7.5826061e-01 4.7988962e-02 3.3032568e-03 1.5588289e-01
  8.5567276e-04 4.5606840e-04 5.2293180e-04]]
Age : (4-6), conf = 0.758
time : 0.094
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.689
Age Output : [[3.2729790e-02 7.5826061e-01 4.7988962e-02 3.3032568e-03 1.5588289e-01
  8.5567276e-04 4.5606840e-04 5.2293180e-04]]
Age : (4-6), conf = 0.758
time : 0.123
Gender : Male, conf = 0.869
Age Output : [[6.0703163e-04 8.0483872e-03 3.2216904e-03 3.8482102e-03 9.8314559e-01
  8.4016687e-04 1.2391483e-04 1.6499877e-04]]
Age : (25-32), conf = 0.983
time : 0.113
Gender : Male, conf = 0.869
Age Output : [[6.0703163e-04 8.0483872e-03 3.2216904e-03 3.8482102e-03 9.8314559e-01
  8.4016687e-04 1.2391483e-04 1.6499877e-04]]
Age : (25-32), conf = 0.983
time : 0.106
Gender : Male, conf = 0.551
Age Output : [[6.2194455e-04 3.0448253e-03 3.4694918e-03 1.6438551e-03 9.8930281e-01
  1.4577793e-03 1.6092969e-04 2.9841266e-04]]
Age : (25-32), conf = 0.989
time : 0.116
Gender : Male, conf = 0.859
Age Output : [[3.0596277e-03 4.4314442e-03 2.7880727e-03 2.3156693e-03 9.8128742e-01
  4.7178334e-03 5.5254210e-04 8.4744900e-04]]
Age : (25-32), conf = 0.981
time : 0.122
Gender : Male, conf = 0.944
Age Output : [[0.08395908 0.06969132 0.01225233 0.00570286 0.814202   0.00913957
  0.00269671 0.00235602]]
Age : (25-32), conf = 0.814
time : 0.084
Gender : Male, conf = 0.944
Age Output : [[0.08395908 0.06969132 0.01225233 0.00570286 0.814202   0.00913957
  0.00269671 0.00235602]]
Age : (25-32), conf = 0.814
time : 0.100
Gender : Male, conf = 0.959
Age Output : [[0.01718489 0.03167242 0.01765068 0.00721074 0.9153107  0.00823726
  0.001177   0.0015563 ]]
Age : (25-32), conf = 0.915
time : 0.078
Gender : Male, conf = 0.677
Age Output : [[0.33166423 0.41571224 0.03344242 0.0072225  0.19588295 0.00760642
  0.00320817 0.00526091]]
Age : (4-6), conf = 0.416
time : 0.101
Gender : Male, conf = 0.846
Age Output : [[0.04318138 0.12672147 0.03325145 0.01273283 0.7733873  0.00691514
  0.0018543  0.00195607]]
Age : (25-32), conf = 0.773
time : 0.086
Gender : Male, conf = 0.866
Age Output : [[4.3904455e-03 2.4530675e-02 1.8903632e-02 1.5768981e-02 9.2888004e-01
  5.9867338e-03 6.8403070e-04 8.5541751e-04]]
Age : (25-32), conf = 0.929
time : 0.100
Gender : Male, conf = 0.866
Age Output : [[4.3904455e-03 2.4530675e-02 1.8903632e-02 1.5768981e-02 9.2888004e-01
  5.9867338e-03 6.8403070e-04 8.5541751e-04]]
Age : (25-32), conf = 0.929
time : 0.086
Gender : Male, conf = 0.815
Age Output : [[3.2164571e-03 2.3014294e-02 1.6811093e-02 1.1480134e-02 9.4267803e-01
  2.1016884e-03 2.7009036e-04 4.2824770e-04]]
Age : (25-32), conf = 0.943
time : 0.084
Gender : Male, conf = 0.643
Age Output : [[2.9111989e-03 2.4116728e-02 1.0966030e-02 1.5516462e-02 9.4352406e-01
  2.2879886e-03 3.0532535e-04 3.7213677e-04]]
Age : (25-32), conf = 0.944
time : 0.106
Gender : Male, conf = 0.724
Age Output : [[0.0269247  0.4193418  0.11621232 0.02316334 0.40672034 0.0057169
  0.0008192  0.00110133]]
Age : (4-6), conf = 0.419
time : 0.098
Gender : Male, conf = 0.641
Age Output : [[0.08632853 0.7319632  0.08560904 0.00973436 0.08099426 0.00361452
  0.0007971  0.00095893]]
Age : (4-6), conf = 0.732
time : 0.076
Gender : Male, conf = 0.761
Age Output : [[0.18413717 0.5849911  0.0593964  0.01846825 0.14506109 0.00491959
  0.00106551 0.00196094]]
Age : (4-6), conf = 0.585
time : 0.089
Gender : Female, conf = 0.924
Age Output : [[0.27480337 0.28878358 0.03195409 0.02002143 0.37412566 0.00564099
  0.00240695 0.00226395]]
Age : (25-32), conf = 0.374
time : 0.084
Gender : Female, conf = 0.772
Age Output : [[0.17181978 0.40437722 0.04050193 0.04854225 0.32557404 0.00619555
  0.00132633 0.00166287]]
Age : (4-6), conf = 0.404
time : 0.084
Gender : Female, conf = 0.772
Age Output : [[0.17181978 0.40437722 0.04050193 0.04854225 0.32557404 0.00619555
  0.00132633 0.00166287]]
Age : (4-6), conf = 0.404
time : 0.084
Gender : Male, conf = 0.540
Age Output : [[0.02699841 0.08763615 0.0492413  0.07403561 0.751505   0.00861582
  0.00097059 0.00099708]]
Age : (25-32), conf = 0.752
time : 0.099
Gender : Male, conf = 0.624
Age Output : [[0.11877248 0.28964606 0.04484712 0.06344243 0.47211137 0.00767526
  0.00165586 0.00184932]]
Age : (25-32), conf = 0.472
time : 0.085
Gender : Female, conf = 0.605
Age Output : [[2.4989906e-01 7.1039671e-01 2.1720730e-02 4.9872301e-03 1.1751526e-02
  7.7542872e-04 2.0949947e-04 2.5970367e-04]]
Age : (4-6), conf = 0.710
time : 0.100
Gender : Male, conf = 0.662
Age Output : [[3.1093585e-01 6.1860132e-01 3.2057967e-02 5.7371869e-03 2.9746778e-02
  1.8076095e-03 5.0857483e-04 6.0477928e-04]]
Age : (4-6), conf = 0.619
time : 0.100
Gender : Female, conf = 0.587
Age Output : [[1.5173256e-01 7.9694599e-01 4.1255426e-02 2.9339259e-03 5.9235091e-03
  6.8822410e-04 1.8722702e-04 3.3316721e-04]]
Age : (4-6), conf = 0.797
time : 0.101
Gender : Male, conf = 0.639
Age Output : [[1.6597597e-01 8.1441396e-01 1.6190704e-02 6.3314388e-04 2.3602569e-03
  2.1492172e-04 9.2112045e-05 1.1890280e-04]]
Age : (4-6), conf = 0.814
time : 0.084
Gender : Female, conf = 0.587
Age Output : [[2.2267309e-01 7.3727661e-01 3.3565622e-02 1.5024713e-03 4.0474986e-03
  4.7049057e-04 2.0712284e-04 2.5708420e-04]]
Age : (4-6), conf = 0.737
time : 0.100
Gender : Female, conf = 0.587
Age Output : [[2.2267309e-01 7.3727661e-01 3.3565622e-02 1.5024713e-03 4.0474986e-03
  4.7049057e-04 2.0712284e-04 2.5708420e-04]]
Age : (4-6), conf = 0.737
time : 0.088
Gender : Male, conf = 0.662
Age Output : [[2.8688607e-01 7.0343822e-01 7.9993587e-03 3.5546004e-04 1.1077047e-03
  8.5567728e-05 5.4149496e-05 7.3397758e-05]]
Age : (4-6), conf = 0.703
time : 0.102
Gender : Female, conf = 0.736
Age Output : [[7.4579215e-01 2.4617963e-01 5.7559656e-03 3.6204400e-04 1.5603332e-03
  1.3114935e-04 8.0015008e-05 1.3876978e-04]]
Age : (0-2), conf = 0.746
time : 0.086
Gender : Male, conf = 0.520
Age Output : [[6.72271073e-01 3.15285504e-01 9.05417185e-03 6.48936664e-04
  2.26151687e-03 1.87127909e-04 1.18392105e-04 1.73343855e-04]]
Age : (0-2), conf = 0.672
time : 0.085
Gender : Female, conf = 0.680
Age Output : [[6.6955233e-01 3.2154942e-01 6.6399444e-03 4.2355404e-04 1.4424276e-03
  1.5097157e-04 9.0858710e-05 1.5051871e-04]]
Age : (0-2), conf = 0.670
time : 0.087
Gender : Female, conf = 0.618
Age Output : [[6.7922813e-01 3.1285357e-01 5.6463052e-03 4.0889106e-04 1.5302466e-03
  1.2360755e-04 8.1970320e-05 1.2729880e-04]]
Age : (0-2), conf = 0.679
time : 0.085
Gender : Female, conf = 0.850
Age Output : [[5.2479815e-01 4.5872247e-01 1.2368647e-02 5.0851132e-04 3.0694113e-03
  2.0833718e-04 1.3240792e-04 1.9209961e-04]]
Age : (0-2), conf = 0.525
time : 0.088
Gender : Female, conf = 0.512
Age Output : [[3.3323777e-01 6.4903772e-01 1.3142050e-02 5.9688033e-04 3.5898406e-03
  1.5236605e-04 9.2885799e-05 1.5045296e-04]]
Age : (4-6), conf = 0.649
time : 0.087
Gender : Female, conf = 0.579
Age Output : [[2.7015212e-01 7.0154232e-01 2.1909736e-02 1.2252236e-03 4.5786737e-03
  2.7014717e-04 1.1981701e-04 2.0197489e-04]]
Age : (4-6), conf = 0.702
time : 0.082
Gender : Male, conf = 0.504
Age Output : [[1.8962370e-01 7.6646656e-01 3.6031853e-02 1.4446075e-03 5.6209019e-03
  3.9506893e-04 1.4967524e-04 2.6759694e-04]]
Age : (4-6), conf = 0.766
time : 0.089
Gender : Male, conf = 0.507
Age Output : [[2.5963190e-01 6.9826573e-01 2.3618139e-02 1.7697775e-03 1.5657185e-02
  4.4673815e-04 2.4002125e-04 3.7058219e-04]]
Age : (4-6), conf = 0.698
time : 0.080
Gender : Male, conf = 0.612
Age Output : [[1.8448004e-01 7.3007542e-01 4.7460448e-02 2.8741106e-03 3.3319976e-02
  7.5903407e-04 3.8824810e-04 6.4280425e-04]]
Age : (4-6), conf = 0.730
time : 0.088
Gender : Female, conf = 0.867
Age Output : [[9.1704056e-02 7.3793668e-01 1.5282479e-01 2.3369940e-03 1.4084141e-02
  5.0522172e-04 1.8867374e-04 4.1942575e-04]]
Age : (4-6), conf = 0.738
time : 0.081
Gender : Female, conf = 0.531
Age Output : [[1.4126976e-01 8.0604690e-01 4.5471556e-02 1.1760090e-03 5.4948851e-03
  1.9654965e-04 1.2298849e-04 2.2130030e-04]]
Age : (4-6), conf = 0.806
time : 0.085
Gender : Female, conf = 0.821
Age Output : [[1.7989844e-01 7.7379560e-01 3.7870254e-02 1.8856387e-03 5.2388539e-03
  5.7514932e-04 3.0035459e-04 4.3568190e-04]]
Age : (4-6), conf = 0.774
time : 0.089
Gender : Female, conf = 0.821
Age Output : [[1.7989844e-01 7.7379560e-01 3.7870254e-02 1.8856387e-03 5.2388539e-03
  5.7514932e-04 3.0035459e-04 4.3568190e-04]]
Age : (4-6), conf = 0.774
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>time : 0.085
Gender : Female, conf = 0.652
Age Output : [[3.4787720e-01 6.1361861e-01 2.8496578e-02 2.4064598e-03 6.0360087e-03
  6.6042121e-04 3.0478477e-04 5.9991790e-04]]
Age : (4-6), conf = 0.614
time : 0.088
Gender : Male, conf = 0.584
Age Output : [[5.3231955e-01 4.5652708e-01 8.7017408e-03 4.1819850e-04 1.6607136e-03
  1.5278702e-04 8.9735717e-05 1.3011994e-04]]
Age : (0-2), conf = 0.532
time : 0.084
Gender : Female, conf = 0.791
Age Output : [[1.6638835e-01 7.1955997e-01 9.7846150e-02 4.7851768e-03 9.1665834e-03
  1.3042021e-03 4.1848136e-04 5.3112942e-04]]
Age : (4-6), conf = 0.720
time : 0.085
Gender : Female, conf = 0.791
Age Output : [[1.6638835e-01 7.1955997e-01 9.7846150e-02 4.7851768e-03 9.1665834e-03
  1.3042021e-03 4.1848136e-04 5.3112942e-04]]
Age : (4-6), conf = 0.720
time : 0.099
Gender : Female, conf = 0.746
Age Output : [[5.4656702e-01 4.3943200e-01 1.1051498e-02 7.6779374e-04 1.7701720e-03
  1.8711734e-04 9.1758942e-05 1.3262749e-04]]
Age : (0-2), conf = 0.547
time : 0.087
Gender : Female, conf = 0.746
Age Output : [[5.4656702e-01 4.3943200e-01 1.1051498e-02 7.6779374e-04 1.7701720e-03
  1.8711734e-04 9.1758942e-05 1.3262749e-04]]
Age : (0-2), conf = 0.547
time : 0.100
Gender : Female, conf = 0.523
Age Output : [[2.8622144e-01 6.9038141e-01 1.8935664e-02 1.0216658e-03 2.7509220e-03
  3.2603330e-04 1.6208860e-04 2.0069575e-04]]
Age : (4-6), conf = 0.690
time : 0.086
Gender : Male, conf = 0.958
Age Output : [[0.18066294 0.5610462  0.05810827 0.01889607 0.17536843 0.0034611
  0.00104756 0.00140943]]
Age : (4-6), conf = 0.561
time : 0.099
Gender : Male, conf = 0.796
Age Output : [[5.08096516e-01 4.63264197e-01 1.21116685e-02 2.03651818e-03
  1.30557111e-02 6.60371501e-04 3.52471572e-04 4.22607060e-04]]
Age : (0-2), conf = 0.508
time : 0.085
Gender : Male, conf = 0.615
Age Output : [[3.6381760e-01 6.0856205e-01 1.7406352e-02 1.7508226e-03 7.3620779e-03
  4.8932474e-04 2.6298541e-04 3.4877539e-04]]
Age : (4-6), conf = 0.609
time : 0.098
Gender : Male, conf = 0.615
Age Output : [[3.6381760e-01 6.0856205e-01 1.7406352e-02 1.7508226e-03 7.3620779e-03
  4.8932474e-04 2.6298541e-04 3.4877539e-04]]
Age : (4-6), conf = 0.609
time : 0.088
Gender : Male, conf = 0.809
Age Output : [[4.7532582e-01 5.0698251e-01 1.1840054e-02 1.1028597e-03 3.9375015e-03
  3.5118603e-04 1.9621079e-04 2.6381903e-04]]
Age : (4-6), conf = 0.507
time : 0.104
Gender : Male, conf = 0.842
Age Output : [[0.0630668  0.54925907 0.17212103 0.02489119 0.18419522 0.00400177
  0.00108147 0.00138348]]
Age : (4-6), conf = 0.549
time : 0.085
Gender : Male, conf = 0.846
Age Output : [[5.0805777e-01 4.8102427e-01 7.7710445e-03 6.0189329e-04 2.0854725e-03
  1.8579878e-04 1.1698903e-04 1.5666916e-04]]
Age : (0-2), conf = 0.508
time : 0.084
Gender : Male, conf = 0.934
Age Output : [[0.06963108 0.698095   0.09570365 0.01353686 0.11857058 0.00258374
  0.00098719 0.00089189]]
Age : (4-6), conf = 0.698
time : 0.087
Gender : Male, conf = 0.633
Age Output : [[5.8707833e-01 3.9955324e-01 1.0053654e-02 8.0245419e-04 1.5957194e-03
  3.8475971e-04 1.9410787e-04 3.3764663e-04]]
Age : (0-2), conf = 0.587
time : 0.101
Gender : Male, conf = 0.877
Age Output : [[0.16637102 0.4857924  0.10353497 0.02363263 0.21236683 0.00474429
  0.00179887 0.00175899]]
Age : (4-6), conf = 0.486
time : 0.090
Gender : Male, conf = 0.877
Age Output : [[0.16637102 0.4857924  0.10353497 0.02363263 0.21236683 0.00474429
  0.00179887 0.00175899]]
Age : (4-6), conf = 0.486
time : 0.103
Gender : Male, conf = 0.835
Age Output : [[0.33079538 0.5647518  0.03753545 0.00792096 0.05359653 0.00260647
  0.00152943 0.00126406]]
Age : (4-6), conf = 0.565
time : 0.083
Gender : Male, conf = 0.655
Age Output : [[4.7169486e-01 5.0917572e-01 1.2830264e-02 1.5925235e-03 3.5815211e-03
  4.5798981e-04 2.5213993e-04 4.1501739e-04]]
Age : (4-6), conf = 0.509
time : 0.098
Gender : Female, conf = 0.580
Age Output : [[0.22657135 0.5754969  0.08402982 0.01690344 0.08886643 0.00463638
  0.00140364 0.00209201]]
Age : (4-6), conf = 0.575
time : 0.089
Gender : Male, conf = 0.948
Age Output : [[3.9263386e-01 5.8273602e-01 1.9487405e-02 1.9100545e-03 1.7177135e-03
  7.0698455e-04 2.2216815e-04 5.8581034e-04]]
Age : (4-6), conf = 0.583
time : 0.102
Gender : Female, conf = 0.515
Age Output : [[3.0823934e-01 6.3223779e-01 4.6171144e-02 4.4539259e-03 6.2730066e-03
  1.2769599e-03 4.8131862e-04 8.6658372e-04]]
Age : (4-6), conf = 0.632
time : 0.082
Gender : Male, conf = 0.600
Age Output : [[1.5079814e-01 7.5844145e-01 8.3226345e-02 3.2177304e-03 3.1638769e-03
  5.8511837e-04 2.2806454e-04 3.3935366e-04]]
Age : (4-6), conf = 0.758
time : 0.101
Gender : Male, conf = 0.582
Age Output : [[0.36509785 0.53166234 0.08474454 0.00519315 0.0088738  0.00277201
  0.00063631 0.00102   ]]
Age : (4-6), conf = 0.532
time : 0.083
Gender : Male, conf = 0.582
Age Output : [[0.36509785 0.53166234 0.08474454 0.00519315 0.0088738  0.00277201
  0.00063631 0.00102   ]]
Age : (4-6), conf = 0.532
time : 0.104
Gender : Male, conf = 0.730
Age Output : [[0.30259332 0.27185884 0.20866661 0.03067116 0.13715728 0.03665321
  0.00580599 0.0065936 ]]
Age : (0-2), conf = 0.303
time : 0.078
Gender : Male, conf = 0.741
Age Output : [[0.45377672 0.40478662 0.09665927 0.00718186 0.02318123 0.0097829
  0.00217419 0.00245734]]
Age : (0-2), conf = 0.454
time : 0.100
Gender : Male, conf = 0.804
Age Output : [[0.18185622 0.3907433  0.2712871  0.02809886 0.09290791 0.02600626
  0.00442384 0.00467655]]
Age : (4-6), conf = 0.391
time : 0.084
Gender : Female, conf = 0.573
Age Output : [[0.11497539 0.27870712 0.28233898 0.04594535 0.23114768 0.03437425
  0.00744991 0.00506135]]
Age : (8-12), conf = 0.282
time : 0.099
Gender : Female, conf = 0.739
Age Output : [[0.1863135  0.27748397 0.17655931 0.03481266 0.2946891  0.02170755
  0.00445169 0.00398224]]
Age : (25-32), conf = 0.295
time : 0.084
Gender : Male, conf = 0.519
Age Output : [[0.26533574 0.5704188  0.11824503 0.0088318  0.0315821  0.00360687
  0.00096836 0.00101131]]
Age : (4-6), conf = 0.570
time : 0.101
Gender : Female, conf = 0.757
Age Output : [[0.12828274 0.53777933 0.24046971 0.01717796 0.06600869 0.00720501
  0.00155115 0.00152538]]
Age : (4-6), conf = 0.538
time : 0.083
Gender : Female, conf = 0.905
Age Output : [[0.11464996 0.42678103 0.2789331  0.01712481 0.1481648  0.01040145
  0.00214573 0.00179919]]
Age : (4-6), conf = 0.427
time : 0.101
Gender : Female, conf = 0.905
Age Output : [[0.11464996 0.42678103 0.2789331  0.01712481 0.1481648  0.01040145
  0.00214573 0.00179919]]
Age : (4-6), conf = 0.427
time : 0.080
Gender : Female, conf = 0.865
Age Output : [[0.06401164 0.3352789  0.26187494 0.01712042 0.3061761  0.01192854
  0.00208813 0.00152139]]
Age : (4-6), conf = 0.335
time : 0.084
Gender : Male, conf = 0.734
Age Output : [[0.11625315 0.52332187 0.31205904 0.00748865 0.03441511 0.00454341
  0.00092955 0.00098926]]
Age : (4-6), conf = 0.523
time : 0.083
Gender : Male, conf = 0.636
Age Output : [[0.11454253 0.52306014 0.25096712 0.01141427 0.09151372 0.00593564
  0.00143546 0.00113112]]
Age : (4-6), conf = 0.523
time : 0.087
Gender : Female, conf = 0.840
Age Output : [[0.12883447 0.34359312 0.29363635 0.020415   0.19860752 0.011243
  0.0018718  0.00179877]]
Age : (4-6), conf = 0.344
time : 0.088
Gender : Male, conf = 0.760
Age Output : [[0.2909918  0.5710541  0.07759166 0.00723664 0.04869017 0.00305034
  0.0007095  0.0006757 ]]
Age : (4-6), conf = 0.571
time : 0.101
Gender : Male, conf = 0.760
Age Output : [[0.2909918  0.5710541  0.07759166 0.00723664 0.04869017 0.00305034
  0.0007095  0.0006757 ]]
Age : (4-6), conf = 0.571
time : 0.082
Gender : Male, conf = 0.785
Age Output : [[0.37023968 0.5051328  0.06675136 0.00953131 0.04293477 0.00344136
  0.00094157 0.00102716]]
Age : (4-6), conf = 0.505
time : 0.084
Gender : Male, conf = 0.876
Age Output : [[0.32796207 0.5202417  0.12451164 0.0082208  0.01386692 0.00358863
  0.00071664 0.00089167]]
Age : (4-6), conf = 0.520
time : 0.116
Gender : Male, conf = 0.929
Age Output : [[0.61836904 0.3245218  0.03971447 0.00441672 0.00945476 0.00206821
  0.00068625 0.00076866]]
Age : (0-2), conf = 0.618
time : 0.085
Gender : Male, conf = 0.950
Age Output : [[0.27337098 0.5363163  0.17486006 0.00594596 0.00513775 0.00293197
  0.00055277 0.00088425]]
Age : (4-6), conf = 0.536
time : 0.102
Gender : Male, conf = 0.885
Age Output : [[0.10602655 0.39277655 0.44673058 0.02308462 0.02032574 0.00848556
  0.00105832 0.00151212]]
Age : (8-12), conf = 0.447
time : 0.089
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.861
Age Output : [[0.03114173 0.19643712 0.6404586  0.05009489 0.05514192 0.0227552
  0.00122312 0.0027474 ]]
Age : (8-12), conf = 0.640
time : 0.103
Gender : Male, conf = 0.972
Age Output : [[2.3518777e-02 2.0129603e-01 6.8907052e-01 3.8354099e-02 3.7328571e-02
  8.6630564e-03 3.2589171e-04 1.4431103e-03]]
Age : (8-12), conf = 0.689
time : 0.088
Gender : Female, conf = 0.581
Age Output : [[8.9977339e-02 6.7943877e-01 1.9813628e-01 1.5975233e-02 1.1906544e-02
  3.6506800e-03 2.7751448e-04 6.3762016e-04]]
Age : (4-6), conf = 0.679
time : 0.098
Gender : Male, conf = 0.506
Age Output : [[3.9285410e-02 4.5706689e-01 4.6419689e-01 2.0567389e-02 1.2183904e-02
  5.5376110e-03 2.6684982e-04 8.9500734e-04]]
Age : (8-12), conf = 0.464
time : 0.091
Gender : Female, conf = 0.624
Age Output : [[0.09005079 0.3878928  0.4779357  0.02282105 0.00340754 0.01444991
  0.00077127 0.00267087]]
Age : (8-12), conf = 0.478
time : 0.099
Gender : Female, conf = 0.881
Age Output : [[0.50192916 0.4206903  0.06146411 0.0043809  0.00639205 0.00296786
  0.00077719 0.00139837]]
Age : (0-2), conf = 0.502
time : 0.090
Gender : Female, conf = 0.883
Age Output : [[0.64678633 0.27398437 0.03086808 0.00591129 0.03440325 0.0050148
  0.00162201 0.00140983]]
Age : (0-2), conf = 0.647
time : 0.098
Gender : Male, conf = 0.794
Age Output : [[0.58598745 0.37483662 0.01772487 0.0035418  0.01499022 0.00139548
  0.00074033 0.00078327]]
Age : (0-2), conf = 0.586
time : 0.086
Gender : Male, conf = 0.665
Age Output : [[0.3984883  0.28464276 0.04704789 0.01394998 0.2348352  0.01292335
  0.00440976 0.00370282]]
Age : (0-2), conf = 0.398
time : 0.098
Gender : Male, conf = 0.652
Age Output : [[0.20506565 0.17987847 0.08945519 0.04514629 0.42585796 0.03717751
  0.00927037 0.00814863]]
Age : (25-32), conf = 0.426
time : 0.089
Gender : Male, conf = 0.741
Age Output : [[0.08699969 0.13282692 0.12374052 0.05031396 0.55438507 0.0385517
  0.00673431 0.00644793]]
Age : (25-32), conf = 0.554
time : 0.098
Gender : Male, conf = 0.790
Age Output : [[0.11019804 0.14987898 0.08660211 0.06758115 0.5175723  0.04888558
  0.01075456 0.00852729]]
Age : (25-32), conf = 0.518
time : 0.084
Gender : Male, conf = 0.865
Age Output : [[0.3066231  0.2790504  0.07911936 0.02115265 0.28918275 0.01636622
  0.00461508 0.00389041]]
Age : (0-2), conf = 0.307
time : 0.099
Gender : Male, conf = 0.702
Age Output : [[0.19684425 0.2556802  0.10833973 0.04177957 0.3553605  0.02912189
  0.00684728 0.00602656]]
Age : (25-32), conf = 0.355
time : 0.089
Gender : Male, conf = 0.769
Age Output : [[0.23606548 0.25773132 0.11309862 0.03908548 0.30452567 0.03441778
  0.00837132 0.00670433]]
Age : (25-32), conf = 0.305
time : 0.095
Gender : Male, conf = 0.740
Age Output : [[0.21275376 0.28500217 0.11524278 0.03495144 0.3112184  0.02673414
  0.00833574 0.00576154]]
Age : (25-32), conf = 0.311
time : 0.090
Gender : Male, conf = 0.804
Age Output : [[0.21077792 0.42628336 0.17118032 0.02768012 0.1377393  0.0164042
  0.00552098 0.00441372]]
Age : (4-6), conf = 0.426
time : 0.100
Gender : Male, conf = 0.871
Age Output : [[0.37980127 0.39900133 0.08973294 0.0185433  0.08883274 0.01346756
  0.00601985 0.004601  ]]
Age : (4-6), conf = 0.399
time : 0.088
Gender : Male, conf = 0.910
Age Output : [[0.19896501 0.5108522  0.19500652 0.02236165 0.05806892 0.00863614
  0.00350427 0.00260538]]
Age : (4-6), conf = 0.511
time : 0.099
Gender : Male, conf = 0.910
Age Output : [[0.19896501 0.5108522  0.19500652 0.02236165 0.05806892 0.00863614
  0.00350427 0.00260538]]
Age : (4-6), conf = 0.511
time : 0.096
Gender : Male, conf = 0.858
Age Output : [[0.5367501  0.29706338 0.05018967 0.01310047 0.08326279 0.01107742
  0.00475997 0.00379623]]
Age : (0-2), conf = 0.537
time : 0.093
Gender : Male, conf = 0.891
Age Output : [[0.6215118  0.26350185 0.03099857 0.00696695 0.06564377 0.00572132
  0.00324648 0.00240916]]
Age : (0-2), conf = 0.622
time : 0.076
Gender : Male, conf = 0.830
Age Output : [[0.29727668 0.4432366  0.12382554 0.02393968 0.08903112 0.01336769
  0.00541462 0.00390798]]
Age : (4-6), conf = 0.443
time : 0.100
Gender : Male, conf = 0.820
Age Output : [[0.4843411  0.40963256 0.05395144 0.00738261 0.03663708 0.00419085
  0.00203697 0.00182725]]
Age : (0-2), conf = 0.484
time : 0.089
Gender : Female, conf = 0.557
Age Output : [[0.34334022 0.507732   0.10062402 0.01566662 0.0202106  0.00680553
  0.00248791 0.00313311]]
Age : (4-6), conf = 0.508
time : 0.100
Gender : Female, conf = 0.612
Age Output : [[0.51495147 0.3489295  0.06432113 0.0141142  0.03651832 0.01303288
  0.00374906 0.00438349]]
Age : (0-2), conf = 0.515
time : 0.086
Gender : Male, conf = 0.919
Age Output : [[0.24625419 0.4742858  0.1839606  0.01928258 0.05074426 0.01606661
  0.00469504 0.00471087]]
Age : (4-6), conf = 0.474
time : 0.101
Gender : Male, conf = 0.834
Age Output : [[0.48110127 0.41544607 0.05904259 0.00878045 0.0262414  0.0048098
  0.00248716 0.00209137]]
Age : (0-2), conf = 0.481
time : 0.086
Gender : Male, conf = 0.834
Age Output : [[0.48110127 0.41544607 0.05904259 0.00878045 0.0262414  0.0048098
  0.00248716 0.00209137]]
Age : (0-2), conf = 0.481
time : 0.112
Gender : Male, conf = 0.835
Age Output : [[0.35955465 0.42267367 0.12900782 0.01383183 0.055095   0.01098239
  0.00507933 0.00377532]]
Age : (4-6), conf = 0.423
time : 0.116
Gender : Male, conf = 0.766
Age Output : [[0.6199863  0.23481405 0.04509296 0.01247607 0.06290752 0.01410593
  0.00569346 0.00492379]]
Age : (0-2), conf = 0.620
time : 0.123
Gender : Male, conf = 0.916
Age Output : [[0.530945   0.30822077 0.06302528 0.01414148 0.05969713 0.01428531
  0.00520776 0.00447732]]
Age : (0-2), conf = 0.531
time : 0.124
Gender : Male, conf = 0.737
Age Output : [[0.37578705 0.4055871  0.1305634  0.01956096 0.04731105 0.01244756
  0.00463927 0.00410376]]
Age : (4-6), conf = 0.406
time : 0.124
Gender : Male, conf = 0.595
Age Output : [[0.5084264  0.37421694 0.06323922 0.01097379 0.03051388 0.00680751
  0.0030413  0.00278097]]
Age : (0-2), conf = 0.508
time : 0.123
Gender : Male, conf = 0.818
Age Output : [[0.46132573 0.26360184 0.06507482 0.02213063 0.14270765 0.02721722
  0.01046914 0.00747296]]
Age : (0-2), conf = 0.461
time : 0.122
Gender : Male, conf = 0.808
Age Output : [[0.39803058 0.35036334 0.08755016 0.02112835 0.10228582 0.0245017
  0.00943578 0.00670437]]
Age : (0-2), conf = 0.398
time : 0.116
Gender : Male, conf = 0.660
Age Output : [[0.27135265 0.33890912 0.16161582 0.03108983 0.13316195 0.04138718
  0.01129567 0.01118797]]
Age : (4-6), conf = 0.339
time : 0.125
Gender : Male, conf = 0.926
Age Output : [[0.38745448 0.26040775 0.10229229 0.02912803 0.1531178  0.04465022
  0.01239997 0.01054958]]
Age : (0-2), conf = 0.387
time : 0.116
Gender : Male, conf = 0.917
Age Output : [[0.29745257 0.3809269  0.12705873 0.02685546 0.12422014 0.02794511
  0.00864804 0.00689301]]
Age : (4-6), conf = 0.381
time : 0.135
Gender : Male, conf = 0.863
Age Output : [[0.4835535  0.27028736 0.0592758  0.01966118 0.12968262 0.02316489
  0.00780219 0.00657231]]
Age : (0-2), conf = 0.484
time : 0.113
Gender : Male, conf = 0.742
Age Output : [[0.36929208 0.23019148 0.10495196 0.03225575 0.17812137 0.0549203
  0.01607484 0.01419217]]
Age : (0-2), conf = 0.369
time : 0.125
Gender : Female, conf = 0.726
Age Output : [[0.43264905 0.38834953 0.09417718 0.01479288 0.03368634 0.01857641
  0.00830021 0.00946845]]
Age : (0-2), conf = 0.433
time : 0.123
Gender : Male, conf = 0.550
Age Output : [[0.43587318 0.34559163 0.09616937 0.01321504 0.08487061 0.01335644
  0.00602281 0.00490083]]
Age : (0-2), conf = 0.436
time : 0.126
Gender : Male, conf = 0.937
Age Output : [[0.46083844 0.33452758 0.0673774  0.01676923 0.09115691 0.01708992
  0.00675068 0.00548993]]
Age : (0-2), conf = 0.461
time : 0.116
Gender : Male, conf = 0.848
Age Output : [[0.3769264  0.46445447 0.08783793 0.00986224 0.04644226 0.0076406
  0.0034089  0.00342722]]
Age : (4-6), conf = 0.464
time : 0.120
Gender : Male, conf = 0.829
Age Output : [[0.45061165 0.31163248 0.11100216 0.02293374 0.06770287 0.02252922
  0.00649473 0.00709318]]
Age : (0-2), conf = 0.451
time : 0.118
Gender : Male, conf = 0.622
Age Output : [[0.43852377 0.33422148 0.10767339 0.02090024 0.05943587 0.02371573
  0.00690024 0.00862939]]
Age : (0-2), conf = 0.439
time : 0.104
Gender : Male, conf = 0.767
Age Output : [[0.4097634  0.35958874 0.12185793 0.01544819 0.06135161 0.01663596
  0.00770545 0.00764888]]
Age : (0-2), conf = 0.410
time : 0.112
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.803
Age Output : [[0.31210813 0.42841744 0.11482003 0.01862618 0.09952012 0.01696772
  0.00505244 0.00448781]]
Age : (4-6), conf = 0.428
time : 0.108
Gender : Male, conf = 0.639
Age Output : [[0.28503332 0.29569218 0.10462382 0.02880828 0.23442703 0.0332875
  0.01027769 0.00785018]]
Age : (4-6), conf = 0.296
time : 0.103
Gender : Male, conf = 0.535
Age Output : [[0.28224844 0.11997627 0.05149889 0.04388616 0.37630606 0.09114987
  0.02044893 0.01448533]]
Age : (25-32), conf = 0.376
time : 0.095
Gender : Male, conf = 0.673
Age Output : [[0.33580992 0.33784914 0.15444167 0.04355114 0.075188   0.03535466
  0.00851226 0.00929335]]
Age : (4-6), conf = 0.338
time : 0.081
Gender : Male, conf = 0.723
Age Output : [[0.2901531  0.3797995  0.14022224 0.0281091  0.12106603 0.02669652
  0.00734695 0.00660653]]
Age : (4-6), conf = 0.380
time : 0.100
Gender : Female, conf = 0.512
Age Output : [[0.44688305 0.22286092 0.1098524  0.02670659 0.10748044 0.0526224
  0.01688378 0.01671045]]
Age : (0-2), conf = 0.447
time : 0.104
Gender : Male, conf = 0.563
Age Output : [[0.19822176 0.4707439  0.25890985 0.02104562 0.0295784  0.01354763
  0.00342631 0.00452656]]
Age : (4-6), conf = 0.471
time : 0.122
Gender : Male, conf = 0.791
Age Output : [[0.21133018 0.16613394 0.07332041 0.04145287 0.4113611  0.06857833
  0.0149069  0.01291623]]
Age : (25-32), conf = 0.411
time : 0.116
Gender : Male, conf = 0.743
Age Output : [[0.22376838 0.23598889 0.11494718 0.04799215 0.28372318 0.06686182
  0.0136456  0.01307287]]
Age : (25-32), conf = 0.284
time : 0.133
Gender : Male, conf = 0.649
Age Output : [[0.36593968 0.20708719 0.08149175 0.04039199 0.22460619 0.05473927
  0.01267997 0.01306396]]
Age : (0-2), conf = 0.366
time : 0.121
Gender : Male, conf = 0.653
Age Output : [[0.50941736 0.2667457  0.0829221  0.01867215 0.07460413 0.02835858
  0.00987752 0.00940235]]
Age : (0-2), conf = 0.509
time : 0.101
Gender : Male, conf = 0.710
Age Output : [[0.16465937 0.11859072 0.08561239 0.05389427 0.43407664 0.09856405
  0.02789176 0.01671075]]
Age : (25-32), conf = 0.434
time : 0.084
Gender : Male, conf = 0.897
Age Output : [[0.3111772  0.23519689 0.10119997 0.03282568 0.250025   0.04712472
  0.0117853  0.01066521]]
Age : (0-2), conf = 0.311
time : 0.098
Gender : Male, conf = 0.897
Age Output : [[0.3111772  0.23519689 0.10119997 0.03282568 0.250025   0.04712472
  0.0117853  0.01066521]]
Age : (0-2), conf = 0.311
time : 0.088
Gender : Male, conf = 0.858
Age Output : [[0.2516879  0.27693278 0.16118044 0.04814975 0.19994693 0.04402566
  0.00960059 0.00847593]]
Age : (4-6), conf = 0.277
time : 0.103
Gender : Male, conf = 0.884
Age Output : [[0.31786856 0.31027907 0.15699875 0.03103404 0.14008778 0.02989932
  0.00691151 0.00692098]]
Age : (0-2), conf = 0.318
time : 0.087
Gender : Male, conf = 0.924
Age Output : [[0.24291407 0.20718063 0.12039477 0.04675421 0.28839746 0.06461351
  0.01755662 0.01218874]]
Age : (25-32), conf = 0.288
time : 0.101
Gender : Male, conf = 0.827
Age Output : [[0.21441907 0.15855663 0.11388531 0.0574422  0.3369001  0.08517603
  0.018131   0.01548966]]
Age : (25-32), conf = 0.337
time : 0.087
Gender : Male, conf = 0.739
Age Output : [[0.20514813 0.11966167 0.07147908 0.06210136 0.3968305  0.10743113
  0.01932654 0.01802168]]
Age : (25-32), conf = 0.397
time : 0.103
Gender : Male, conf = 0.847
Age Output : [[0.33143422 0.30025253 0.13014032 0.04002808 0.1424295  0.03696853
  0.00895404 0.00979287]]
Age : (0-2), conf = 0.331
time : 0.087
Gender : Male, conf = 0.705
Age Output : [[0.21581618 0.1368111  0.09876013 0.05036675 0.30856425 0.14052677
  0.0264759  0.02267892]]
Age : (25-32), conf = 0.309
time : 0.098
Gender : Male, conf = 0.705
Age Output : [[0.21581618 0.1368111  0.09876013 0.05036675 0.30856425 0.14052677
  0.0264759  0.02267892]]
Age : (25-32), conf = 0.309
time : 0.091
Gender : Male, conf = 0.894
Age Output : [[0.35737053 0.33373713 0.1329357  0.03060437 0.09940773 0.03021172
  0.00759377 0.00813902]]
Age : (0-2), conf = 0.357
time : 0.099
Gender : Male, conf = 0.836
Age Output : [[0.15784098 0.43349892 0.2716362  0.03550024 0.07873172 0.01593853
  0.00323638 0.00361712]]
Age : (4-6), conf = 0.433
time : 0.090
Gender : Male, conf = 0.559
Age Output : [[0.35353053 0.29627168 0.14409417 0.03052212 0.10682153 0.04661643
  0.00973588 0.01240765]]
Age : (0-2), conf = 0.354
time : 0.099
Gender : Male, conf = 0.669
Age Output : [[0.26158303 0.3030312  0.20795621 0.03470771 0.11586126 0.04992478
  0.01331852 0.01361725]]
Age : (4-6), conf = 0.303
time : 0.086
Gender : Male, conf = 0.894
Age Output : [[0.33348948 0.25057507 0.10071997 0.03226321 0.21190694 0.04648892
  0.01317405 0.01138238]]
Age : (0-2), conf = 0.333
time : 0.101
Gender : Male, conf = 0.515
Age Output : [[0.42378566 0.2813684  0.10446253 0.02848151 0.11154915 0.03274476
  0.00845982 0.00914823]]
Age : (0-2), conf = 0.424
time : 0.082
Gender : Male, conf = 0.879
Age Output : [[0.17253917 0.11309722 0.10150482 0.05368087 0.4184839  0.11049237
  0.01698069 0.01322092]]
Age : (25-32), conf = 0.418
time : 0.105
Gender : Male, conf = 0.615
Age Output : [[0.44747052 0.222608   0.07928732 0.03663778 0.15215209 0.04258915
  0.00953455 0.00972052]]
Age : (0-2), conf = 0.447
time : 0.082
Gender : Male, conf = 0.615
Age Output : [[0.44747052 0.222608   0.07928732 0.03663778 0.15215209 0.04258915
  0.00953455 0.00972052]]
Age : (0-2), conf = 0.447
time : 0.086
Gender : Male, conf = 0.791
Age Output : [[0.25326273 0.24430509 0.18336368 0.05970987 0.18538615 0.05258086
  0.01064618 0.01074546]]
Age : (0-2), conf = 0.253
time : 0.083
Gender : Male, conf = 0.583
Age Output : [[0.30158398 0.22046246 0.17438556 0.04613636 0.1631854  0.06866097
  0.01302861 0.01255664]]
Age : (0-2), conf = 0.302
time : 0.101
Gender : Male, conf = 0.859
Age Output : [[0.17424414 0.11414709 0.08776078 0.05330827 0.40548375 0.12632778
  0.02199201 0.01673626]]
Age : (25-32), conf = 0.405
time : 0.082
Gender : Female, conf = 0.630
Age Output : [[0.33515477 0.33894753 0.20261796 0.0293316  0.04820497 0.02998827
  0.00756311 0.00819169]]
Age : (4-6), conf = 0.339
time : 0.101
Gender : Male, conf = 0.571
Age Output : [[0.39601055 0.3379869  0.11910854 0.03106906 0.07275292 0.0268501
  0.00759847 0.00862348]]
Age : (0-2), conf = 0.396
time : 0.081
Gender : Male, conf = 0.571
Age Output : [[0.39601055 0.3379869  0.11910854 0.03106906 0.07275292 0.0268501
  0.00759847 0.00862348]]
Age : (0-2), conf = 0.396
time : 0.084
Gender : Male, conf = 0.580
Age Output : [[0.28630304 0.24980105 0.15475968 0.03752783 0.20129758 0.04824995
  0.01133612 0.01072478]]
Age : (0-2), conf = 0.286
time : 0.088
Gender : Male, conf = 0.724
Age Output : [[0.00933277 0.00925389 0.0281021  0.02472259 0.8327979  0.0813192
  0.00851179 0.00595978]]
Age : (25-32), conf = 0.833
time : 0.102
Gender : Male, conf = 0.921
Age Output : [[0.05514744 0.22073534 0.4696475  0.04273427 0.14096987 0.05524385
  0.00601411 0.00950764]]
Age : (8-12), conf = 0.470
time : 0.081
Gender : Male, conf = 0.992
Age Output : [[0.00685478 0.09566925 0.78131425 0.05006292 0.0456168  0.01531345
  0.00105079 0.00411785]]
Age : (8-12), conf = 0.781
time : 0.085
Gender : Male, conf = 0.809
Age Output : [[0.02315736 0.19408886 0.576      0.08194923 0.07576514 0.03712577
  0.00322819 0.00868548]]
Age : (8-12), conf = 0.576
time : 0.088
Gender : Male, conf = 0.809
Age Output : [[0.02315736 0.19408886 0.576      0.08194923 0.07576514 0.03712577
  0.00322819 0.00868548]]
Age : (8-12), conf = 0.576
time : 0.084
Gender : Male, conf = 0.599
Age Output : [[0.15374164 0.4612141  0.36181292 0.00793614 0.00690174 0.00415725
  0.00105283 0.0031833 ]]
Age : (4-6), conf = 0.461
time : 0.087
Gender : Male, conf = 0.508
Age Output : [[0.6203306  0.31866112 0.0279566  0.00540143 0.02136384 0.00282842
  0.00167749 0.00178055]]
Age : (0-2), conf = 0.620
time : 0.101
Gender : Female, conf = 0.690
Age Output : [[7.3710811e-01 2.2253759e-01 1.6304726e-02 4.0808148e-03 1.6962806e-02
  1.5432717e-03 6.7968323e-04 7.8302040e-04]]
Age : (0-2), conf = 0.737
time : 0.079
Gender : Male, conf = 0.876
Age Output : [[0.4091649  0.4506098  0.08316563 0.01227506 0.03597609 0.00520416
  0.00166555 0.00193871]]
Age : (4-6), conf = 0.451
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>time : 0.085
Gender : Female, conf = 0.655
Age Output : [[5.4147011e-01 4.3542966e-01 1.3387667e-02 1.5739867e-03 6.4444644e-03
  6.5288635e-04 4.6748066e-04 5.7372026e-04]]
Age : (0-2), conf = 0.541
time : 0.085
Gender : Male, conf = 0.587
Age Output : [[0.507709   0.44780228 0.02565912 0.00241899 0.01389577 0.00115491
  0.00062269 0.00073723]]
Age : (0-2), conf = 0.508
time : 0.097
Gender : Male, conf = 0.587
Age Output : [[0.507709   0.44780228 0.02565912 0.00241899 0.01389577 0.00115491
  0.00062269 0.00073723]]
Age : (0-2), conf = 0.508
time : 0.090
Gender : Male, conf = 0.634
Age Output : [[0.57061756 0.3700098  0.025421   0.00454003 0.02418119 0.00254321
  0.00135673 0.0013304 ]]
Age : (0-2), conf = 0.571
time : 0.099
Gender : Female, conf = 0.608
Age Output : [[0.4778725  0.47458082 0.03009927 0.00497485 0.00923697 0.00141624
  0.00075297 0.00106648]]
Age : (0-2), conf = 0.478
time : 0.088
Gender : Female, conf = 0.697
Age Output : [[0.723258   0.24081832 0.01749474 0.00188329 0.01170929 0.00234574
  0.00122115 0.00126952]]
Age : (0-2), conf = 0.723
time : 0.104
Gender : Male, conf = 0.543
Age Output : [[0.6020558  0.3614996  0.01626742 0.0023357  0.01439099 0.00154754
  0.00099164 0.00091133]]
Age : (0-2), conf = 0.602
time : 0.087
Gender : Female, conf = 0.644
Age Output : [[7.1344686e-01 2.6737240e-01 9.3541779e-03 1.8132617e-03 6.1918269e-03
  7.7549485e-04 4.8439504e-04 5.6166510e-04]]
Age : (0-2), conf = 0.713
time : 0.100
Gender : Female, conf = 0.605
Age Output : [[0.7129105  0.26475167 0.011671   0.00179778 0.00639537 0.00096883
  0.00072198 0.00078294]]
Age : (0-2), conf = 0.713
time : 0.081
Gender : Male, conf = 0.527
Age Output : [[0.60049397 0.360259   0.02056147 0.00397035 0.01110562 0.00149757
  0.00089422 0.00121781]]
Age : (0-2), conf = 0.600
time : 0.091
Gender : Male, conf = 0.717
Age Output : [[8.2290024e-01 1.6095939e-01 5.9126746e-03 1.3393291e-03 6.6526635e-03
  9.4218290e-04 6.8895193e-04 6.0443615e-04]]
Age : (0-2), conf = 0.823
time : 0.088
Gender : Female, conf = 0.621
Age Output : [[0.71654516 0.23134218 0.02052522 0.0042165  0.01975978 0.00388114
  0.00192636 0.00180366]]
Age : (0-2), conf = 0.717
time : 0.090
Gender : Female, conf = 0.775
Age Output : [[0.73959976 0.23306134 0.00951993 0.00201017 0.01304617 0.00119838
  0.00079911 0.00076503]]
Age : (0-2), conf = 0.740
time : 0.086
Gender : Male, conf = 0.645
Age Output : [[0.75543076 0.21301684 0.01123853 0.00274911 0.01352288 0.00177234
  0.00112916 0.00114031]]
Age : (0-2), conf = 0.755
time : 0.090
Gender : Female, conf = 0.731
Age Output : [[0.642905   0.3228168  0.01563504 0.00326804 0.01217645 0.00132109
  0.00091665 0.00096092]]
Age : (0-2), conf = 0.643
time : 0.086
Gender : Female, conf = 0.756
Age Output : [[0.69484043 0.27046546 0.01589073 0.00238565 0.01082787 0.00262288
  0.00147674 0.00149033]]
Age : (0-2), conf = 0.695
time : 0.107
Gender : Male, conf = 0.599
Age Output : [[0.63854617 0.3271708  0.01908558 0.00347672 0.00774329 0.00165831
  0.00104988 0.00126931]]
Age : (0-2), conf = 0.639
time : 0.081
Gender : Female, conf = 0.749
Age Output : [[0.55875224 0.40043512 0.02801672 0.00330693 0.00487566 0.00219646
  0.00096677 0.00145004]]
Age : (0-2), conf = 0.559
time : 0.101
Gender : Female, conf = 0.941
Age Output : [[0.5609163  0.16844973 0.05616204 0.02478244 0.09115399 0.0813931
  0.00844087 0.0087015 ]]
Age : (0-2), conf = 0.561
time : 0.089
Gender : Female, conf = 0.991
Age Output : [[0.68355906 0.13270393 0.02770337 0.01634209 0.07157139 0.04961105
  0.00980231 0.00870672]]
Age : (0-2), conf = 0.684
time : 0.093
Gender : Female, conf = 0.983
Age Output : [[0.5551463  0.1478854  0.0147129  0.01153716 0.22190063 0.02679042
  0.0148633  0.00716388]]
Age : (0-2), conf = 0.555
time : 0.091
Gender : Female, conf = 0.976
Age Output : [[0.07921792 0.10910165 0.02037849 0.01907857 0.7203803  0.03859486
  0.00792021 0.00532812]]
Age : (25-32), conf = 0.720
time : 0.100
Gender : Male, conf = 0.640
Age Output : [[0.00281686 0.00823663 0.00280558 0.01124957 0.96050316 0.01142247
  0.00151616 0.0014496 ]]
Age : (25-32), conf = 0.961
time : 0.100
Gender : Male, conf = 0.969
Age Output : [[0.08694334 0.24449453 0.01964331 0.01177324 0.6245407  0.00664595
  0.00363265 0.00232629]]
Age : (25-32), conf = 0.625
time : 0.100
Gender : Female, conf = 0.600
Age Output : [[0.45134524 0.4070225  0.023096   0.01623172 0.0881616  0.00814177
  0.00343022 0.00257089]]
Age : (0-2), conf = 0.451
time : 0.091
Gender : Female, conf = 0.668
Age Output : [[0.56315035 0.37006778 0.01386362 0.00795759 0.04057032 0.0024445
  0.00095166 0.0009941 ]]
Age : (0-2), conf = 0.563
time : 0.098
Gender : Male, conf = 0.771
Age Output : [[7.2373056e-01 2.3604088e-01 8.6385952e-03 2.3525327e-03 2.6325736e-02
  1.4467067e-03 8.2841847e-04 6.3661957e-04]]
Age : (0-2), conf = 0.724
time : 0.090
Gender : Male, conf = 0.881
Age Output : [[0.62012285 0.31506294 0.02204079 0.00402022 0.03225094 0.00320247
  0.00179309 0.00150666]]
Age : (0-2), conf = 0.620
time : 0.099
Gender : Female, conf = 0.636
Age Output : [[7.7914971e-01 2.0860001e-01 8.7497663e-03 5.2115793e-04 1.8691604e-03
  4.5524765e-04 2.8930861e-04 3.6570441e-04]]
Age : (0-2), conf = 0.779
time : 0.089
Gender : Female, conf = 0.636
Age Output : [[7.7914971e-01 2.0860001e-01 8.7497663e-03 5.2115793e-04 1.8691604e-03
  4.5524765e-04 2.8930861e-04 3.6570441e-04]]
Age : (0-2), conf = 0.779
time : 0.102
Gender : Male, conf = 0.929
Age Output : [[9.1682160e-01 7.8208938e-02 2.9686044e-03 3.2647536e-04 1.0261682e-03
  2.4681858e-04 1.9109530e-04 2.1041864e-04]]
Age : (0-2), conf = 0.917
time : 0.091
Gender : Male, conf = 0.821
Age Output : [[8.2989788e-01 1.6047342e-01 6.5879216e-03 5.4448383e-04 1.6185179e-03
  3.4173837e-04 2.4925030e-04 2.8675684e-04]]
Age : (0-2), conf = 0.830
time : 0.097
Gender : Male, conf = 0.907
Age Output : [[7.5199938e-01 2.3334478e-01 1.1763164e-02 6.8125362e-04 1.3193587e-03
  3.9390955e-04 2.2845085e-04 2.6974935e-04]]
Age : (0-2), conf = 0.752
time : 0.090
Gender : Male, conf = 0.645
Age Output : [[8.3862793e-01 1.5235931e-01 6.8986700e-03 4.0319641e-04 8.9794613e-04
  2.9667022e-04 2.2928108e-04 2.8702233e-04]]
Age : (0-2), conf = 0.839
time : 0.102
Gender : Male, conf = 0.600
Age Output : [[8.8059169e-01 1.1243586e-01 4.2085564e-03 4.9087731e-04 1.5074055e-03
  3.0727033e-04 2.0024813e-04 2.5802889e-04]]
Age : (0-2), conf = 0.881
time : 0.094
Gender : Male, conf = 0.507
Age Output : [[7.8786021e-01 1.9711439e-01 9.0586394e-03 6.8713923e-04 4.0615834e-03
  4.9739319e-04 3.4659778e-04 3.7404621e-04]]
Age : (0-2), conf = 0.788
time : 0.101
Gender : Female, conf = 0.754
Age Output : [[7.8416008e-01 1.9555485e-01 1.6060686e-02 8.5457513e-04 1.7308001e-03
  6.1015197e-04 3.3818043e-04 6.9070078e-04]]
Age : (0-2), conf = 0.784
time : 0.092
Gender : Male, conf = 0.602
Age Output : [[0.31442043 0.42044574 0.21913946 0.01580394 0.01468297 0.00792263
  0.00205039 0.00553446]]
Age : (4-6), conf = 0.420
time : 0.102
Gender : Male, conf = 0.868
Age Output : [[0.10450321 0.19059667 0.6329424  0.04635417 0.00566293 0.01040808
  0.00095754 0.00857507]]
Age : (8-12), conf = 0.633
time : 0.090
Gender : Male, conf = 0.868
Age Output : [[0.10450321 0.19059667 0.6329424  0.04635417 0.00566293 0.01040808
  0.00095754 0.00857507]]
Age : (8-12), conf = 0.633
time : 0.101
Gender : Male, conf = 0.893
Age Output : [[0.25289714 0.26215094 0.35726476 0.06697397 0.0203598  0.01337036
  0.00343825 0.02354478]]
Age : (8-12), conf = 0.357
time : 0.077
Gender : Male, conf = 0.924
Age Output : [[0.7454875  0.21051458 0.01965583 0.00319536 0.01066096 0.00451875
  0.00218834 0.0037787 ]]
Age : (0-2), conf = 0.745
time : 0.101
Gender : Male, conf = 0.903
Age Output : [[0.8575445  0.11984639 0.00982989 0.00177727 0.00522323 0.00230031
  0.00151489 0.00196363]]
Age : (0-2), conf = 0.858
time : 0.078
Gender : Male, conf = 0.872
Age Output : [[0.7590378  0.21540014 0.01425297 0.00167082 0.00504835 0.00175485
  0.00120108 0.00163397]]
Age : (0-2), conf = 0.759
time : 0.091
Gender : Male, conf = 0.682
Age Output : [[8.1428701e-01 1.6982032e-01 9.3329139e-03 1.2136926e-03 3.0058478e-03
  9.0737193e-04 6.3951913e-04 7.9325627e-04]]
Age : (0-2), conf = 0.814
time : 0.094
Gender : Male, conf = 0.689
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Age Output : [[7.9669923e-01 1.8381459e-01 1.0730358e-02 1.7235054e-03 3.8537395e-03
  1.2051106e-03 7.1862154e-04 1.2547848e-03]]
Age : (0-2), conf = 0.797
time : 0.101
Gender : Male, conf = 0.773
Age Output : [[9.2216361e-01 6.8993881e-02 3.4563774e-03 7.7471172e-04 2.9878339e-03
  6.4007589e-04 3.9748906e-04 5.8599631e-04]]
Age : (0-2), conf = 0.922
time : 0.084
Gender : Male, conf = 0.913
Age Output : [[9.1439676e-01 7.4753284e-02 3.6319469e-03 9.3314226e-04 4.0989853e-03
  8.0507773e-04 5.7959137e-04 8.0117997e-04]]
Age : (0-2), conf = 0.914
time : 0.085
Gender : Male, conf = 0.913
Age Output : [[9.1439676e-01 7.4753284e-02 3.6319469e-03 9.3314226e-04 4.0989853e-03
  8.0507773e-04 5.7959137e-04 8.0117997e-04]]
Age : (0-2), conf = 0.914
time : 0.091
Gender : Male, conf = 0.850
Age Output : [[0.90912795 0.06817231 0.00632306 0.00233365 0.00727071 0.00276089
  0.00167662 0.00233481]]
Age : (0-2), conf = 0.909
time : 0.098
Gender : Male, conf = 0.923
Age Output : [[9.0996569e-01 8.0429167e-02 3.6848672e-03 8.1385794e-04 3.0053833e-03
  7.4409385e-04 5.4280279e-04 8.1406214e-04]]
Age : (0-2), conf = 0.910
time : 0.082
Gender : Female, conf = 0.708
Age Output : [[8.7029767e-01 1.1710975e-01 6.8527921e-03 7.9238025e-04 2.5867387e-03
  7.8914990e-04 5.3410284e-04 1.0373833e-03]]
Age : (0-2), conf = 0.870
time : 0.101
Gender : Male, conf = 0.989
Age Output : [[8.6122113e-01 1.2712483e-01 4.9096155e-03 8.1765017e-04 3.9257221e-03
  6.2203401e-04 4.9988221e-04 8.7919808e-04]]
Age : (0-2), conf = 0.861
time : 0.091
Gender : Male, conf = 0.966
Age Output : [[9.1229093e-01 7.5874537e-02 3.8480519e-03 8.6397643e-04 4.5660357e-03
  9.1794564e-04 6.4200471e-04 9.9657255e-04]]
Age : (0-2), conf = 0.912
time : 0.105
Gender : Male, conf = 0.876
Age Output : [[8.76090646e-01 1.08853444e-01 5.33145573e-03 1.08229963e-03
  5.32873627e-03 9.99665586e-04 8.07573204e-04 1.50605780e-03]]
Age : (0-2), conf = 0.876
time : 0.082
Gender : Male, conf = 0.876
Age Output : [[8.76090646e-01 1.08853444e-01 5.33145573e-03 1.08229963e-03
  5.32873627e-03 9.99665586e-04 8.07573204e-04 1.50605780e-03]]
Age : (0-2), conf = 0.876
time : 0.101
Gender : Male, conf = 0.960
Age Output : [[9.3190610e-01 6.0561370e-02 2.6148106e-03 5.5269583e-04 2.5901378e-03
  5.3117267e-04 4.0911487e-04 8.3458552e-04]]
Age : (0-2), conf = 0.932
time : 0.085
Gender : Male, conf = 0.905
Age Output : [[0.8886716  0.09185603 0.00742999 0.00204264 0.00551099 0.00152189
  0.00099697 0.00196987]]
Age : (0-2), conf = 0.889
time : 0.100
Gender : Male, conf = 0.971
Age Output : [[9.2056739e-01 6.7731224e-02 5.4088761e-03 1.3484535e-03 2.1528145e-03
  9.3356759e-04 5.1807769e-04 1.3396483e-03]]
Age : (0-2), conf = 0.921
time : 0.088
Gender : Male, conf = 0.829
Age Output : [[9.6280378e-01 3.1750731e-02 2.1069825e-03 4.7366999e-04 1.1879129e-03
  5.6705123e-04 3.2515242e-04 7.8471401e-04]]
Age : (0-2), conf = 0.963
time : 0.101
Gender : Male, conf = 0.957
Age Output : [[0.9105154  0.07036098 0.00767686 0.00197114 0.00375503 0.00215202
  0.00103733 0.00253119]]
Age : (0-2), conf = 0.911
time : 0.087
Gender : Male, conf = 0.984
Age Output : [[0.9043927  0.07413678 0.0077952  0.0026265  0.00547714 0.00204637
  0.00110546 0.00241962]]
Age : (0-2), conf = 0.904
time : 0.084
Gender : Male, conf = 0.969
Age Output : [[9.1011822e-01 7.5397618e-02 5.4922998e-03 1.3191868e-03 4.9927672e-03
  9.5924002e-04 6.4718153e-04 1.0734331e-03]]
Age : (0-2), conf = 0.910
time : 0.088
Gender : Male, conf = 0.969
Age Output : [[9.1011822e-01 7.5397618e-02 5.4922998e-03 1.3191868e-03 4.9927672e-03
  9.5924002e-04 6.4718153e-04 1.0734331e-03]]
Age : (0-2), conf = 0.910
time : 0.102
Gender : Male, conf = 0.961
Age Output : [[9.1171247e-01 7.5258106e-02 5.0281705e-03 1.2680182e-03 4.0289564e-03
  9.4091747e-04 6.3007633e-04 1.1333278e-03]]
Age : (0-2), conf = 0.912
time : 0.081
Gender : Male, conf = 0.944
Age Output : [[9.2776436e-01 6.0109969e-02 4.7892174e-03 1.2062204e-03 3.3802018e-03
  1.0368744e-03 5.9691345e-04 1.1163137e-03]]
Age : (0-2), conf = 0.928
time : 0.084
Gender : Male, conf = 0.941
Age Output : [[9.2071909e-01 6.3807875e-02 5.9061768e-03 1.4499441e-03 3.8844077e-03
  1.5068536e-03 8.6030795e-04 1.8653612e-03]]
Age : (0-2), conf = 0.921
time : 0.090
Gender : Male, conf = 0.653
Age Output : [[9.3673980e-01 5.6681842e-02 3.9793518e-03 3.8910218e-04 8.7715307e-04
  4.0657146e-04 2.6238113e-04 6.6376763e-04]]
Age : (0-2), conf = 0.937
time : 0.099
Gender : Male, conf = 0.600
Age Output : [[0.8978427  0.07891118 0.0111049  0.00187279 0.00481026 0.00194947
  0.00105339 0.00245522]]
Age : (0-2), conf = 0.898
time : 0.082
Gender : Male, conf = 0.930
Age Output : [[9.0691990e-01 7.2532922e-02 1.0101297e-02 1.6805978e-03 4.3538297e-03
  1.5501562e-03 8.9480152e-04 1.9663407e-03]]
Age : (0-2), conf = 0.907
time : 0.099
Gender : Male, conf = 0.930
Age Output : [[9.0691990e-01 7.2532922e-02 1.0101297e-02 1.6805978e-03 4.3538297e-03
  1.5501562e-03 8.9480152e-04 1.9663407e-03]]
Age : (0-2), conf = 0.907
time : 0.091
Gender : Male, conf = 0.720
Age Output : [[0.9120182  0.06805395 0.00809276 0.00166082 0.00524967 0.00177097
  0.00106127 0.00209244]]
Age : (0-2), conf = 0.912
time : 0.088
Gender : Male, conf = 0.848
Age Output : [[0.9156337  0.06686233 0.00771574 0.00113989 0.00302424 0.00148581
  0.00096501 0.00317343]]
Age : (0-2), conf = 0.916
time : 0.081
Gender : Male, conf = 0.752
Age Output : [[9.4215924e-01 4.5365110e-02 6.8168929e-03 9.1834425e-04 1.3641388e-03
  1.1495820e-03 4.6831043e-04 1.7582447e-03]]
Age : (0-2), conf = 0.942
time : 0.104
Gender : Male, conf = 0.953
Age Output : [[0.9339028  0.04198287 0.00747622 0.00197946 0.00518266 0.00339631
  0.00171779 0.00436191]]
Age : (0-2), conf = 0.934
time : 0.080
Gender : Male, conf = 0.799
Age Output : [[0.9257534  0.05103606 0.00717299 0.00157598 0.00710365 0.00293639
  0.00183635 0.00258509]]
Age : (0-2), conf = 0.926
time : 0.115
Gender : Male, conf = 0.827
Age Output : [[9.5511913e-01 3.5537675e-02 3.0143699e-03 6.9463206e-04 3.4807301e-03
  9.4571034e-04 5.1339524e-04 6.9421850e-04]]
Age : (0-2), conf = 0.955
time : 0.121
Gender : Female, conf = 0.682
Age Output : [[9.3334270e-01 5.9426982e-02 2.2965188e-03 3.9655578e-04 3.5563903e-03
  4.1086640e-04 2.5605006e-04 3.1393746e-04]]
Age : (0-2), conf = 0.933
time : 0.119
Gender : Male, conf = 0.727
Age Output : [[8.9926296e-01 7.8814581e-02 5.7437127e-03 1.4273934e-03 1.1978073e-02
  1.2206145e-03 7.4167538e-04 8.1109290e-04]]
Age : (0-2), conf = 0.899
time : 0.112
Gender : Male, conf = 0.732
Age Output : [[8.8889730e-01 9.1210067e-02 6.8683475e-03 1.0418200e-03 9.5576849e-03
  1.0775314e-03 6.5401971e-04 6.9319375e-04]]
Age : (0-2), conf = 0.889
time : 0.122
Gender : Male, conf = 0.850
Age Output : [[0.8126282  0.14972472 0.01189869 0.00144757 0.02030513 0.00172918
  0.00122659 0.00103996]]
Age : (0-2), conf = 0.813
time : 0.116
Gender : Female, conf = 0.875
Age Output : [[8.8886184e-01 8.4171265e-02 7.3939483e-03 1.3913555e-03 1.5012329e-02
  1.4066331e-03 8.7147224e-04 8.9121592e-04]]
Age : (0-2), conf = 0.889
time : 0.126
Gender : Female, conf = 0.618
Age Output : [[9.3571568e-01 5.0089393e-02 3.4513944e-03 9.9009846e-04 7.6728086e-03
  9.2966447e-04 5.2647531e-04 6.2450924e-04]]
Age : (0-2), conf = 0.936
time : 0.121
Gender : Female, conf = 0.714
Age Output : [[9.6616137e-01 2.9047113e-02 1.6856524e-03 3.1913305e-04 1.9025207e-03
  4.1079102e-04 1.9264720e-04 2.8072030e-04]]
Age : (0-2), conf = 0.966
time : 0.142
Gender : Female, conf = 0.723
Age Output : [[9.4656718e-01 4.8323076e-02 2.4056432e-03 4.1560529e-04 1.3773424e-03
  3.6121107e-04 1.9490930e-04 3.5509118e-04]]
Age : (0-2), conf = 0.947
time : 0.123
Gender : Male, conf = 0.590
Age Output : [[9.0359527e-01 8.4617339e-02 5.5291061e-03 9.2028850e-04 3.2399886e-03
  9.5491926e-04 5.1111513e-04 6.3184003e-04]]
Age : (0-2), conf = 0.904
time : 0.117
Gender : Female, conf = 0.766
Age Output : [[0.84251404 0.13143462 0.01451516 0.00224815 0.00399283 0.00283277
  0.00097174 0.00149078]]
Age : (0-2), conf = 0.843
time : 0.124
Gender : Female, conf = 0.784
Age Output : [[8.82315576e-01 1.02425426e-01 8.45691469e-03 1.13906094e-03
  2.49217520e-03 1.46366365e-03 6.12594013e-04 1.09458307e-03]]
Age : (0-2), conf = 0.882
time : 0.113
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.504
Age Output : [[8.9663774e-01 9.5226392e-02 4.6183621e-03 5.2760192e-04 1.6330916e-03
  5.8926217e-04 3.3842691e-04 4.2907379e-04]]
Age : (0-2), conf = 0.897
time : 0.123
Gender : Female, conf = 0.818
Age Output : [[8.6803144e-01 1.1753655e-01 8.1259487e-03 8.8228245e-04 3.1203551e-03
  1.0110461e-03 5.6736171e-04 7.2500622e-04]]
Age : (0-2), conf = 0.868
time : 0.110
Gender : Male, conf = 0.834
Age Output : [[9.0361017e-01 8.0618560e-02 7.2707580e-03 1.4012108e-03 3.7912061e-03
  1.6111970e-03 6.9310638e-04 1.0039307e-03]]
Age : (0-2), conf = 0.904
time : 0.121
Gender : Female, conf = 0.952
Age Output : [[8.7485343e-01 1.0372472e-01 1.3278463e-02 1.3325579e-03 2.5854490e-03
  2.0432435e-03 8.6058548e-04 1.3214535e-03]]
Age : (0-2), conf = 0.875
time : 0.110
Gender : Male, conf = 0.716
Age Output : [[8.9133209e-01 9.9451654e-02 5.0671361e-03 5.8361463e-04 1.9763403e-03
  6.8647839e-04 3.7277967e-04 5.2989851e-04]]
Age : (0-2), conf = 0.891
time : 0.122
Gender : Male, conf = 0.857
Age Output : [[8.4839398e-01 1.2565422e-01 2.0150010e-02 1.2904998e-03 2.0805842e-03
  1.0233135e-03 3.8975143e-04 1.0176373e-03]]
Age : (0-2), conf = 0.848
time : 0.116
Gender : Male, conf = 0.547
Age Output : [[0.7957939  0.11903702 0.04576519 0.00874481 0.0056291  0.00942389
  0.00379017 0.01181597]]
Age : (0-2), conf = 0.796
time : 0.122
Gender : Female, conf = 0.814
Age Output : [[0.77744704 0.13498558 0.05773547 0.00701686 0.00358043 0.00681295
  0.00193119 0.01049049]]
Age : (0-2), conf = 0.777
time : 0.116
Gender : Male, conf = 0.815
Age Output : [[0.713833   0.1720707  0.08303825 0.01068472 0.0056428  0.00485564
  0.00159251 0.00828249]]
Age : (0-2), conf = 0.714
time : 0.116
Gender : Male, conf = 0.792
Age Output : [[9.3550920e-01 5.9805203e-02 2.8362526e-03 3.5491909e-04 5.5588351e-04
  2.5569848e-04 1.3869455e-04 5.4397027e-04]]
Age : (0-2), conf = 0.936
time : 0.096
Gender : Male, conf = 0.642
Age Output : [[5.9265262e-01 3.1508964e-01 7.5785123e-02 5.0056446e-03 7.0254514e-03
  1.7223974e-03 4.4954653e-04 2.2696131e-03]]
Age : (0-2), conf = 0.593
time : 0.099
Gender : Female, conf = 0.531
Age Output : [[0.72516495 0.20009173 0.02856865 0.00535139 0.03682515 0.00187926
  0.00078119 0.0013377 ]]
Age : (0-2), conf = 0.725
time : 0.089
Gender : Female, conf = 0.702
Age Output : [[0.4181003  0.41663733 0.0616651  0.01377901 0.08154681 0.00394928
  0.00177954 0.00254271]]
Age : (0-2), conf = 0.418
time : 0.100
Gender : Male, conf = 0.562
Age Output : [[0.20113118 0.143983   0.05102028 0.01754176 0.57291347 0.00782999
  0.00214365 0.0034367 ]]
Age : (25-32), conf = 0.573
time : 0.114
Gender : Female, conf = 0.692
Age Output : [[0.10185611 0.08644467 0.03012989 0.01877118 0.753697   0.00551519
  0.00142245 0.00216356]]
Age : (25-32), conf = 0.754
time : 0.127
Gender : Female, conf = 0.841
Age Output : [[0.0518293  0.03429605 0.01642824 0.01649695 0.87322056 0.00511508
  0.00108155 0.00153234]]
Age : (25-32), conf = 0.873
time : 0.113
Gender : Female, conf = 0.805
Age Output : [[0.39502215 0.33897743 0.04272126 0.01177942 0.2057959  0.00314082
  0.00104407 0.00151898]]
Age : (0-2), conf = 0.395
time : 0.120
Gender : Female, conf = 0.841
Age Output : [[0.02340359 0.03038256 0.01813531 0.01235533 0.90808004 0.005376
  0.00100961 0.00125759]]
Age : (25-32), conf = 0.908
time : 0.116
Gender : Female, conf = 0.673
Age Output : [[0.04553658 0.03386518 0.0150446  0.02357243 0.8707215  0.0079349
  0.00151892 0.00180576]]
Age : (25-32), conf = 0.871
time : 0.105
Gender : Male, conf = 0.776
Age Output : [[0.19882752 0.12916891 0.03230627 0.01286476 0.6145867  0.00745989
  0.00219152 0.00259444]]
Age : (25-32), conf = 0.615
time : 0.111
Gender : Male, conf = 0.557
Age Output : [[0.41378206 0.15471326 0.0316354  0.01238926 0.37365982 0.00761231
  0.00236996 0.00383792]]
Age : (0-2), conf = 0.414
time : 0.099
Gender : Male, conf = 0.636
Age Output : [[0.35283428 0.32348517 0.09671862 0.0148427  0.1979233  0.00767331
  0.00269195 0.00383068]]
Age : (0-2), conf = 0.353
time : 0.080
Gender : Male, conf = 0.976
Age Output : [[0.48528987 0.28682333 0.0539152  0.01393131 0.14914352 0.0060708
  0.0015977  0.00322817]]
Age : (0-2), conf = 0.485
time : 0.100
Gender : Male, conf = 0.976
Age Output : [[0.48528987 0.28682333 0.0539152  0.01393131 0.14914352 0.0060708
  0.0015977  0.00322817]]
Age : (0-2), conf = 0.485
time : 0.091
Gender : Male, conf = 0.916
Age Output : [[8.0487305e-01 1.5821257e-01 9.1059320e-03 2.1328395e-03 2.2736449e-02
  1.5010271e-03 7.0976396e-04 7.2839035e-04]]
Age : (0-2), conf = 0.805
time : 0.103
Gender : Male, conf = 0.899
Age Output : [[0.61498827 0.20972395 0.03183628 0.01113188 0.11966755 0.00745761
  0.00288093 0.00231343]]
Age : (0-2), conf = 0.615
time : 0.082
Gender : Male, conf = 0.942
Age Output : [[8.8721931e-01 8.8243410e-02 6.1091157e-03 1.4556056e-03 1.4682958e-02
  1.0387809e-03 4.8552192e-04 7.6520833e-04]]
Age : (0-2), conf = 0.887
time : 0.106
Gender : Male, conf = 0.882
Age Output : [[0.7160851  0.20926507 0.01960761 0.00361491 0.0450618  0.00280711
  0.0016428  0.00191563]]
Age : (0-2), conf = 0.716
time : 0.081
Gender : Male, conf = 0.976
Age Output : [[0.424415   0.26549837 0.07113755 0.02195794 0.19516397 0.01309551
  0.00460953 0.00412225]]
Age : (0-2), conf = 0.424
time : 0.098
Gender : Male, conf = 0.991
Age Output : [[0.6793623  0.159512   0.02190892 0.00698018 0.12433167 0.00423658
  0.00168525 0.00198312]]
Age : (0-2), conf = 0.679
time : 0.084
Gender : Male, conf = 0.970
Age Output : [[0.498376   0.24403104 0.04955074 0.01440695 0.18265116 0.00591515
  0.0020468  0.00302224]]
Age : (0-2), conf = 0.498
time : 0.085
Gender : Male, conf = 0.970
Age Output : [[0.498376   0.24403104 0.04955074 0.01440695 0.18265116 0.00591515
  0.0020468  0.00302224]]
Age : (0-2), conf = 0.498
time : 0.085
Gender : Male, conf = 0.960
Age Output : [[0.7751818  0.14466308 0.01510275 0.00533995 0.052738   0.00369799
  0.00163316 0.00164321]]
Age : (0-2), conf = 0.775
time : 0.099
Gender : Male, conf = 0.981
Age Output : [[0.6507348  0.23264621 0.03692707 0.00919347 0.05818747 0.0069238
  0.00280343 0.00258372]]
Age : (0-2), conf = 0.651
time : 0.085
Gender : Male, conf = 0.977
Age Output : [[0.86538345 0.09417388 0.00799391 0.00236215 0.02624217 0.00174883
  0.00097617 0.00111949]]
Age : (0-2), conf = 0.865
time : 0.104
Gender : Male, conf = 0.631
Age Output : [[8.5083115e-01 1.2550995e-01 9.8488890e-03 1.3260402e-03 9.4520152e-03
  1.4295321e-03 6.1116175e-04 9.9121616e-04]]
Age : (0-2), conf = 0.851
time : 0.080
Gender : Female, conf = 0.581
Age Output : [[4.3401346e-01 4.6640769e-01 8.4445886e-02 2.7622611e-03 9.3566226e-03
  1.4582567e-03 4.4612947e-04 1.1096827e-03]]
Age : (4-6), conf = 0.466
time : 0.110
Gender : Male, conf = 0.901
Age Output : [[0.82093966 0.13944995 0.01364365 0.00189326 0.02047924 0.00150087
  0.0009185  0.00117475]]
Age : (0-2), conf = 0.821
time : 0.084
Gender : Male, conf = 0.862
Age Output : [[8.4770274e-01 1.0314202e-01 1.0971281e-02 3.1609193e-03 3.1131590e-02
  1.8424892e-03 7.9051137e-04 1.2584557e-03]]
Age : (0-2), conf = 0.848
time : 0.098
Gender : Male, conf = 0.862
Age Output : [[8.4770274e-01 1.0314202e-01 1.0971281e-02 3.1609193e-03 3.1131590e-02
  1.8424892e-03 7.9051137e-04 1.2584557e-03]]
Age : (0-2), conf = 0.848
time : 0.087
Gender : Male, conf = 0.666
Age Output : [[9.1046494e-01 5.6463636e-02 6.7358599e-03 1.7763424e-03 2.0840876e-02
  1.6280795e-03 7.9042302e-04 1.2999756e-03]]
Age : (0-2), conf = 0.910
time : 0.099
Gender : Male, conf = 0.976
Age Output : [[0.8321147  0.1054292  0.01381624 0.00365353 0.04045834 0.00227847
  0.00088889 0.00136067]]
Age : (0-2), conf = 0.832
time : 0.086
Gender : Male, conf = 0.914
Age Output : [[0.7939412  0.10288478 0.01534533 0.0053345  0.07409574 0.0043224
  0.00164968 0.00242644]]
Age : (0-2), conf = 0.794
time : 0.108
Gender : Male, conf = 0.680
Age Output : [[9.6014279e-01 3.4319337e-02 2.1080256e-03 2.9479974e-04 2.4821707e-03
  3.2011687e-04 1.2625569e-04 2.0664038e-04]]
Age : (0-2), conf = 0.960
time : 0.082
Gender : Female, conf = 0.674
Age Output : [[9.7071326e-01 2.5539903e-02 1.4798024e-03 2.1766812e-04 1.4817944e-03
  2.5713944e-04 1.0302428e-04 2.0747467e-04]]
Age : (0-2), conf = 0.971
time : 0.108
Gender : Female, conf = 0.539
Age Output : [[8.9747864e-01 8.6969860e-02 6.6105588e-03 9.1787049e-04 5.9524057e-03
  9.8473416e-04 4.9268035e-04 5.9338758e-04]]
Age : (0-2), conf = 0.897
time : 0.113
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>Gender : Male, conf = 0.691
Age Output : [[0.6923273  0.15549804 0.05398604 0.00863589 0.07722334 0.00709407
  0.00215336 0.00308194]]
Age : (0-2), conf = 0.692
time : 0.098
Gender : Male, conf = 0.631
Age Output : [[0.821508   0.09671526 0.01400613 0.00309293 0.05752174 0.00369563
  0.00160081 0.00185946]]
Age : (0-2), conf = 0.822
time : 0.087
Gender : Male, conf = 0.631
Age Output : [[0.821508   0.09671526 0.01400613 0.00309293 0.05752174 0.00369563
  0.00160081 0.00185946]]
Age : (0-2), conf = 0.822
time : 0.098
Gender : Male, conf = 0.957
Age Output : [[0.15273361 0.02250277 0.01498304 0.01108434 0.7445158  0.03524726
  0.00997959 0.00895362]]
Age : (25-32), conf = 0.745
time : 0.091
Gender : Male, conf = 0.908
Age Output : [[0.3767346  0.04965083 0.00759145 0.00534804 0.540976   0.00738152
  0.00610115 0.00621636]]
Age : (25-32), conf = 0.541
time : 0.097
Gender : Male, conf = 0.911
Age Output : [[0.07266384 0.01793583 0.00528656 0.00599044 0.8675547  0.01285596
  0.00960764 0.00810486]]
Age : (25-32), conf = 0.868
time : 0.089
Gender : Male, conf = 0.982
Age Output : [[6.7569304e-04 3.8875607e-04 4.6400572e-04 1.8808171e-03 9.8928386e-01
  4.3537766e-03 1.3410320e-03 1.6120154e-03]]
Age : (25-32), conf = 0.989
time : 0.100
Gender : Male, conf = 0.959
Age Output : [[0.00829296 0.00397352 0.00255958 0.00287358 0.9701788  0.00545336
  0.00370799 0.00296028]]
Age : (25-32), conf = 0.970
time : 0.084
Gender : Male, conf = 0.980
Age Output : [[0.00319169 0.00309726 0.00426846 0.00336252 0.97943807 0.00246059
  0.00224466 0.0019368 ]]
Age : (25-32), conf = 0.979
time : 0.106
Gender : Male, conf = 0.951
Age Output : [[0.00946659 0.01051528 0.00472711 0.00232675 0.9671545  0.00210701
  0.00204384 0.00165895]]
Age : (25-32), conf = 0.967
time : 0.078
Gender : Male, conf = 0.903
Age Output : [[0.02530758 0.02287319 0.00604888 0.00259651 0.93423694 0.00358435
  0.00305699 0.00229557]]
Age : (25-32), conf = 0.934
time : 0.103
Gender : Male, conf = 0.905
Age Output : [[0.00970651 0.00915867 0.00352158 0.00320439 0.96784735 0.00249385
  0.00256949 0.00149799]]
Age : (25-32), conf = 0.968
time : 0.084
Gender : Male, conf = 0.911
Age Output : [[2.3826091e-03 4.6850313e-03 2.7095827e-03 2.5411635e-03 9.8458809e-01
  1.4855881e-03 7.5609435e-04 8.5171370e-04]]
Age : (25-32), conf = 0.985
time : 0.100
Gender : Male, conf = 0.970
Age Output : [[3.3189896e-03 4.8336103e-03 3.9317235e-03 2.1716508e-03 9.8216677e-01
  1.8647325e-03 1.0015797e-03 7.1096711e-04]]
Age : (25-32), conf = 0.982
time : 0.087
Gender : Male, conf = 0.981
Age Output : [[0.00716217 0.00956711 0.00576995 0.00337831 0.9691246  0.00241226
  0.00156494 0.00102073]]
Age : (25-32), conf = 0.969
time : 0.101
Gender : Male, conf = 0.981
Age Output : [[0.00716217 0.00956711 0.00576995 0.00337831 0.9691246  0.00241226
  0.00156494 0.00102073]]
Age : (25-32), conf = 0.969
time : 0.086
Gender : Male, conf = 0.934
Age Output : [[4.5187874e-03 8.2032848e-03 9.2603564e-03 5.4278322e-03 9.6775836e-01
  2.9383958e-03 1.1188693e-03 7.7417371e-04]]
Age : (25-32), conf = 0.968
time : 0.084
Gender : Male, conf = 0.953
Age Output : [[0.00362821 0.00682907 0.0084304  0.0050369  0.97016406 0.00335286
  0.00148685 0.00107159]]
Age : (25-32), conf = 0.970
time : 0.085
</pre></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell unrendered selected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[&nbsp;]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 4px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 7px; margin-bottom: -17px; border-right-width: 33px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 33px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 61px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to expand output; double click to hide output"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div></div><div class="end_space"></div></div>
        <div id="tooltip" class="ipython_tooltip" style="display:none"><div class="tooltipbuttons"><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="button" class="ui-button"><span class="ui-icon ui-icon-close">Close</span></a><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="button" class="ui-button" id="expanbutton" title="Grow the tooltip vertically (press shift-tab twice)"><span class="ui-icon ui-icon-plus">Expand</span></a><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="button" class="ui-button" title="show the current docstring in pager (press shift-tab 4 times)"><span class="ui-icon ui-icon-arrowstop-l-n">Open in Pager</span></a><a href="http://localhost:8888/notebooks/Real-Time%20Age%20Gender%20Detection%20using%20OpenCV.ipynb#" role="button" class="ui-button" title="Tooltip will linger for 10 seconds while you type" style="display: none;"><span class="ui-icon ui-icon-clock">Close</span></a></div><div class="pretooltiparrow"></div><div class="tooltiptext smalltooltip"></div></div>
    </div>
</div>



</div>



<div id="pager" class="ui-resizable">
    <div id="pager-contents">
        <div id="pager-container" class="container"></div>
    </div>
    <div id="pager-button-area"><a role="button" title="Open the pager in an external window" class="ui-button"><span class="ui-icon ui-icon-extlink"></span></a><a role="button" title="Close the pager" class="ui-button"><span class="ui-icon ui-icon-close"></span></a></div>
<div class="ui-resizable-handle ui-resizable-n" style="z-index: 90;"></div></div>






<script type="text/javascript">
    sys_info = {"notebook_version": "6.4.8", "notebook_path": "G:\\PROJECT 2023\\Anaconda\\Lib\\site-packages\\notebook", "commit_source": "", "commit_hash": "", "sys_version": "3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)]", "sys_executable": "G:\\PROJECT 2023\\Anaconda\\python.exe", "sys_platform": "win32", "platform": "Windows-10-10.0.19044-SP0", "os_name": "nt", "default_encoding": "utf-8"};
</script>

<script src="./Real-Time Age Gender Detection_files/encoding.js.download" charset="utf-8"></script>

<script src="./Real-Time Age Gender Detection_files/main.min.js.download" type="text/javascript" charset="utf-8"></script>



<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


<div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal;"></div></div></body></html>