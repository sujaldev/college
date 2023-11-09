%! Class = ipu-mechanics
%! Author = Sujal Singh
%! Date = 11/3/23

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipu-mechanics}[A class for mechanics assignments for the Indraprastha University.]

\LoadClass[a4paper,12pt,oneside]{article}

\RequirePackage{lmodern}
\RequirePackage{graphicx}
\RequirePackage{tabularray}
\RequirePackage{tabularx}
\RequirePackage{float}
\RequirePackage[a4paper,left=1.5cm,right=1.5cm,top=2cm,bottom=2cm]{geometry}

\renewcommand{\@author}{Sujal Singh}
\renewcommand{\@title}{Engineering Mechanics \\ Assignment--X}
\newcommand{\@enrollmentno}{XXXXXXXXXXXX}
\newcommand{\@rollno}{XX}
\newcommand{\@branch}{Industrial Internet of Things -- B1}

\renewcommand{\author}[1]{\renewcommand{\@author}{#1}}
\renewcommand{\title}[1]{\renewcommand{\@title}{#1}}
\newcommand{\enrollmentno}[1]{\renewcommand{\@enrollmentno}{#1}}
\newcommand{\rollno}[1]{\renewcommand{\@rollno}{#1}}
\newcommand{\branch}[1]{\renewcommand{\@branch}{#1}}

% Fetches the roll number value from the environment to keep my roll number private.
% (Shamlessly copied from https://tex.stackexchange.com/a/547742/306289)
\ExplSyntaxOn
\sys_get_shell:nnN{ kpsewhich ~ --var-value ~ ENROLLMENTNO | ~ sed ~ s/^\$/XXXXXXXXXXXX/ }{} \@enrollmentno
\sys_get_shell:nnN{ kpsewhich ~ --var-value ~ ROLLNO | ~ sed ~ s/^\$/XXXXXXXXXXXX/ }{} \@rollno
\ExplSyntaxOff

\newcounter{questions}
\setcounter{questions}{1}

\renewcommand*{\maketitle}{
    \pagenumbering{gobble}
    \begin{center}
        \vspace*{8em}
        \includegraphics[width=200pt]{../../tools/pdf/template/logo} \\[40pt]
        \textbf{\Huge \@title} \\[40pt]
        \begin{table}[htb]
            \label{tab:name-slip}
            \begin{tblr}{rows={30pt},colspec={|X|X[3]|},hlines}
                \textbf{Name}              & \@author                                    \\
                \textbf{Enrollment Number} & \@enrollmentno                              \\
                \textbf{Roll Number}       & \@rollno                                    \\
                \textbf{Branch}            & \@branch                                    \\
                \textbf{School}            & University School of Automation \& Robotics \\
                \textbf{University}        & Guru Gobind Singh Indraprastha University   \\
            \end{tblr}
        \end{table}
    \end{center}
    \newpage
    \pagenumbering{arabic}
}

\newcommand{\question}[1]{\noindent\textbf{\arabic{questions}. #1\\[5pt]}\stepcounter{questions}}

% https://tex.stackexchange.com/a/152567/306289
\newcolumntype{Y}{>{\centering\arraybackslash}X}
\newcolumntype{Z}{>{\raggedleft\arraybackslash}X}
\newcommand{\headerline}[3]{
    \noindent
    \begin{tabularx}{\textwidth}{X Y Z}
        \noindent #1 & #2 & #3
    \end{tabularx}\vspace*{-8pt}
    \rule{\textwidth}{1pt}\\[10pt]
}
