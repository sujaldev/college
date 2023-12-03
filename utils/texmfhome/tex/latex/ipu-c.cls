%! Class = ipu-c
%! Author = Sujal Singh
%! Date = 10/18/23

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipu-c}[A class for C programming practical files for the Indraprastha University.]

\LoadClass[a4paper,12pt,oneside]{article}

\RequirePackage{lmodern}
\RequirePackage{graphicx}
\RequirePackage{tabularray}
\RequirePackage[a4paper,hmargin=1.5cm,vmargin=1.5cm]{geometry}
\RequirePackage[outputdir=./build]{minted}
\RequirePackage[most,minted,listings]{tcolorbox}
\RequirePackage{tikz}
\usetikzlibrary{shapes.geometric, arrows, calc}

% Flowchart symbols (copied as is from overleaf docs)
\tikzstyle{startstop} = [rectangle, rounded corners, minimum width=3cm, minimum height=1cm,text centered, draw=black]
\tikzstyle{io} = [trapezium, trapezium left angle=70, trapezium right angle=110, minimum width=3cm, minimum height=1cm,
text centered, draw=black]
\tikzstyle{process} = [rectangle, minimum width=3cm, minimum height=1cm, text centered, draw=black]
\tikzstyle{decision} = [diamond, minimum width=3cm, minimum height=1cm, text centered, draw=black]
\tikzstyle{arrow} = [thick,->,>=stealth]

\renewcommand{\@author}{Sujal Singh}
\newcommand{\@rollno}{XXXXXXXXXXXX}
\newcommand{\@branch}{IIOT--B1--23}
\renewcommand{\author}[1]{\renewcommand{\@author}{#1}}
\newcommand{\rollno}[1]{\renewcommand{\@rollno}{#1}}
\newcommand{\branch}[1]{\renewcommand{\@branch}{#1}}

% Fetches the roll number value from the environment to keep my roll number private.
% (Shamlessly copied from https://tex.stackexchange.com/a/547742/306289)
\ExplSyntaxOn
\sys_get_shell:nnN{ kpsewhich ~ --var-value ~ ROLLNO | ~ sed ~ s/^\$/XXXXXXXXXXXX/ }{} \@rollno
\ExplSyntaxOff

\renewcommand*{\maketitle}{
    \pagenumbering{gobble}
    \begin{center}
        \vspace*{8em}
        \includegraphics[width=200pt]{logo} \\[40pt]
        \textbf{\Huge Programming Lab Practical File} \\[40pt]
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
        stripall,
        breaklines,
        xleftmargin=10pt,
    },
    overlay={%
        \begin{tcbclipinterior}
            \draw [line width=1pt] (frame.north west) rectangle ([xshift=18pt]frame.south west);
        \end{tcbclipinterior}
    }}

\BeforeBeginEnvironment{code}{\vspace*{-18pt}}

\newtcolorbox{tabularsection}[1]{
    breakable,
    enhanced,
    colback=white,
    coltitle=black,
    colbacktitle=white,
    top=0pt,
    bottom=0pt,
    sharp corners,
    title=\textbf{#1:},
}

% TODO: Implement automatic counter here which allows sub parts like "5(a)", "5(b)".
\newcommand{\experiment}[3]{%
    \newpage%
    \begin{center}%
        \textbf{\Huge Experiment--#1}\\[30pt]%
    \end{center}%
    \begin{tabularsection}{Aim}%
        ~\\#2\\%
    \end{tabularsection}%
    \begin{tabularsection}{Description}%
        ~\\#3\\%
    \end{tabularsection}}

\BeforeBeginEnvironment{tabularsection}{\vspace*{-18pt}}

\newenvironment{flowchart}{
    \begin{tabularsection}{Flowchart}%
        \centering%
        ~\\~\\%
        }{\\~\\%
    \end{tabularsection}}