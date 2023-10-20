%! Class = ipu-c
%! Author = Sujal Singh
%! Date = 10/18/23

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipu-c}[A class for C programming practical files for the Indraprastha University.]

\LoadClass[a4paper,12pt,oneside]{article}

\RequirePackage{lmodern}
\RequirePackage{graphicx}
\RequirePackage{tabularray}
\RequirePackage[a4paper,left=1.5cm,right=1.5cm,top=2cm,bottom=2cm]{geometry}
\RequirePackage[outputdir=../build]{minted}
\RequirePackage[most,minted,listings]{tcolorbox}


\renewcommand{\@author}{Sujal Singh}
\newcommand{\@rollno}{999999999999}
\newcommand{\@branch}{Industrial Internet of Things -- B1}
\renewcommand{\author}[1]{\renewcommand{\@author}{#1}}
\newcommand{\rollno}[1]{\renewcommand{\@rollno}{#1}}
\newcommand{\branch}[1]{\renewcommand{\@branch}{#1}}

\newcounter{assignments}
\setcounter{assignments}{1}
\newcounter{questions}

\renewcommand*{\maketitle}{
    \pagenumbering{gobble}
    \begin{center}
        \vspace*{8em}
        \includegraphics[width=200pt]{logo} \\[40pt]
        \textbf{\Huge C Programming Practical File} \\[40pt]
        \begin{table}[htb]
            \label{tab:name-slip}
            \begin{tblr}{rows={30pt},colspec={|X|X[3]|},hlines}
                \textbf{Name}        & \@author                                    \\
                \textbf{Roll Number} & \@rollno                                    \\
                \textbf{Branch}      & \@branch                                    \\
                \textbf{School}      & University School of Automation \& Robotics \\
                \textbf{University}  & Guru Gobind Singh Indraprastha University   \\
            \end{tblr}
        \end{table}
    \end{center}
    \newpage
    \pagenumbering{arabic}
}

\newenvironment{assignment}{
    \newpage
    \setcounter{questions}{1}
    \begin{center}
        \textbf{\Huge Assignment--\arabic{assignments}}\\[20pt]
    \end{center}
    }{\newpage\stepcounter{assignments}}

\newcommand{\question}[1]{\noindent\textbf{\\\arabic{questions}. #1\\[5pt]}\stepcounter{questions}}

\usemintedstyle{bw}
% Changes minted line number size
\renewcommand{\theFancyVerbLine}{\parbox{10pt}{\centering\footnotesize\arabic{FancyVerbLine}}}

\newtcblisting{code}[2]{
    listing only,
    listing engine=minted,
    minted language=#2,
    breakable,
    enhanced,
    colback=white,
    coltitle=black,
    colbacktitle=white,
    top=0pt,
    bottom=0pt,
    sharp corners,
    title=\textbf{#1:},
    minted options = {
        linenos,
        autogobble,
        breaklines,
        xleftmargin=10pt,
    },
    overlay={%
        \begin{tcbclipinterior}
            \draw [line width=1pt] (frame.north west) rectangle ([xshift=18pt]frame.south west);
        \end{tcbclipinterior}
    }}

\BeforeBeginEnvironment{code}{\vspace*{-18pt}}