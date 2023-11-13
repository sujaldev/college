%! Class = IPU-papers
%! Author = Sujal Singh
%! Date = 11/10/23

\NeedsTeXFormat{LaTeX2e}
%! suppress = PackageNameDoesNotMatchFileName
\ProvidesPackage{ipu-papers}[Digital reconstruction of IPU examination papers.]

% Preamble
\LoadClass[a4paper,oneside,11pt]{article}
\RequirePackage{lmodern}
\RequirePackage[hmargin=0.5in,vmargin=0.8in]{geometry}
\RequirePackage{xifthen}
\RequirePackage{setspace}
\RequirePackage{changepage}

\pagestyle{empty}
\onehalfspace

\newcommand{\@exam}{}
\newcommand{\@papercode}{}
\newcommand{\@subject}{}
\newcommand{\@duration}{}
\newcommand{\@maxmarks}{}
\newcommand{\@note}{All questions are compulsory.}

\newcommand{\exam}[1]{\renewcommand{\@exam}{#1}}
\newcommand{\papercode}[1]{\renewcommand{\@papercode}{#1}}
\newcommand{\subject}[1]{\renewcommand{\@subject}{#1}}
\newcommand{\duration}[1]{\renewcommand{\@duration}{#1}}
\newcommand{\maxmarks}[1]{\renewcommand{\@maxmarks}{#1}}
\newcommand{\note}[1]{\renewcommand{\@note}{#1}}

\renewcommand{\maketitle}{
    \noindent\textbf{
        \begin{center}
            \vspace*{-30pt}%
            \noindent{Guru Gobind Singh Indraprastha University, East Delhi Campus\\[8pt]\@exam}
        \end{center}
        Paper Code: \@papercode \hfill Subject: \@subject
        \\[8pt]
        Time: \@duration \hfill Max Marks: \@maxmarks
        \\[8pt]
        Note: \@note%
    }\\\vspace*{-10pt}
}

% Question Environments and Commands
\newcounter{qcounter}
\newcounter{subqcounter}
\newcounter{subsubqcounter}

\newcommand{\@qprefix}{}
\newcommand{\@qnumberstyle}{}
\newcommand{\@contextcounter}{}
\newcommand{\@qpostfix}{}

\newcommand{\question}[2][]{%
    \noindent\@qprefix\@qnumberstyle\@contextcounter\@qpostfix~#2%
    \ifthenelse{\isempty{#1}}{}{\hfill(#1)}\stepcounter{\@contextcounter}\\}

\newcommand{\@setqenvdefaults}[4]{%
    \renewcommand{\@qprefix}{#1}%
    \renewcommand{\@qnumberstyle}{#2}%
    \renewcommand{\@contextcounter}{#3}%
    \renewcommand{\@qpostfix}{#4}%
    \setcounter{#3}{1}%
}

\newenvironment{qsection}{\@setqenvdefaults{Q}{\arabic}{qcounter}{.}}{}

\newenvironment{subqsection}{\@setqenvdefaults{}{\alph}{subqcounter}{)}\vspace*{-15pt}%
    \begin{adjustwidth}{\parindent}{0pt}}{\end{adjustwidth}\vspace*{-15pt}}

\newenvironment{subsubqsection}{\@setqenvdefaults{}{\roman}{subsubqcounter}{.}\vspace*{-15pt}%
    \begin{adjustwidth}{\parindent}{0pt}}{\end{adjustwidth}\vspace*{-15pt}}
