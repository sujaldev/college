%! Class = CLASS_NAME
%! Author = sujal
%! Date = 5/11/24

\NeedsTeXFormat{LaTeX2e}
%! suppress = PackageNameDoesNotMatchFileName
\ProvidesPackage{ipu-ethics}[Quick class for submitting ethics assignment.]

\LoadClass[a4paper,twoside,11pt]{article}

% Packages
\RequirePackage{lmodern}
\RequirePackage[a4paper,hmargin=2cm,vmargin=1cm,includeheadfoot,headsep=10pt]{geometry}
\RequirePackage{setspace}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{enumitem}

% Arguments
\renewcommand{\@author}{Sujal Singh}
\newcommand{\@rollno}{04119051723}
\newcommand{\@batch}{IIOT--B1}
\renewcommand{\author}[1]{\renewcommand{\@author}{#1}}
\newcommand{\rollno}[1]{\renewcommand{\@rollno}{#1}}
\newcommand{\batch}[1]{\renewcommand{\@batch}{#1}}

% Headers and Footers
\fancypagestyle{assignmentstart}{
    \fancyhf{}
    \globaldefs=1
    \restoregeometry
    \newgeometry{hmargin=1.5cm,vmargin=1cm,includeheadfoot,headheight=60pt,headsep=20pt}
    \globaldefs=0
    \AddToHookNext{shipout/after}{%
        \globaldefs=1
        \restoregeometry
        \thispagestyle{fancy}
        \globaldefs=0
    }
    \fancyhead[C]{%
        \hrule\\[15pt]\textbf{\Large ICT144: Assignment -- 1}\\[4pt]\@author~--~\@rollno,~\@batch\rule[-15pt]{0pt}{2ex}}
    \fancyfoot[C]{Page \thepage}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
}
\fancypagestyle{fancy}{
    \restoregeometry
    \fancyhf{}
    \fancyhead[L]{\@author}
    \fancyhead[C]{\textbf{Assignment 1}}
    \fancyhead[RO]{\@batch}
    \fancyhead[RE]{\@rollno}
    \fancyfoot[C]{Page \thepage}
    \renewcommand{\footrulewidth}{0.4pt}
    \renewcommand{\headrulewidth}{0.4pt}
}

% Questions
\newcounter{questions}
\setcounter{questions}{0}
\newcommand{\question}[1]{\stepcounter{questions}\noindent\textbf{\arabic{questions}. #1}\\[10pt]}
