%! Class = ipu-ai
%! Author = Sujal Singh
%! Date = 11/28/24

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipu-ai}[A class for AI programming practical files for the Indraprastha University.]

\LoadClass[a4paper,12pt,twoside]{report}

% --- Packages ---
\RequirePackage{lmodern}
\RequirePackage{graphicx}
\RequirePackage{tabularray}
\RequirePackage[a4paper,hmargin=1.5cm,vmargin=2.25cm]{geometry}
\RequirePackage[outputdir=./build]{minted}
\RequirePackage[most,minted,listings]{tcolorbox}
\RequirePackage{tikz}
\usetikzlibrary{shapes.geometric, arrows, calc}

% --- Arguments ---
\renewcommand{\@author}{Sujal Singh}
\newcommand{\@rollno}{04119051723} % what can one do, look up my GPA? I'll tell you, it's exactly mediocre (~50%ile).
\newcommand{\@batch}{IIOT--B1--23}
\newcommand{\@doctitle}{Programming in Python (ICT 160)}
\renewcommand{\author}[1]{\renewcommand{\@author}{#1}}
\newcommand{\rollno}[1]{\renewcommand{\@rollno}{#1}}
\newcommand{\batch}[1]{\renewcommand{\@batch}{#1}}
\newcommand{\doctitle}[1]{\renewcommand{\@doctitle}{#1}}


% --- Title Page ---
\renewcommand*{\maketitle}{
    \thispagestyle{empty}
    \pagenumbering{gobble}
    \vspace*{5pt}\noindent%
    \begin{minipage}{0.2\textwidth}
        \includegraphics[width=0.95\linewidth]{logo}~~~~~\vline
    \end{minipage}%
    \hfill%
    \begin{minipage}{0.75\textwidth}%
        \textbf{\Large Guru Gobind Singh Indraprastha University}\\[10pt]%
        {\large University School of Automation \& Robotics}
    \end{minipage}\vfill%
    \begin{center}
        \rule{\textwidth}{2pt}\\[30pt]%
        \textbf{\Huge \@doctitle}\\[20pt]%
        \textbf{\LARGE Practical File}%
        \\[25pt]\rule{\textwidth}{2pt}\\\vfill%
        {\large\begin{tblr}{width=0.75\textwidth,colspec={|X[c]|X[c]|},rows=30pt,hlines}
                   \textbf{Name}              & \@author \\
                   \textbf{Enrollment Number} & \@rollno \\
                   \textbf{Batch}             & \@batch  \\
        \end{tblr}}\\[20pt]%
    \end{center}
    \newpage
    \pagenumbering{arabic}
}

% --- Setup Long Table for Index ---
\DefTblrTemplate{caption}{default}{}    % Removes a caption
\DefTblrTemplate{capcont}{default}{}    % Removes a caption on subsequent pages
\DefTblrTemplate{contfoot}{default}{}   % Removes text denoting continuation on next page


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

\BeforeBeginEnvironment{tabularsection}{\vspace*{-20pt}}
%
%\newenvironment{flowchart}{
%    \begin{tabularsection}{Flowchart}%
%        \centering%
%        ~\\~\\%
%        }{\\~\\%
%    \end{tabularsection}}