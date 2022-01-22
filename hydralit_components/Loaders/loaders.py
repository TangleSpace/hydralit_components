from enum import Enum, auto
from numpy.lib.arraysetops import isin
import streamlit as st

SHOWCASE2_GLOBAL_STYLES = """
    <style>
        a{
        text-decoration: none;
        }
        /* GRID */
        .twelve { width: 100%; }
        .eleven { width: 91.53%; }
        .ten { width: 83.06%; }
        .nine { width: 74.6%; }
        .eight { width: 66.13%; }
        .seven { width: 57.66%; }
        .six { width: 49.2%; }
        .five { width: 40.73%; }
        .four { width: 32.26%; }
        .three { width: 23.8%; }
        .two { width: 15.33%; }
        .one { width: 6.866%; }
        /* COLUMNS */
        .col {
            display: block;
            float:left;
            margin: 1% 0 1% 1.6%;
        }
        .col:first-of-type {
        margin-left: 0;
        }
        .container{
        width: 100%;
        max-width: 940px;
        margin: 0 auto;
        position: relative;
        text-align: center;
        }

        /* CLEARFIX */
        .cf:before,
        .cf:after {
            content: " ";
            display: table;
        }
        .cf:after {
            clear: both;
        }
        .cf {
            *zoom: 1;
        }
        .row{
        margin: 30px 0;
        }
        .three{
        padding: 50px 0;
        }
        /* ALL LOADERS */
        .loader{
        width: 100px;
        height: 100px;
        margin: 75px;
        border-radius: 100%;
        position: relative;
        display: inline-block;
        vertical-align: middle;
        }

        /* LOADER 1 */

        #loader-1:before, #loader-1:after{
        content: "";
        position: absolute;
        top: -10px;
        left: -10px;
        width: 100%;
        height: 100%;
        border-radius: 100%;
        border: 10px solid transparent;
        border-top-color: ||-pcolor-||;
        }

        #loader-1:before{
        z-index: 100;
        animation: spin 1s infinite;
        }

        #loader-1:after{
        border: 10px solid #ccc;
        }

        @keyframes spin{
        0%{
            -webkit-transform: rotate(0deg);
            -ms-transform: rotate(0deg);
            -o-transform: rotate(0deg);
            transform: rotate(0deg);
        }

        100%{
            -webkit-transform: rotate(360deg);
            -ms-transform: rotate(360deg);
            -o-transform: rotate(360deg);
            transform: rotate(360deg);
        }
        }

        /* LOADER 2 */

        #loader-2 span{
        display: inline-block;
        width: 20px;
        height: 20px;
        border-radius: 100%;
        background-color: ||-pcolor-||;
        margin: 35px 5px;
        }

        #loader-2 span:nth-child(1){
        animation: bounce 1s ease-in-out infinite;
        }

        #loader-2 span:nth-child(2){
        animation: bounce 1s ease-in-out 0.33s infinite;
        }

        #loader-2 span:nth-child(3){
        animation: bounce 1s ease-in-out 0.66s infinite;
        }

        @keyframes bounce{
        0%, 75%, 100%{
            -webkit-transform: translateY(0);
            -ms-transform: translateY(0);
            -o-transform: translateY(0);
            transform: translateY(0);
        }

        25%{
            -webkit-transform: translateY(-20px);
            -ms-transform: translateY(-20px);
            -o-transform: translateY(-20px);
            transform: translateY(-20px);
        }
        }

        /* LOADER 3 */

        #loader-3:before, #loader-3:after{
        content: "";
        width: 20px;
        height: 20px;
        position: absolute;
        top: 0;
        left: calc(50% - 10px);
        background-color: ||-pcolor-||;
        animation: squaremove 1s ease-in-out infinite;
        }

        #loader-3:after{
        bottom: 0;
        animation-delay: 0.5s;
        }

        @keyframes squaremove{
        0%, 100%{
            -webkit-transform: translate(0,0) rotate(0);
            -ms-transform: translate(0,0) rotate(0);
            -o-transform: translate(0,0) rotate(0);
            transform: translate(0,0) rotate(0);
        }

        25%{
            -webkit-transform: translate(40px,40px) rotate(45deg);
            -ms-transform: translate(40px,40px) rotate(45deg);
            -o-transform: translate(40px,40px) rotate(45deg);
            transform: translate(40px,40px) rotate(45deg);
        }

        50%{
            -webkit-transform: translate(0px,80px) rotate(0deg);
            -ms-transform: translate(0px,80px) rotate(0deg);
            -o-transform: translate(0px,80px) rotate(0deg);
            transform: translate(0px,80px) rotate(0deg);
        }

        75%{
            -webkit-transform: translate(-40px,40px) rotate(45deg);
            -ms-transform: translate(-40px,40px) rotate(45deg);
            -o-transform: translate(-40px,40px) rotate(45deg);
            transform: translate(-40px,40px) rotate(45deg);
        }
        }

        /* LOADER 4 */

        #loader-4 span{
        display: inline-block;
        width: 20px;
        height: 20px;
        border-radius: 100%;
        background-color: ||-pcolor-||;
        margin: 35px 5px;
        opacity: 0;
        }

        #loader-4 span:nth-child(1){
        animation: opacitychange 1s ease-in-out infinite;
        }

        #loader-4 span:nth-child(2){
        animation: opacitychange 1s ease-in-out 0.33s infinite;
        }

        #loader-4 span:nth-child(3){
        animation: opacitychange 1s ease-in-out 0.66s infinite;
        }

        @keyframes opacitychange{
        0%, 100%{
            opacity: 0;
        }

        60%{
            opacity: 1;
        }
        }

        /* LOADER 5 */

        #loader-5 span{
        display: block;
        position: absolute;
        left: calc(50% - 20px);
        top: calc(50% - 20px);
        width: 20px;
        height: 20px;
        background-color: ||-pcolor-||;
        }

        #loader-5 span:nth-child(2){
        animation: moveanimation1 1s ease-in-out infinite;
        }

        #loader-5 span:nth-child(3){
        animation: moveanimation2 1s ease-in-out infinite;
        }

        #loader-5 span:nth-child(4){
        animation: moveanimation3 1s ease-in-out infinite;
        }

        @keyframes moveanimation1{
        0%, 100%{
            -webkit-transform: translateX(0px);
            -ms-transform: translateX(0px);
            -o-transform: translateX(0px);
            transform: translateX(0px);
        }

        75%{
            -webkit-transform: translateX(30px);
            -ms-transform: translateX(30px);
            -o-transform: translateX(30px);
            transform: translateX(30px);
        }
        }

        @keyframes moveanimation2{
        0%, 100%{
            -webkit-transform: translateY(0px);
            -ms-transform: translateY(0px);
            -o-transform: translateY(0px);
            transform: translateY(0px);
        }

        75%{
            -webkit-transform: translateY(30px);
            -ms-transform: translateY(30px);
            -o-transform: translateY(30px);
            transform: translateY(30px);
        }
        }

        @keyframes moveanimation3{
        0%, 100%{
            -webkit-transform: translate(0px, 0px);
            -ms-transform: translate(0px, 0px);
            -o-transform: translate(0px, 0px);
            transform: translate(0px, 0px);
        }

        75%{
            -webkit-transform: translate(30px, 30px);
            -ms-transform: translate(30px, 30px);
            -o-transform: translate(30px, 30px);
            transform: translate(30px, 30px);
        }
        }

        /* LOADER 6 */

        #loader-6{
        top: 40px;
        left: -2.5px;
        }

        #loader-6 span{
        display: inline-block;
        width: 5px;
        height: 20px;
        background-color: ||-pcolor-||;
        }

        #loader-6 span:nth-child(1){
        animation: grow 1s ease-in-out infinite;
        }

        #loader-6 span:nth-child(2){
        animation: grow 1s ease-in-out 0.15s infinite;
        }

        #loader-6 span:nth-child(3){
        animation: grow 1s ease-in-out 0.30s infinite;
        }

        #loader-6 span:nth-child(4){
        animation: grow 1s ease-in-out 0.45s infinite;
        }

        @keyframes grow{
        0%, 100%{
            -webkit-transform: scaleY(1);
            -ms-transform: scaleY(1);
            -o-transform: scaleY(1);
            transform: scaleY(1);
        }

        50%{
            -webkit-transform: scaleY(1.8);
            -ms-transform: scaleY(1.8);
            -o-transform: scaleY(1.8);
            transform: scaleY(1.8);
        }
        }

        /* LOADER 7 */

        #loader-7{
        -webkit-perspective: 120px;
        -moz-perspective: 120px;
        -ms-perspective: 120px;
        perspective: 120px;
        }

        #loader-7:before{
        content: "";
        position: absolute;
        left: 25px;
        top: 25px;
        width: 50px;
        height: 50px;
        background-color: ||-pcolor-||;
        animation: flip 1s infinite;
        }

        @keyframes flip {
        0% {
            transform: rotate(0);
        }

        50% {
            transform: rotateY(180deg);
        }

        100% {
            transform: rotateY(180deg)  rotateX(180deg);
        }
        }

        /* LOADER 8 */

        #loader-8:before{
        content: "";
        position: absolute;
        width: 10px;
        height: 10px;
        top: calc(50% - 10px);
        left: 0px;
        background-color: ||-pcolor-||;
        animation: rotatemove 1s infinite;
        }

        @keyframes rotatemove{
        0%{
            -webkit-transform: scale(1) translateX(0px);
            -ms-transform: scale(1) translateX(0px);
            -o-transform: scale(1) translateX(0px);
            transform: scale(1) translateX(0px);
        }

        100%{
            -webkit-transform: scale(2) translateX(45px);
            -ms-transform: scale(2) translateX(45px);
            -o-transform: scale(2) translateX(45px);
            transform: scale(2) translateX(45px);
        }
        }


    </style>
    """

SHOWCASE_GLOBAL_STYLES = """
<style>
    .parent {
    display: flex;
    position: absolute;
    justify-content: center;
    text-align: center;
    width: 100%;
    height: ||-height-||;
    z-index: 999;
    }         
    .container {
        text-align: center;
        z-index: 998;
    }
  
    section {
        width: 30%;
        display: inline-block;
        text-align: center;
        min-height: 215px;
        vertical-align: top;
        margin: 1%;
    }

@media only screen and (max-width: 600px) {
  section {
    min-width: 350px;
  }
}
    
    .loader {
        position: relative;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        margin: 75px;
        display: inline-block;
        vertical-align: middle;
    }
    
    .loader-star {
        position: absolute;
        top: calc(50% - 12px);
    }
    /*LOADER-1*/
    
    .loader-1 .loader-outter {
        position: absolute;
        border: 4px solid ||-pcolor-||;
        border-left-color: transparent;
        border-bottom: 0;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        -webkit-animation: loader-1-outter 1s cubic-bezier(.42, .61, .58, .41) infinite;
        animation: loader-1-outter 1s cubic-bezier(.42, .61, .58, .41) infinite;
    }
    
    .loader-1 .loader-inner {
        position: absolute;
        border: 4px solid ||-pcolor-||;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        left: calc(50% - 20px);
        top: calc(50% - 20px);
        border-right: 0;
        border-top-color: transparent;
        -webkit-animation: loader-1-inner 1s cubic-bezier(.42, .61, .58, .41) infinite;
        animation: loader-1-inner 1s cubic-bezier(.42, .61, .58, .41) infinite;
    }
    /*LOADER-2*/
    
    .loader-2 .loader-star {
        position: static;
        width: 60px;
        height: 60px;
        -webkit-transform: scale(0.7);
        -ms-transform: scale(0.7);
            transform: scale(0.7);
        -webkit-animation: loader-2-star 1s ease alternate infinite;
        animation: loader-2-star 1s ease alternate infinite;
    }
    
    .loader-2 .loader-circles {
        width: 8px;
        height: 8px;
        background: #18ffff;
        border-radius: 50%;
        position: absolute;
        left: calc(50% - 4px);
        top: calc(50% - 4px);
        -webkit-transition: all 1s ease;
        -o-transition: all 1s ease;
        transition: all 1s ease;
        -webkit-animation: loader-2-circles 1s ease-in-out alternate infinite;
        animation: loader-2-circles 1s ease-in-out alternate infinite;
    }
    /*LOADER-3*/
    
    .loader-3 .dot {
        width: 10px;
        height: 10px;
        background: #00e676;
        border-radius: 50%;
        position: absolute;
        top: calc(50% - 5px);
    }
    
    .loader-3 .dot1 {
        left: 0px;
        -webkit-animation: dot-jump 0.5s cubic-bezier(0.77, 0.47, 0.64, 0.28) alternate infinite;
        animation: dot-jump 0.5s cubic-bezier(0.77, 0.47, 0.64, 0.28) alternate infinite;
    }
    
    .loader-3 .dot2 {
        left: 20px;
        -webkit-animation: dot-jump 0.5s 0.2s cubic-bezier(0.77, 0.47, 0.64, 0.28) alternate infinite;
        animation: dot-jump 0.5s 0.2s cubic-bezier(0.77, 0.47, 0.64, 0.28) alternate infinite;
    }
    
    .loader-3 .dot3 {
        left: 40px;
        -webkit-animation: dot-jump 0.5s 0.4s cubic-bezier(0.77, 0.47, 0.64, 0.28) alternate infinite;
        animation: dot-jump 0.5s 0.4s cubic-bezier(0.77, 0.47, 0.64, 0.28) alternate infinite;
    }
    /*LOADER-4*/
    
    .loader-4 {
        border: 7px double #ff5722;
        -webkit-animation: ball-turn 1s linear infinite;
        animation: ball-turn 1s linear infinite;
    }
    
    .loader-4:before,
    .loader-4:after {
        content: "";
        position: absolute;
        width: 12px;
        height: 12px;
        background: #ff5722;
        border-radius: 50%;
        bottom: 0;
        right: 37px;
    }
    
    .loader-4:after {
        left: 37px;
        top: 0;
    }
    /*LOADER-5*/
    
    .loader-5 {
        border: 8px dotted rgba(255, 255, 0, 1);
        -webkit-transition: all 1s ease;
        -o-transition: all 1s ease;
        transition: all 1s ease;
        -webkit-animation: dotted-spin 1s linear infinite;
        animation: dotted-spin 1s linear infinite;
        border-bottom-width: 1px;
        border-bottom-color: rgba(255, 255, 0, 0.3);
        border-left-width: 2px;
        border-left-color: rgba(255, 255, 0, 0.5);
        border-top-width: 3px;
        border-right-width: 4px;
        border-top-color: rgba(255, 255, 0, 0.7);
    }
    
    .loader-5 .loader-pacman,
    .loader-pacman {
        position: absolute;
        top: 40px;
        left: 25px;
        width: 0px;
        height: 0px;
        border-right: 12px solid transparent;
        border-top: 12px solid rgba(255, 255, 0, 1);
        border-left: 12px solid rgba(255, 255, 0, 1);
        border-bottom: 12px solid rgba(255, 255, 0, 1);
        border-top-left-radius: 12px;
        border-top-right-radius: 12px;
        border-bottom-left-radius: 12px;
        border-bottom-right-radius: 12px;
    }
    /*LOADER-6*/
    
    .loader-6 {
        border: 6px groove #7e57c2;
        -webkit-transform: rotate(360deg);
        -ms-transform: rotate(360deg);
            transform: rotate(360deg);
        -webkit-transition: all 1s ease;
        -o-transition: all 1s ease;
        transition: all 1s ease;
        -webkit-animation: loader-1-inner 1s ease-out alternate infinite;
        animation: loader-1-inner 1s ease-out alternate infinite;
    }
    
    .loader-6 .loader-inner {
        border: 0px inset #9575cd;
        border-radius: 50%;
        width: 100%;
        height: 100%;
        -webkit-animation: border-zoom 1s ease-out alternate infinite;
        animation: border-zoom 1s ease-out alternate infinite;
    }
    /*LOADER-7*/
    
    .loader-7 .line {
        width: 8px;
        position: absolute;
        border-radius: 5px;
        bottom: 0;
        background: -webkit-gradient(linear, left top, left bottom, from(#1ee95d), to(#5714ce));
        background: -webkit-linear-gradient(top, #1ee95d, #5714ce);
        background: -o-linear-gradient(top, #1ee95d, #5714ce);
        background: linear-gradient(to bottom, #1ee95d, #5714ce);
    }
    
    .loader-7 .line1 {
        left: 0;
        -webkit-animation: line-grow 0.5s ease alternate infinite;
        animation: line-grow 0.5s ease alternate infinite;
    }
    
    .loader-7 .line2 {
        left: 20px;
        -webkit-animation: line-grow 0.5s 0.2s ease alternate infinite;
        animation: line-grow 0.5s 0.2s ease alternate infinite;
    }
    
    .loader-7 .line3 {
        left: 40px;
        -webkit-animation: line-grow 0.5s 0.4s ease alternate infinite;
        animation: line-grow 0.5s 0.4s ease alternate infinite;
    }
    /*LOADER-8*/
    
    .loader-8 .star1 {
        -webkit-animation: star-jump 0.5s ease-out alternate infinite;
        animation: star-jump 0.5s ease-out alternate infinite;
    }
    
    .loader-8 .star2 {
        -webkit-animation: star-jump 0.5s 0.25s ease-out alternate infinite;
        animation: star-jump 0.5s 0.25s ease-out alternate infinite;
    }
    
    .loader-8 .star3 {
        -webkit-animation: star-jump 0.5s 0.5s ease-out alternate infinite;
        animation: star-jump 0.5s 0.5s ease-out alternate infinite;
    }
    
    .loader-8 .loader-star {
        -webkit-transform: scale3d(0.7, 0.7, 0.7);
        transform: scale3d(0.7, 0.7, 0.7);
    }
    
    .loader-8 .star1 {
        left: 0px;
    }
    
    .loader-8 .star2 {
        left: 25px;
    }
    
    .loader-8 .star3 {
        left: 50px;
    }
    /*LOADER-9*/
    
    .loader-9 .star1 {
        -webkit-animation: stars-pulse 1s ease-in-out infinite;
        animation: stars-pulse 1s ease-in-out infinite;
        left: 0;
    }
    
    .loader-9 .star2 {
        -webkit-animation: stars-pulse 1s 0.2s ease-in-out infinite;
        animation: stars-pulse 1s 0.2s ease-in-out infinite;
        left: 25px;
    }
    
    .loader-9 .star3 {
        -webkit-animation: stars-pulse 1s 0.4s ease-in-out infinite;
        animation: stars-pulse 1s 0.4s ease-in-out infinite;
        left: 50px;
    }
    /*LOADER-10*/
    
    .loader-10 {
        width: auto;
        height: auto;
        -webkit-animation: star-pulse 2s ease-in-out infinite;
        animation: star-pulse 2s ease-in-out infinite;
    }
    
    .loader-10 .loader-star {
        position: static;
    }
    /*LOADER-11*/
    
    .loader-11 {
        /*    animation: stars-rotate 2s cubic-bezier(0, 0, 0.63, 0.77) infinite;*/
        -webkit-animation: stars-rotate 2s linear infinite;
        animation: stars-rotate 2s linear infinite;
    }
    
    .loader-11 .loader-star {
        position: absolute;
    }
    
    .loader-11 .star1 {
        top: 0px;
        left: -7px;
    }
    
    .loader-11 .star2 {
        left: 8px;
        top: -12px;
        position: absolute;
        -webkit-transform: scale(0.8);
        -ms-transform: scale(0.8);
            transform: scale(0.8);
        opacity: 0.9;
    }
    
    .loader-11 .star3 {
        left: 26px;
        top: -11px;
        position: absolute;
        -webkit-transform: scale(0.7);
        -ms-transform: scale(0.7);
            transform: scale(0.7);
        opacity: 0.8;
    }
    
    .loader-11 .star4 {
        left: 39px;
        top: -2px;
        position: absolute;
        -webkit-transform: scale(0.6);
        -ms-transform: scale(0.6);
            transform: scale(0.6);
        opacity: 0.7;
    }
    
    .loader-11 .star5 {
        left: 44px;
        top: 10px;
        position: absolute;
        -webkit-transform: scale(0.5);
        -ms-transform: scale(0.5);
            transform: scale(0.5);
        opacity: 0.6;
    }
    
    .loader-11 .star6 {
        left: 45px;
        top: 21px;
        position: absolute;
        -webkit-transform: scale(0.4);
        -ms-transform: scale(0.4);
            transform: scale(0.4);
        opacity: 0.5;
    }
    /*LOADER-12*/
    
    .loader-12 {
        -webkit-animation: stars-rotate-reverse 2s ease infinite;
        animation: stars-rotate-reverse 2s ease infinite;
    }
    
    .loader-12 polygon {
        fill: #d500f9 !important;
    }
    
    .loader-12 .loader-star {
        position: absolute;
    }
    
    .loader-12 .star1 {
        top: 0px;
        right: -7px;
    }
    
    .loader-12 .star2 {
        right: 9px;
        top: -12px;
        position: absolute;
        -webkit-transform: scale(0.8);
        -ms-transform: scale(0.8);
            transform: scale(0.8);
        -webkit-animation: stars-catch 2s 0.1s ease infinite;
        animation: stars-catch 2s 0.1s ease infinite;
    }
    
    .loader-12 .star3 {
        right: 27px;
        top: -11px;
        position: absolute;
        -webkit-transform: scale(0.7);
        -ms-transform: scale(0.7);
            transform: scale(0.7);
        -webkit-animation: stars-catch 2s 0.15s ease infinite;
        animation: stars-catch 2s 0.15s ease infinite;
    }
    
    .loader-12 .star4 {
        right: 41px;
        top: -2px;
        position: absolute;
        -webkit-transform: scale(0.6);
        -ms-transform: scale(0.6);
            transform: scale(0.6);
        -webkit-animation: stars-catch 2s 0.2s ease infinite;
        animation: stars-catch 2s 0.2s ease infinite;
    }
    
    .loader-12 .star5 {
        right: 47px;
        top: 10px;
        position: absolute;
        -webkit-transform: scale(0.5);
        -ms-transform: scale(0.5);
            transform: scale(0.5);
        -webkit-animation: stars-catch 2s 0.25s ease infinite;
        animation: stars-catch 2s 0.25s ease infinite;
    }
    
    .loader-12 .star6 {
        right: 47px;
        top: 21px;
        position: absolute;
        -webkit-transform: scale(0.4);
        -ms-transform: scale(0.4);
            transform: scale(0.4);
        -webkit-animation: stars-catch 2s 0.3s ease infinite;
        animation: stars-catch 2s 0.3s ease infinite;
    }

    /*LOADER-13*/
    
    
    .loader-13 .css-heart {
        position: absolute;
        -webkit-animation: star-fly-out 1s ease alternate infinite;
        animation: star-fly-out 1s ease alternate infinite;
        -webkit-transform: scale(0.2);
            -ms-transform: scale(0.2);
                transform: scale(0.2);
    }
    
    .loader-13 .heart1 {
        top: 0;
        left: 30px;
    }
    
    .loader-13 .heart2 {
        left: 60px;
        top: 30px;
    }
    
    .loader-13 .heart3 {
        top: 60px;
        left: 30px;
    }
    
    .loader-13 .heart4 {
        left: 0;
        top: 30px;
    }


    /*LOADER-14*/
    
  
    
    .loader-14 .loader-star {
        position: absolute;
        top: calc(50% - 12px);
        left: calc(50% - 12px);
    }
    
    .star-small {
        -webkit-animation: star-small-pulse 1s ease-in-out alternate infinite;
        animation: star-small-pulse 1s ease-in-out alternate infinite;
    }
    
    .loader-14 .star-big {
        -webkit-animation: star-big-pulse 2s -0.2s ease-in-out infinite;
        animation: star-big-pulse 2s -0.2s ease-in-out infinite;
    }
    /*LOADER-15*/
    
    .loader-15 {
        border: 2px dotted #e11a2b;
        -webkit-animation: stars-rotate-reverse 2s linear both infinite;
        animation: stars-rotate-reverse 2s linear both infinite;
    }
    
    .loader-15 .loader-star {
        -webkit-transform: scale(1.5);
        -ms-transform: scale(1.5);
            transform: scale(1.5);
        position: absolute;
        left: calc(50% - 12px);
        top: calc(50% - 13px);
    }
    /*CSS-STAR*/
    
    .css-star {
        margin: 10px 0;
        position: relative;
        display: block;
        width: 0px;
        height: 0px;
        border-right: 26px solid transparent;
        border-bottom: 23px solid #e11a2b;
        border-left: 23px solid transparent;
        -webkit-transform: rotate(180deg);
        -ms-transform: rotate(180deg);
            transform: rotate(180deg);
    }
    
    .css-star:before {
        border-bottom: 18px solid #e11a2b;
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        position: absolute;
        height: 0;
        width: 0;
        top: -9px;
        left: -16px;
        display: block;
        content: '';
        -webkit-transform: rotate(-35deg);
        -moz-transform: rotate(-35deg);
        -ms-transform: rotate(-35deg);
        -o-transform: rotate(-35deg);
    }
    
    .css-star:after {
        position: absolute;
        display: block;
        top: 2px;
        left: -26px;
        width: 0px;
        height: 0px;
        border-right: 25px solid transparent;
        border-bottom: 22px solid #e11a2b;
        border-left: 27px solid transparent;
        -webkit-transform: rotate(-70deg);
        -moz-transform: rotate(-70deg);
        -ms-transform: rotate(-70deg);
        -o-transform: rotate(-70deg);
        content: '';
    }
    /*LOADER-16*/
    
    .loader-16 .css-star {
        position: absolute;
        -webkit-transform: rotate(180deg) scale(0.35);
        -ms-transform: rotate(180deg) scale(0.35);
            transform: rotate(180deg) scale(0.35);
    }
    
    .loader-16 .star1 {
        top: -20px;
        left: 5px;
        -webkit-animation: star-flicker 1s 0.1s linear infinite;
        animation: star-flicker 1s 0.1s linear infinite;
    }
    
    .loader-16 .star2 {
        left: 25px;
        top: -10px;
        -webkit-animation: star-flicker 1s 0.25s linear infinite;
        animation: star-flicker 1s 0.25s linear infinite;
    }
    
    .loader-16 .star3 {
        left: 35px;
        top: 10px;
        -webkit-animation: star-flicker 1s 0.5s linear infinite;
        animation: star-flicker 1s 0.5s linear infinite;
    }
    
    .loader-16 .star4 {
        top: 30px;
        left: 27px;
        -webkit-animation: star-flicker 1s 0.6s linear infinite;
        animation: star-flicker 1s 0.6s linear infinite;
    }
    
    .loader-16 .star5 {
        top: 40px;
        left: 5px;
        -webkit-animation: star-flicker 1s 0.7s linear infinite;
        animation: star-flicker 1s 0.7s linear infinite;
    }
    
    .loader-16 .star6 {
        top: 30px;
        left: -15px;
        -webkit-animation: star-flicker 1s 0.8s linear infinite;
        animation: star-flicker 1s 0.8s linear infinite;
    }
    
    .loader-16 .star7 {
        top: 10px;
        left: -25px;
        -webkit-animation: star-flicker 1s 0.9s linear infinite;
        animation: star-flicker 1s 0.9s linear infinite;
    }
    
    .loader-16 .star8 {
        top: -10px;
        left: -15px;
        -webkit-animation: star-flicker 1s 1s linear infinite;
        animation: star-flicker 1s 1s linear infinite;
    }
    /*LOADER-17*/
    
 .loader-17 .css-square { 
      position: absolute;
      top: 50%;
      width: 25px; height: 7px;
    background: white;
    -webkit-box-shadow: 2px 2px 3px 0px black;
            box-shadow: 2px 2px 3px 0px black;
   }

    
    .loader-17 .square1 {
        left: 70px;
        -webkit-animation: dominos 1s 0.125s ease infinite;
        animation: dominos 1s 0.125s ease infinite;
    }
    
    .loader-17 .square2 {
        left: 60px;
        -webkit-animation: dominos 1s 0.3s ease infinite;
        animation: dominos 1s 0.3s ease infinite;
    }
    
    .loader-17 .square3 {
        left: 50px;
        -webkit-animation: dominos 1s 0.425s ease infinite;
        animation: dominos 1s 0.425s ease infinite;
    }
    
    .loader-17 .square4 {
        left: 40px;
        -webkit-animation: dominos 1s 0.540s ease infinite;
        animation: dominos 1s 0.540s ease infinite;
    }
    
    .loader-17 .square5 {
        left: 30px;
        -webkit-animation: dominos 1s 0.665s ease infinite;
        animation: dominos 1s 0.665s ease infinite;
    }
    
    .loader-17 .square6 {
        left: 20px;
        -webkit-animation: dominos 1s 0.79s ease infinite;
        animation: dominos 1s 0.79s ease infinite;
    }
    
    .loader-17 .square7 {
        left: 10px;
        -webkit-animation: dominos 1s 0.9s ease infinite;
        animation: dominos 1s 0.9s ease infinite;
    }
    
    .loader-17 .square8 {
        left: 0px;
        -webkit-animation: dominos 1s 1s ease infinite;
        animation: dominos 1s 1s ease infinite;
    }


    /*LOADER-18*/
    
    .loader-18 .css-star {
        position: absolute;
        -webkit-transform: rotate(180deg) scale(0.5);
        -ms-transform: rotate(180deg) scale(0.5);
            transform: rotate(180deg) scale(0.5);
        opacity: 0.4;
    }
    
    .loader-18 .css-star,
    .loader-18 .css-star:before,
    .loader-18 .css-star:after {
        border-bottom-color: #00e676;
    }
    
    .loader-18 .star1 {
        top: -20px;
        left: 5px;
        -webkit-animation: star-crazyness 1s 0.125s ease infinite;
        animation: star-crazyness 1s 0.125s ease infinite;
    }
    
    .loader-18 .star2 {
        left: 25px;
        top: -10px;
        -webkit-animation: star-crazyness 1s 0.3s ease infinite;
        animation: star-crazyness 1s 0.3s ease infinite;
    }
    
    .loader-18 .star3 {
        left: 35px;
        top: 10px;
        -webkit-animation: star-crazyness 1s 0.425s ease infinite;
        animation: star-crazyness 1s 0.425s ease infinite;
    }
    
    .loader-18 .star4 {
        top: 30px;
        left: 27px;
        -webkit-animation: star-crazyness 1s 0.540s ease infinite;
        animation: star-crazyness 1s 0.540s ease infinite;
    }
    
    .loader-18 .star5 {
        top: 40px;
        left: 5px;
        -webkit-animation: star-crazyness 1s 0.665s ease infinite;
        animation: star-crazyness 1s 0.665s ease infinite;
    }
    
    .loader-18 .star6 {
        top: 30px;
        left: -15px;
        -webkit-animation: star-crazyness 1s 0.79s ease infinite;
        animation: star-crazyness 1s 0.79s ease infinite;
    }
    
    .loader-18 .star7 {
        top: 10px;
        left: -25px;
        -webkit-animation: star-crazyness 1s 0.9s ease infinite;
        animation: star-crazyness 1s 0.9s ease infinite;
    }
    
    .loader-18 .star8 {
        top: -10px;
        left: -15px;
        -webkit-animation: star-crazyness 1s 1s ease infinite;
        animation: star-crazyness 1s 1s ease infinite;
    }
    /*LOADER-19*/
    
    .loader-19 .css-star {
        position: absolute;
        -webkit-transform: rotate(180deg) scale(0.5);
        -ms-transform: rotate(180deg) scale(0.5);
            transform: rotate(180deg) scale(0.5);
    }
    
    .loader-19 .star1 {
        left: 0;
        -webkit-animation: star-crawl 1s ease-out alternate infinite;
        animation: star-crawl 1s ease-out alternate infinite;
    }
    
    .loader-19 .star2 {
        left: 22px;
        -webkit-transform: rotate(180deg) scale(0.45);
        -ms-transform: rotate(180deg) scale(0.45);
            transform: rotate(180deg) scale(0.45);
        -webkit-animation: star-crawl 1s 0.1s ease-out alternate infinite;
        animation: star-crawl 1s 0.1s ease-out alternate infinite;
    }
    
    .loader-19 .star3 {
        left: 44px;
        -webkit-transform: rotate(180deg) scale(0.4);
        -ms-transform: rotate(180deg) scale(0.4);
            transform: rotate(180deg) scale(0.4);
        -webkit-animation: star-crawl 1s 0.2s ease-out alternate infinite;
        animation: star-crawl 1s 0.2s ease-out alternate infinite;
    }
    
    .loader-19 .star4 {
        left: 66px;
        -webkit-transform: rotate(180deg) scale(0.35);
        -ms-transform: rotate(180deg) scale(0.35);
            transform: rotate(180deg) scale(0.35);
        -webkit-animation: star-crawl 1s 0.3s ease-out alternate infinite;
        animation: star-crawl 1s 0.3s ease-out alternate infinite;
    }
    
    .loader-19 .star5 {
        left: 88px;
        -webkit-transform: rotate(180deg) scale(0.3);
        -ms-transform: rotate(180deg) scale(0.3);
            transform: rotate(180deg) scale(0.3);
        -webkit-animation: star-crawl 1s 0.4s ease-out alternate infinite;
        animation: star-crawl 1s 0.4s ease-out alternate infinite;
    }
    
    .loader-19 .star6 {
        left: 110px;
        -webkit-transform: rotate(180deg) scale(0.25);
        -ms-transform: rotate(180deg) scale(0.25);
            transform: rotate(180deg) scale(0.25);
        -webkit-animation: star-crawl 1s 0.5s ease-out alternate infinite;
        animation: star-crawl 1s 0.5s ease-out alternate infinite;
    }
    
    .loader-19 .star7 {
        left: 132px;
        -webkit-transform: rotate(180deg) scale(0.2);
        -ms-transform: rotate(180deg) scale(0.2);
            transform: rotate(180deg) scale(0.2);
        -webkit-animation: star-crawl 1s 0.6s ease-out alternate infinite;
        animation: star-crawl 1s 0.6s ease-out alternate infinite;
    }
    
    .loader-19 .star8 {
        left: 154px;
        -webkit-transform: rotate(180deg) scale(0.15);
        -ms-transform: rotate(180deg) scale(0.15);
            transform: rotate(180deg) scale(0.15);
        -webkit-animation: star-crawl 1s 0.7s ease-out alternate infinite;
        animation: star-crawl 1s 0.7s ease-out alternate infinite;
    }
    
    .loader-20 {
        width: 70px;
        height: 70px;
        border: 3px dashed #d3d3d3;
        -webkit-animation: stars-rotate-reverse 2s linear both infinite;
        animation: stars-rotate-reverse 2s linear both infinite;
    }
    
    .loader-20 .css-diamond {
        position: absolute;
        left: calc(50% - 50px);
        top: calc(50% - 50px);
        -webkit-transform: scale(0.3);
            -ms-transform: scale(0.3);
                transform: scale(0.3);
        -webkit-transform-origin: 50% 100%;
            -ms-transform-origin: 50% 100%;
                transform-origin: 50% 100%;
        border-color: transparent transparent #fff transparent;
    }
    
    .loader-20 .css-diamond:after {
        border-color: lightgrey transparent transparent transparent;
    }
    
    .css-diamond {
        border-style: solid;
        border-color: transparent transparent #ce93d8 transparent;
        border-width: 0 25px 25px 25px;
        height: 0;
        width: 100px;
        position: relative;
        margin: 20px 0 50px 0;
    }
    
    .css-diamond:after {
        content: "";
        position: absolute;
        top: 25px;
        left: -25px;
        width: 0;
        height: 0;
        border-style: solid;
        border-color: #ce93d8 transparent transparent transparent;
        border-width: 70px 50px 0 50px;
    }
    
    .css-heart {
        position: absolute;
  /*      width: 100px;
        height: 90px;*/
    }
    
    .css-heart:before,
    .css-heart:after {
        position: absolute;
        content: "";
        left: 50px;
        top: 0;
        width: 50px;
        height: 80px;
        background: #950d0d;
        border-radius: 50px 50px 0 0;
        -webkit-transform: rotate(-45deg);
            -ms-transform: rotate(-45deg);
                transform: rotate(-45deg);
        -webkit-transform-origin: 0 100%;
            -ms-transform-origin: 0 100%;
                transform-origin: 0 100%;
    }
    
    .css-heart:after {
        left: 0;
        -webkit-transform: rotate(45deg);
            -ms-transform: rotate(45deg);
                transform: rotate(45deg);
        -webkit-transform-origin: 100% 100%;
            -ms-transform-origin: 100% 100%;
                transform-origin: 100% 100%;
    }
    
    .css-times {
        position: absolute;
        width: 100px;
        height: 90px;
    }
    
    .css-times:before,
    .css-times:after {
        position: absolute;
        content: "";
        left: 50px;
        top: 0;
        width: 2px;
        height: 65px;
        background: red;
        border-radius: 50px 50px 0 0;
        -webkit-transform: rotate(-45deg);
            -ms-transform: rotate(-45deg);
                transform: rotate(-45deg);
        -webkit-transform-origin: 0 100%;
            -ms-transform-origin: 0 100%;
                transform-origin: 0 100%;
        -webkit-animation: times-background 1s ease-in-out infinite;
                animation: times-background 1s ease-in-out infinite;
    }
    
    .css-times:after {
        left: 0;
        -webkit-transform: rotate(45deg);
            -ms-transform: rotate(45deg);
                transform: rotate(45deg);
        -webkit-transform-origin: 100% 100%;
            -ms-transform-origin: 100% 100%;
                transform-origin: 100% 100%;
    }
    
    .loader-21 {
        width: 100px;
    }
    
    .loader-21 .times1 {
        -webkit-animation: times-pulse 1s ease-in-out infinite;
                animation: times-pulse 1s ease-in-out infinite;
        left: 0;
    }
    
    .loader-21 .times2 {
        -webkit-animation: times-pulse 1s 0.2s ease-in-out infinite;
                animation: times-pulse 1s 0.2s ease-in-out infinite;
        left: 25px;
    }
    
    .loader-21 .times3 {
        -webkit-animation: times-pulse 1s 0.4s ease-in-out infinite;
                animation: times-pulse 1s 0.4s ease-in-out infinite;
        left: 50px;
    }
    
    .css-flower {
        position: absolute;
        background: green;
        width: 35px;
        height: 35px;
        position: relative;
        text-align: center;
        -webkit-transform: rotate(20deg);
        -ms-transform: rotate(20deg);
            transform: rotate(20deg);
        border-radius: 40%;
        border-top: 4px solid #ababa9;
    }
    
    .css-flower:before {
        content: "";
        position: absolute;
        top: -6px;
        left: 0;
        height: 10px;
        width: 20px;
        background: green;
        -webkit-transform: rotate(135deg);
        -ms-transform: rotate(135deg);
            transform: rotate(135deg);
        border-radius: 10px;
    }
    
    .loader-22 .css-flower {
        position: absolute;
        -webkit-transform: rotate(180deg) scale(0.5);
        -ms-transform: rotate(180deg) scale(0.5);
            transform: rotate(180deg) scale(0.5);
    }
    
    .loader-22 .flower1 {
        left: 0;
        -webkit-animation: caterpillarCrawl 1s ease-out alternate infinite;
                animation: caterpillarCrawl 1s ease-out alternate infinite;
        width: 45px;
        height: 45px;
        top: -10px;
        background: #066c06;
        z-index: 2;
    }
    
    .loader-22 .flower1:before {
        dissplay: none;
    }
    
    .loader-22 .flower2 {
        left: 10px;
        -webkit-transform: rotate(180deg) scale(0.45);
        -ms-transform: rotate(180deg) scale(0.45);
            transform: rotate(180deg) scale(0.45);
        -webkit-animation: caterpillarCrawl 1s 0.1s ease-out alternate infinite;
                animation: caterpillarCrawl 1s 0.1s ease-out alternate infinite;
    }
    
    .loader-22 .flower3 {
        left: 20px;
        -webkit-transform: rotate(180deg) scale(0.4);
        -ms-transform: rotate(180deg) scale(0.4);
            transform: rotate(180deg) scale(0.4);
        -webkit-animation: caterpillarCrawl 1s 0.2s ease-out alternate infinite;
                animation: caterpillarCrawl 1s 0.2s ease-out alternate infinite;
    }
    
    .loader-22 .flower4 {
        left: 30px;
        -webkit-transform: rotate(180deg) scale(0.35);
        -ms-transform: rotate(180deg) scale(0.35);
            transform: rotate(180deg) scale(0.35);
        -webkit-animation: caterpillarCrawl 1s 0.3s ease-out alternate infinite;
                animation: caterpillarCrawl 1s 0.3s ease-out alternate infinite;
    }
    
    .loader-22 .flower5 {
        left: 40px;
        -webkit-transform: rotate(180deg) scale(0.3);
        -ms-transform: rotate(180deg) scale(0.3);
            transform: rotate(180deg) scale(0.3);
        -webkit-animation: caterpillarCrawl 1s 0.4s ease-out alternate infinite;
                animation: caterpillarCrawl 1s 0.4s ease-out alternate infinite;
    }
    
    .loader-22 .flower6 {
        left: 50px;
        -webkit-transform: rotate(180deg) scale(0.25);
        -ms-transform: rotate(180deg) scale(0.25);
            transform: rotate(180deg) scale(0.25);
        -webkit-animation: caterpillarCrawl 1s 0.5s ease-out alternate infinite;
                animation: caterpillarCrawl 1s 0.5s ease-out alternate infinite;
    }
    /* ----------------     KEYFRAMES    ----------------- */
    
    @-webkit-keyframes loader-1-outter {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100% {
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
        }
    }
    
    @keyframes loader-1-outter {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100% {
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
        }
    }
    
    @-webkit-keyframes loader-1-inner {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100% {
            -webkit-transform: rotate(-360deg);
            transform: rotate(-360deg);
        }
    }
    
    @keyframes loader-1-inner {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100% {
            -webkit-transform: rotate(-360deg);
            transform: rotate(-360deg);
        }
    }
    
    @-webkit-keyframes loader-2-circles {
        0% {
            -webkit-box-shadow: 0 0 0 #18ffff;
            box-shadow: 0 0 0 #18ffff;
            opacity: 1;
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        50% {
            -webkit-box-shadow: 24px -22px #18ffff, 30px -15px 0 -3px #18ffff, 31px 0px #18ffff, 29px 9px 0 -3px #18ffff, 24px 23px #18ffff, 17px 30px 0 -3px #18ffff, 0px 33px #18ffff, -10px 28px 0 -3px #18ffff, -24px 22px #18ffff, -29px 14px 0 -3px #18ffff, -31px -3px #18ffff, -30px -11px 0 -3px #18ffff, -20px -25px #18ffff, -12px -30px 0 -3px #18ffff, 5px -29px #18ffff, 13px -25px 0 -3px #18ffff;
            box-shadow: 24px -22px #18ffff, 30px -15px 0 -3px #18ffff, 31px 0px #18ffff, 29px 9px 0 -3px #18ffff, 24px 23px #18ffff, 17px 30px 0 -3px #18ffff, 0px 33px #18ffff, -10px 28px 0 -3px #18ffff, -24px 22px #18ffff, -29px 14px 0 -3px #18ffff, -31px -3px #18ffff, -30px -11px 0 -3px #18ffff, -20px -25px #18ffff, -12px -30px 0 -3px #18ffff, 5px -29px #18ffff, 13px -25px 0 -3px #18ffff;
            -webkit-transform: rotate(180deg);
            transform: rotate(180deg);
        }
        100% {
            opacity: 0;
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
            -webkit-box-shadow: 25px -22px #18ffff, 15px -22px 0 -3px black, 31px 2px #18ffff, 21px 2px 0 -3px black, 23px 25px #18ffff, 13px 25px 0 -3px black, 0px 33px #18ffff, -10px 33px 0 -3px black, -26px 24px #18ffff, -19px 17px 0 -3px black, -32px 0px #18ffff, -23px 0px 0 -3px black, -25px -23px #18ffff, -16px -23px 0 -3px black, 0px -31px #18ffff, -2px -23px 0 -3px black;
            box-shadow: 25px -22px #18ffff, 15px -22px 0 -3px black, 31px 2px #18ffff, 21px 2px 0 -3px black, 23px 25px #18ffff, 13px 25px 0 -3px black, 0px 33px #18ffff, -10px 33px 0 -3px black, -26px 24px #18ffff, -19px 17px 0 -3px black, -32px 0px #18ffff, -23px 0px 0 -3px black, -25px -23px #18ffff, -16px -23px 0 -3px black, 0px -31px #18ffff, -2px -23px 0 -3px black;
        }
    }
    
    @keyframes loader-2-circles {
        0% {
            -webkit-box-shadow: 0 0 0 #18ffff;
            box-shadow: 0 0 0 #18ffff;
            opacity: 1;
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        50% {
            -webkit-box-shadow: 24px -22px #18ffff, 30px -15px 0 -3px #18ffff, 31px 0px #18ffff, 29px 9px 0 -3px #18ffff, 24px 23px #18ffff, 17px 30px 0 -3px #18ffff, 0px 33px #18ffff, -10px 28px 0 -3px #18ffff, -24px 22px #18ffff, -29px 14px 0 -3px #18ffff, -31px -3px #e11a2b, -30px -11px 0 -3px #18ffff, -20px -25px #18ffff, -12px -30px 0 -3px #18ffff, 5px -29px #18ffff, 13px -25px 0 -3px #18ffff;
            box-shadow: 24px -22px #18ffff, 30px -15px 0 -3px #18ffff, 31px 0px #18ffff, 29px 9px 0 -3px #18ffff, 24px 23px #18ffff, 17px 30px 0 -3px #18ffff, 0px 33px #18ffff, -10px 28px 0 -3px #18ffff, -24px 22px #18ffff, -29px 14px 0 -3px #18ffff, -31px -3px #18ffff, -30px -11px 0 -3px #18ffff, -20px -25px #18ffff, -12px -30px 0 -3px #18ffff, 5px -29px #18ffff, 13px -25px 0 -3px #18ffff;
            -webkit-transform: rotate(180deg);
            transform: rotate(180deg);
        }
        100% {
            opacity: 0;
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
            -webkit-box-shadow: 25px -22px #18ffff, 15px -22px 0 -3px black, 31px 2px #18ffff, 21px 2px 0 -3px black, 23px 25px #18ffff, 13px 25px 0 -3px black, 0px 33px #18ffff, -10px 33px 0 -3px black, -26px 24px #18ffff, -19px 17px 0 -3px black, -32px 0px #18ffff, -23px 0px 0 -3px black, -25px -23px #18ffff, -16px -23px 0 -3px black, 0px -31px #18ffff, -2px -23px 0 -3px black;
            box-shadow: 25px -22px #18ffff, 15px -22px 0 -3px black, 31px 2px #18ffff, 21px 2px 0 -3px black, 23px 25px #18ffff, 13px 25px 0 -3px black, 0px 33px #18ffff, -10px 33px 0 -3px black, -26px 24px #18ffff, -19px 17px 0 -3px black, -32px 0px #18ffff, -23px 0px 0 -3px black, -25px -23px #18ffff, -16px -23px 0 -3px black, 0px -31px #18ffff, -2px -23px 0 -3px black;
        }
    }
    
    @-webkit-keyframes loader-2-star {
        0% {
            -webkit-transform: scale(0) rotate(0deg);
            transform: scale(0) rotate(0deg);
        }
        100% {
            -webkit-transform: scale(0.7) rotate(360deg);
            transform: scale(0.7) rotate(360deg);
        }
    }
    
    @keyframes loader-2-star {
        0% {
            -webkit-transform: scale(0) rotate(0deg);
            transform: scale(0) rotate(0deg);
        }
        100% {
            -webkit-transform: scale(0.7) rotate(360deg);
            transform: scale(0.7) rotate(360deg);
        }
    }
    
    @-webkit-keyframes dot-jump {
        0% {
            -webkit-transform: translateY(0);
            transform: translateY(0);
        }
        100% {
            -webkit-transform: translateY(-15px);
            transform: translateY(-15px);
        }
    }
    
    @keyframes dot-jump {
        0% {
            -webkit-transform: translateY(0);
            transform: translateY(0);
        }
        100% {
            -webkit-transform: translateY(-15px);
            transform: translateY(-15px);
        }
    }
    
    @-webkit-keyframes ball-turn {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100% {
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
        }
    }
    
    @keyframes ball-turn {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100% {
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
        }
    }
    
    @-webkit-keyframes dotted-spin {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100% {
            -webkit-transform: rotate(-360deg);
            transform: rotate(-360deg);
        }
    }
    
    @keyframes dotted-spin {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100% {
            -webkit-transform: rotate(-360deg);
            transform: rotate(-360deg);
        }
    }
    
    @-webkit-keyframes hike {
        0% {
            -webkit-transform: translate(0);
            transform: translate(0);
        }
        25% {
            -webkit-transform: translate(20px, -20px);
            transform: translate(20px, -20px);
        }
        50% {
            -webkit-transform: translate(40px, 0px);
            transform: translate(40px, 0px);
        }
        75% {
            -webkit-transform: translate(60px, -20px);
            transform: translate(60px, -20px);
        }
        100% {
            -webkit-transform: translate(80px, 0px);
            transform: translate(80px, 0px);
        }
    }
    
    @keyframes hike {
        0% {
            -webkit-transform: translate(0);
            transform: translate(0);
        }
        25% {
            -webkit-transform: translate(20px, -20px);
            transform: translate(20px, -20px);
        }
        50% {
            -webkit-transform: translate(40px, 0px);
            transform: translate(40px, 0px);
        }
        75% {
            -webkit-transform: translate(60px, -20px);
            transform: translate(60px, -20px);
        }
        100% {
            -webkit-transform: translate(80px, 0px);
            transform: translate(80px, 0px);
        }
    }
    
    @-webkit-keyframes border-zoom {
        0% {
            border-width: 0px;
        }
        100% {
            border-width: 10px;
        }
    }
    
    @keyframes border-zoom {
        0% {
            border-width: 0px;
        }
        100% {
            border-width: 10px;
        }
    }
    /*@-webkit-keyframes line-grow {
  0% {
    height: 0;
  }
  100% {
    height: 75%;
  }
}*/
    
    @-webkit-keyframes line-grow {
        0% {
            height: 0;
        }
        100% {
            height: 75%;
        }
    }
    
    @keyframes line-grow {
        0% {
            height: 0;
        }
        100% {
            height: 75%;
        }
    }
    
    @-webkit-keyframes star-jump {
        0% {
            -webkit-transform: translateY(0) scale(0.7);
            transform: translateY(0) scale(0.7);
        }
        100% {
            -webkit-transform: translateY(-15px) scale(1);
            transform: translateY(-15px) scale(1);
        }
    }
    
    @keyframes star-jump {
        0% {
            -webkit-transform: translateY(0) scale(0.7);
            transform: translateY(0) scale(0.7);
        }
        100% {
            -webkit-transform: translateY(-15px) scale(1);
            transform: translateY(-15px) scale(1);
        }
    }
    
    @-webkit-keyframes stars-pulse {
        0%,
        100% {
            -webkit-transform: scale(1);
            transform: scale(1);
            opacity: 1;
        }
        80% {
            -webkit-transform: scale(0);
            transform: scale(0);
            opacity: 0;
        }
    }
    
    @keyframes stars-pulse {
        0%,
        100% {
            -webkit-transform: scale(1);
            transform: scale(1);
            opacity: 1;
        }
        80% {
            -webkit-transform: scale(0);
            transform: scale(0);
            opacity: 0;
        }
    }
    
    @-webkit-keyframes times-pulse {
        0%,
        100% {
            -webkit-transform: scale(1);
            transform: scale(1);
            opacity: 1;
        }
        60% {
            -webkit-transform: scale(0);
            transform: scale(0);
            opacity: 0;
        }
    }
    
    @keyframes times-pulse {
        0%,
        100% {
            -webkit-transform: scale(1);
            transform: scale(1);
            opacity: 1;
        }
        60% {
            -webkit-transform: scale(0);
            transform: scale(0);
            opacity: 0;
        }
    }
    
    @-webkit-keyframes times-background {
        0%,
        100% {
            background: blueviolet;
        }
        60% {
            background: #ff3d00;
        }
    }
    
    @keyframes times-background {
        0%,
        100% {
            background: blueviolet;
        }
        60% {
            background: #ff3d00;
        }
    }
    
    @-webkit-keyframes star-pulse {
        0%,
        100% {
            -webkit-transform: scale(0) rotate(0deg);
            transform: scale(0) rotate(0deg);
            opacity: 0.5;
        }
        25% {
            -webkit-transform: scale(1) rotate(0deg);
            transform: scale(1) rotate(0deg);
        }
        50% {
            -webkit-transform: scale(2) rotate(0deg);
            transform: scale(2) rotate(0deg);
            opacity: 1;
        }
        75% {
            -webkit-transform: scale(1.5) rotate(90deg);
            transform: scale(1.5) rotate(90deg);
        }
    }
    
    @keyframes star-pulse {
        0%,
        100% {
            -webkit-transform: scale(0) rotate(0deg);
            transform: scale(0) rotate(0deg);
            opacity: 0.5;
        }
        25% {
            -webkit-transform: scale(1) rotate(0deg);
            transform: scale(1) rotate(0deg);
        }
        50% {
            -webkit-transform: scale(2) rotate(0deg);
            transform: scale(2) rotate(0deg);
            opacity: 1;
        }
        75% {
            -webkit-transform: scale(1.5) rotate(90deg);
            transform: scale(1.5) rotate(90deg);
        }
    }
    
    @-webkit-keyframes stars-rotate {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        25% {
            -webkit-transform: rotate(-90deg);
            transform: rotate(-90deg);
        }
        50% {
            -webkit-transform: rotate(-180deg);
            transform: rotate(-180deg);
        }
        75% {
            -webkit-transform: rotate(-270deg);
            transform: rotate(-270deg);
        }
        100% {
            -webkit-transform: rotate(-360deg);
            transform: rotate(-360deg);
        }
    }
    
    @keyframes stars-rotate {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        25% {
            -webkit-transform: rotate(-90deg);
            transform: rotate(-90deg);
        }
        50% {
            -webkit-transform: rotate(-180deg);
            transform: rotate(-180deg);
        }
        75% {
            -webkit-transform: rotate(-270deg);
            transform: rotate(-270deg);
        }
        100% {
            -webkit-transform: rotate(-360deg);
            transform: rotate(-360deg);
        }
    }
    
    @-webkit-keyframes stars-rotate-reverse {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100% {
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
        }
    }
    
    @keyframes stars-rotate-reverse {
        0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        100% {
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
        }
    }
    
    @-webkit-keyframes stars-catch {
        0% {}
        25% {}
        50% {}
        75% {
            top: -2px;
            right: -11px;
            opacity: 0;
        }
        100% {}
    }
    
    @keyframes stars-catch {
        0% {}
        25% {}
        50% {}
        75% {
            top: -2px;
            right: -11px;
            opacity: 0;
        }
        100% {}
    }
    
    @-webkit-keyframes star-fly-out {
        0% {
            top: 19px;
            left: 19px;
        }
        100% {}
    }
    
    @keyframes star-fly-out {
        0% {
            top: 19px;
            left: 19px;
        }
        100% {}
    }
    
    @-webkit-keyframes star-cube {
        0%,
        100% {
            -webkit-transform: translate(0px, 0);
            transform: translate(0px, 0);
        }
        {}
        25% {
            -webkit-transform: translate(60px);
            transform: translate(60px);
        }
        50% {
            -webkit-transform: translate(60px, 60px);
            transform: translate(60px, 60px);
        }
        75% {
            -webkit-transform: translate(0px, 60px);
            transform: translate(0px, 60px);
        }
    }
    
    @keyframes star-cube {
        0%,
        100% {
            -webkit-transform: translate(0px, 0);
            transform: translate(0px, 0);
        }
        {}
        25% {
            -webkit-transform: translate(60px);
            transform: translate(60px);
        }
        50% {
            -webkit-transform: translate(60px, 60px);
            transform: translate(60px, 60px);
        }
        75% {
            -webkit-transform: translate(0px, 60px);
            transform: translate(0px, 60px);
        }
    }
    
    @-webkit-keyframes star-big-pulse {
        0% {
            -webkit-transform: scale(0);
            transform: scale(0);
            opacity: 1;
        }
        100% {
            -webkit-transform: scale(5);
            transform: scale(5);
            opacity: 0;
        }
    }
    
    @keyframes star-big-pulse {
        0% {
            -webkit-transform: scale(0);
            transform: scale(0);
            opacity: 1;
        }
        100% {
            -webkit-transform: scale(5);
            transform: scale(5);
            opacity: 0;
        }
    }
    
    @-webkit-keyframes star-small-pulse {
        0% {
            -webkit-transform: scale(1);
            transform: scale(1);
        }
        100% {
            -webkit-transform: scale(2);
            transform: scale(2);
        }
    }
    
    @keyframes star-small-pulse {
        0% {
            -webkit-transform: scale(1);
            transform: scale(1);
        }
        100% {
            -webkit-transform: scale(2);
            transform: scale(2);
        }
    }
    
    @-webkit-keyframes star-flicker {
        0% {
            -webkit-transform: rotate(180deg) scale(0.35);
            transform: rotate(180deg) scale(0.35);
        }
        50% {
            -webkit-transform: rotate(180deg) scale(0.1);
            transform: rotate(180deg) scale(0.1);
        }
        100% {
            -webkit-transform: rotate(180deg) scale(0.35);
            transform: rotate(180deg) scale(0.35);
        }
    }
    
    @keyframes star-flicker {
        0% {
            -webkit-transform: rotate(180deg) scale(0.35);
            transform: rotate(180deg) scale(0.35);
        }
        50% {
            -webkit-transform: rotate(180deg) scale(0.1);
            transform: rotate(180deg) scale(0.1);
        }
        100% {
            -webkit-transform: rotate(180deg) scale(0.35);
            transform: rotate(180deg) scale(0.35);
        }
    }
    
    @-webkit-keyframes star-catcher {
        0% {
            opacity: 0.5;
        }
        /*12.5% { opacity: 1;  }*/
        25% {
            opacity: 0.5;
        }
        /*  37.5% {  opacity: 1;  }*/
        50% {
            opacity: 0.5;
        }
        /*  62.5% {opacity: 1;}*/
        75% {
            opacity: 0.5;
        }
        80% {
            opacity: 1;
        }
        100% {
            opacity: 0.5;
        }
    }
    
    @keyframes star-catcher {
        0% {
            opacity: 0.5;
        }
        25% {
            opacity: 0.5;
        }
        50% {
            opacity: 0.5;
        }
        75% {
            opacity: 0.5;
        }
        80% {
            opacity: 1;
        }
        100% {
            opacity: 0.5;
        }
    }
    

 @-webkit-keyframes dominos {
  50% { opacity: 0.7; }
  75% { -webkit-transform: rotate(90deg); transform: rotate(90deg); }
  80% { opacity: 1; } 
 }
    

 @keyframes dominos {
  50% { opacity: 0.7; }
  75% { -webkit-transform: rotate(90deg); transform: rotate(90deg); }
  80% { opacity: 1; } 
 }


    @-webkit-keyframes star-crazyness {
        0% {
            opacity: 0.4;
            -webkit-transform: rotate(180deg) translate(0px, 0) scale(0.6);
            transform: rotate(180deg) translate(0px, 0) scale(0.6);
        }
        25% {
            opacity: 0.4;
            -webkit-transform: rotate(180deg) translate(0, 0) scale(0.2);
            transform: rotate(180deg) translate(0, 0) scale(0.2);
        }
        50% {
            opacity: 0.7;
            -webkit-transform: rotate(180deg) translate(5px, 5px) scale(0.4);
            transform: rotate(180deg) translate(5px, 5px) scale(0.4);
        }
        75% {
            opacity: 0.4;
            -webkit-transform: rotate(180deg) translate(0, 0) scale(0.6);
            transform: rotate(180deg) translate(0, 0) scale(0.6);
        }
        80% {
            opacity: 1;
            -webkit-transform: rotate(180deg) translate(5px, 0) scale(0.1);
            transform: rotate(180deg) translate(5px, 0) scale(0.1);
        }
        100% {
            opacity: 0.4;
            -webkit-transform: rotate(180deg) translate(0, 0) scale(0.6);
            transform: rotate(180deg) translate(0, 0) scale(0.6);
        }
    }
    
    @keyframes star-crazyness {
        0% {
            opacity: 0.4;
            -webkit-transform: rotate(180deg) translate(0px, 0) scale(0.6);
            transform: rotate(180deg) translate(0px, 0) scale(0.6);
        }
        25% {
            opacity: 0.4;
            -webkit-transform: rotate(180deg) translate(0, 0) scale(0.2);
            transform: rotate(180deg) translate(0, 0) scale(0.2);
        }
        50% {
            opacity: 0.7;
            -webkit-transform: rotate(180deg) translate(5px, 5px) scale(0.4);
            transform: rotate(180deg) translate(5px, 5px) scale(0.4);
        }
        75% {
            opacity: 0.4;
            -webkit-transform: rotate(180deg) translate(0, 0) scale(0.6);
            transform: rotate(180deg) translate(0, 0) scale(0.6);
        }
        80% {
            opacity: 1;
            -webkit-transform: rotate(180deg) translate(5px, 0) scale(0.1);
            transform: rotate(180deg) translate(5px, 0) scale(0.1);
        }
        100% {
            opacity: 0.4;
            -webkit-transform: rotate(180deg) translate(0, 0) scale(0.6);
            transform: rotate(180deg) translate(0, 0) scale(0.6);
        }
    }
    
    @-webkit-keyframes star-crawl {
        0% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.2);
            transform: rotate(180deg) translateY(0) scale(0.2);
        }
        20% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.3);
            transform: rotate(180deg) translateY(0) scale(0.3);
        }
        40% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.4);
            transform: rotate(180deg) translateY(0) scale(0.4);
        }
        60% {
            -webkit-transform: rotate(90deg) translateY(0) scale(0.4);
            transform: rotate(90deg) translateY(0) scale(0.4);
        }
        80% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.4);
            transform: rotate(180deg) translateY(0) scale(0.4);
        }
        100% {
            -webkit-transform: rotate(180deg) translateY(25px) scale(0.2);
            transform: rotate(180deg) translateY(25px) scale(0.2);
        }
    }
    
    @keyframes star-crawl {
        0% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.2);
            transform: rotate(180deg) translateY(0) scale(0.2);
        }
        20% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.3);
            transform: rotate(180deg) translateY(0) scale(0.3);
        }
        40% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.4);
            transform: rotate(180deg) translateY(0) scale(0.4);
        }
        60% {
            -webkit-transform: rotate(90deg) translateY(0) scale(0.4);
            transform: rotate(90deg) translateY(0) scale(0.4);
        }
        80% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.4);
            transform: rotate(180deg) translateY(0) scale(0.4);
        }
        100% {
            -webkit-transform: rotate(180deg) translateY(25px) scale(0.2);
            transform: rotate(180deg) translateY(25px) scale(0.2);
        }
    }
    
    @-webkit-keyframes caterpillarCrawl {
        0% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.2);
            transform: rotate(180deg) translateY(0) scale(0.3);
        }
        20% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.3);
            transform: rotate(180deg) translateY(0) scale(0.4);
        }
        40% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.4);
            transform: rotate(180deg) translateY(0) scale(0.5);
        }
        60% {
            -webkit-transform: rotate(90deg) translateY(0) scale(0.4);
            transform: rotate(90deg) translateY(0) scale(0.5);
        }
        80% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.4);
            transform: rotate(180deg) translateY(0) scale(0.5);
        }
        100% {
            -webkit-transform: rotate(180deg) translateY(25px) scale(0.2);
            transform: rotate(180deg) translateY(25px) scale(0.3);
        }
    }
    
    @keyframes caterpillarCrawl {
        0% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.2);
            transform: rotate(180deg) translateY(0) scale(0.3);
        }
        20% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.3);
            transform: rotate(180deg) translateY(0) scale(0.4);
        }
        40% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.4);
            transform: rotate(180deg) translateY(0) scale(0.5);
        }
        60% {
            -webkit-transform: rotate(90deg) translateY(0) scale(0.4);
            transform: rotate(90deg) translateY(0) scale(0.5);
        }
        80% {
            -webkit-transform: rotate(180deg) translateY(0) scale(0.4);
            transform: rotate(180deg) translateY(0) scale(0.5);
        }
        100% {
            -webkit-transform: rotate(180deg) translateY(25px) scale(0.2);
            transform: rotate(180deg) translateY(25px) scale(0.3);
        }
    }
</style>
"""

def point_line(**kargs):
    outer_style = """
        <style>
        .parent {
        display: flex;
        justify-content: center;
        text-align: center;
        width: 100%;
        height: ||-height-||;
        z-index: 999;
        }          
        .container {
            text-align: center;
            z-index: 999;
        }
        section {
            width: 30%;
            display: inline-block;
            text-align: center;
            min-height: 215px;
            vertical-align: top;
            margin: 1%;
            background: #ccccc;
            border-radius: 5px;
            -webkit-box-shadow: 0px 0px 30px 1px #103136 inset;
                    box-shadow: 0px 0px 30px 1px #103136 inset;
        }
        </style>
    """

    point_line_style = """
    <style>
        .lds-ellipsis {
        display: inline-block;
        position: absolute;
        width: 80%;
        height: 100%;
        top: 30%;
        }
        .lds-ellipsis div {
        display: inline-block;
        position: absolute;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: ||-pcolor-||;
        animation-timing-function: cubic-bezier(0, 1, 1, 0);
        }
        .lds-ellipsis div:nth-child(1) {
        left: 0%;
        animation: lds-ellipsis1 0.4s infinite;
        }
        .lds-ellipsis div:nth-child(2) {
        left: 5%;
        animation: lds-ellipsis2 0.5s infinite;
        }
        .lds-ellipsis div:nth-child(3) {
        left: 15%;
        animation: lds-ellipsis2 0.5s infinite;
        }
        .lds-ellipsis div:nth-child(4) {
        left: 25%;
        animation: lds-ellipsis2 0.5s infinite;
        }
        .lds-ellipsis div:nth-child(5) {
        left: 35%;
        animation: lds-ellipsis2 0.5s infinite;
        }
        .lds-ellipsis div:nth-child(6) {
        left: 45%;
        animation: lds-ellipsis2 0.5s infinite;
        }
        .lds-ellipsis div:nth-child(7) {
        left: 55%;
        animation: lds-ellipsis2 0.5s infinite;
        }
        .lds-ellipsis div:nth-child(8) {
        left: 65%;
        animation: lds-ellipsis2 0.5s infinite;
        }
        .lds-ellipsis div:nth-child(9) {
        left: 75%;
        animation: lds-ellipsis2 0.5s infinite;
        }
        .lds-ellipsis div:nth-child(10) {
        left: 85%;
        animation: lds-ellipsis2 0.5s infinite;
        }
        .lds-ellipsis div:nth-child(11) {
        left: 95%;
        animation: lds-ellipsis2 0.5s infinite;
        }
        .lds-ellipsis div:nth-child(12) {
        left: 100%;
        animation: lds-ellipsis3 0.4s infinite;
        }
        @keyframes lds-ellipsis1 {
        0% {
            transform: scale(0);
        }
        100% {
            transform: scale(1);
        }
        }
        @keyframes lds-ellipsis3 {
        0% {
            transform: scale(1);
        }
        100% {
            transform: scale(0);
        }
        }
        @keyframes lds-ellipsis2 {
        0% {
            transform: translate(0, 0);
        }
        25%,50%,75%, 100% {
            transform: translate(50px, 0);
        }
        }
    """

    point_lines = """
        <div class="parent">
            <h1>||-label-||</h1><br>
                <div class="lds-ellipsis">
                    <div></div>
                    <div></div>
                    <div></div>
                    <div></div>
                    <div></div>
                    <div></div>
                    <div></div>
                    <div></div>
                    <div></div>
                    <div></div>
                    <div></div>
                    <div></div>
                </div>
        </div>
    """

    return point_lines,point_line_style

def grid_points(**kargs):
    outer_style = """
        <style>
        .parent {
        display: flex;
        justify-content: center;
        text-align: center;
        position: relative;
        width: 100%;
        height: ||-height-||;
        z-index: 999;
        }           
        .container {
            text-align: center;
            z-index: 999;
        }
        section {
            width: 30%;
            display: inline-block;
            text-align: center;
            min-height: 215px;
            vertical-align: top;
            margin: 1%;
            background: #ccccc;
            border-radius: 5px;
            -webkit-box-shadow: 0px 0px 30px 1px #103136 inset;
                    box-shadow: 0px 0px 30px 1px #103136 inset;
        }
        </style>
    """

    spotted_div_style = """
        <style>
        .lds-grid {
        display: inline-block;
        position: absolute;
        width: 100%;
        height: 100%;
        top: 20%;
        }
        .lds-grid div {
        display: inline-block;
        position: absolute;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: ||-pcolor-||;
        animation: lds-grid 1.2s linear infinite;
        }
        .lds-grid div:nth-child(1) {
        top: 20%;
        left: 20%;
        animation-delay: 0s;
        }
        .lds-grid div:nth-child(2) {
        top: 20%;
        left: 50%;
        animation-delay: -0.4s;
        }
        .lds-grid div:nth-child(3) {
        top: 20%;
        left: 80%;
        animation-delay: -0.8s;
        }
        .lds-grid div:nth-child(4) {
        top: 50%;
        left: 20%;
        animation-delay: -0.4s;
        }
        .lds-grid div:nth-child(5) {
        top: 50%;
        left: 50%;
        animation-delay: -0.8s;
        }
        .lds-grid div:nth-child(6) {
        top: 50%;
        left: 80%;
        animation-delay: -1.2s;
        }
        .lds-grid div:nth-child(7) {
        top: 80%;
        left: 20%;
        animation-delay: -0.8s;
        }
        .lds-grid div:nth-child(8) {
        top: 80%;
        left: 50%;
        animation-delay: -1.2s;
        }
        .lds-grid div:nth-child(9) {
        top: 80%;
        left: 80%;
        animation-delay: -1.6s;
        }
        @keyframes lds-grid {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.2;
        }
        }
        </style>
        """

    spotted_div = """
        <div class="parent">
            <h1>||-label-||</h1><br>
            <div class="lds-grid">
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div>
        """

    return spotted_div, spotted_div_style

def pulse_bars(**kargs):
    outer_style = """
        <style>
        .labelbox {
        display: inline-block;
        justify-content: center;
        position: relative;
        width: 100%;
        height: ||-height-||;
        z-index: 92;
        }
        .parent {
        display: flex;
        justify-content: center;
        position: absolute;
        width: 80%;
        top: 25%;
        left: 10%;
        height: ||-height-||;
        z-index: 90;
        }          
        .container {
            text-align: center;
            z-index: 999;
        }
        section {
            width: 30%;
            display: inline-block;
            text-align: center;
            min-height: 215px;
            vertical-align: top;
            margin: 1%;
            background: #ccccc;
            border-radius: 5px;
            -webkit-box-shadow: 0px 0px 30px 1px #103136 inset;
                    box-shadow: 0px 0px 30px 1px #103136 inset;
        }
        </style>
    """

    spinner_div_style = """
        <style>
        .lds-facebook div {
        justify-content: center;
        position: absolute;
        left: 50%;
        height: 80%;
        width: 5%;
        background: ||-pcolor-||;
        animation: lds-facebook 1.2s cubic-bezier(0, 0.5, 0.5, 1) infinite;
        }
        .lds-facebook div:nth-child(1) {
        left: 5%;
        animation-delay: -0.24s;
        }
        .lds-facebook div:nth-child(2) {
        left: 20%;
        animation-delay: -0.12s;
        }
        .lds-facebook div:nth-child(3) {
        left: 35%;
        animation-delay: 0;
        }
        .lds-facebook div:nth-child(4) {
        left: 50%;
        animation-delay: -0.24s;
        }
        .lds-facebook div:nth-child(5) {
        left: 65%;
        animation-delay: -0.12s;
        }
        .lds-facebook div:nth-child(6) {
        left: 80%;
        animation-delay: 0;
        }
        .lds-facebook div:nth-child(7) {
        left: 95%;
        animation-delay: 0;
        }
        @keyframes lds-facebook {
        0% {
            top: 20%;
            height: 90%;
        }
        25%, 75% {
            top: 10%;
            height: 50%;
        }
        50%, 100% {
            top: 20%;
            height: 20%;
        }
        }
        </style>
        """

    spinner_div = """
        <div class="labelbox"><h1>||-label-||</h1><br></div>
        <div class="parent">
            <div class="lds-facebook">
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div>
        """
    return spinner_div,spinner_div_style

def pacman_loader(**kargs):
    pacman_style = """
        <style type="text/css">
        .labelbox {
        display: flex;
        justify-content: center;
        position: absolute;
        width: 100%;
        height: ||-height-||;
        z-index: 90;
        }
        .parent {
        display: flex;
        justify-content: center;
        position: absolute;
        width: 80%;
        top: 25%;
        left: 40%;
        height: ||-height-||;
        z-index: 90;
        }         
        .container {
            text-align: center;
            z-index: 999;
        }
        @keyframes ldio-2h0ei997e6j-1 {
            0% { transform: rotate(0deg) }
        50% { transform: rotate(-45deg) }
        100% { transform: rotate(0deg) }
        }
        @keyframes ldio-2h0ei997e6j-2 {
            0% { transform: rotate(180deg) }
        50% { transform: rotate(225deg) }
        100% { transform: rotate(180deg) }
        }
        .ldio-2h0ei997e6j > div:nth-child(2) {
        transform: translate(-15px,0);
        }
        .ldio-2h0ei997e6j > div:nth-child(2) div {
        position: absolute;
        top: 90.8px;
        left: 20.8px;
        width: 272.4px;
        height: 136.2px;
        border-radius: 272.4px 272.4px 0 0;
        background: ||-pcolor-||;
        animation: ldio-2h0ei997e6j-1 1s linear infinite;
        transform-origin: 136.2px 136.2px
        }
        .ldio-2h0ei997e6j > div:nth-child(2) div:nth-child(2) {
        animation: ldio-2h0ei997e6j-2 1s linear infinite
        }
        .ldio-2h0ei997e6j > div:nth-child(2) div:nth-child(3) {
        transform: rotate(-90deg);
        animation: none;
        }@keyframes ldio-2h0ei997e6j-3 {
            0% { transform: translate(431.3px,0); opacity: 0 }
        20% { opacity: 1 }
        100% { transform: translate(158.9px,0); opacity: 1 }
        }
        .ldio-2h0ei997e6j > div:nth-child(1) {
        display: block;
        }
        .ldio-eye {
        position: absolute;
        top: 120.84px;
        left: 160.16px;
        width: 36.32px;
        height: 36.32px;
        border-radius: 50%;
        background: #000000;
        z-index:990;
        }
        .ldio-eye-outer {
        position: absolute;
        top: 137.84px;
        left: 180px;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #F0F2F6;
        z-index:991;
        }
        .ldio-2h0ei997e6j > div:nth-child(1) div {
        position: absolute;
        top: 208.84px;
        left: -18.16px;
        width: 36.32px;
        height: 36.32px;
        border-radius: 50%;
        background: #F0F2F6;
        animation: ldio-2h0ei997e6j-3 1s linear infinite
        }
        .ldio-2h0ei997e6j > div:nth-child(1) div:nth-child(1) { animation-delay: -0.67s }
        .ldio-2h0ei997e6j > div:nth-child(1) div:nth-child(2) { animation-delay: -0.33s }
        .ldio-2h0ei997e6j > div:nth-child(1) div:nth-child(3) { animation-delay: 0s }
        .loadingio-spinner-bean-eater-8cann0gbu3e {
        width: 100%;
        height: 200%;
        display: inline-block;
        overflow: hidden;
        background: none;
        }
        .ldio-2h0ei997e6j {
        width: 100%;
        height: 100%;
        position: relative;
        transform: translateZ(0) scale(1);
        backface-visibility: hidden;
        transform-origin: 0 0; /* see note above */
        }
        .ldio-2h0ei997e6j div { box-sizing: content-box; }
        </style>
    """

    pacman = """
        <div class="labelbox"><h1>||-label-||</h1><br></div>
        <div class="parent">
            <div class="ldio-eye"></div><div class="ldio-eye-outer"></div>
            <div class="loadingio-spinner-bean-eater-8cann0gbu3e">
                <div class="ldio-2h0ei997e6j">
                    <div>
                        <div></div>
                        <div></div>
                        <div></div>
                        </div><div>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                </div>
            </div>
        </div>
    """

    return pacman,pacman_style

#template function for spinners and loaders
# def tester():
#     element_code = """
        # <div class="parent">


        # </div>
    
#     """

#     element_style = """
        # <style>
        #         .parent {
        #         display: flex;
        #         justify-content: center;
        #         text-align: center;
        #         width: 100%;
        #         height: ||-height-||;
        #         }



        # </style>
#     """

#     return element_code,element_style



def showcase(**kargs):
    element_code = """
        <div class="parent">
            <div class="container">
            <section>
                <div class="loader loader-1">
                <div class="loader-outter"></div>
                <div class="loader-inner"></div>
                </div>
            </section>
            <section>
                <div class="loader loader-2">
                <svg class="loader-star" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
                        <polygon points="29.8 0.3 22.8 21.8 0 21.8 18.5 35.2 11.5 56.7 29.8 43.4 48.2 56.7 41.2 35.1 59.6 21.8 36.8 21.8 " fill="#18ffff" />
                    </svg>
                <div class="loader-circles"></div>
                </div>
            </section>
            <section>
                <div class="loader loader-21">
                <div class="css-times times1"></div>
                <div class="css-times times2"></div>
                <div class="css-times times3"></div>
                </div>
            </section>
            <section>
                <div class="loader loader-7">
                <div class="line line1"></div>
                <div class="line line2"></div>
                <div class="line line3"></div>
                </div>
            </section>
            <section>
                <div class="loader loader-18">
                <div class="css-star star1"></div>
                <div class="css-star star2"></div>
                <div class="css-star star3"></div>
                <div class="css-star star4"></div>
                <div class="css-star star5"></div>
                <div class="css-star star6"></div>
                <div class="css-star star7"></div>
                <div class="css-star star8"></div>
                </div>
            </section>
            <section>
                <div class="loader loader-5">
                <div class="loader-pacman"></div>
                </div>
            </section>
            <section>
                <div class="loader loader-4"></div>
            </section>
            <section>
                <div class="loader loader-17">
                <div class="css-square square1"></div>
                <div class="css-square square2"></div>
                <div class="css-square square3"></div>
                <div class="css-square square4"></div>
                <div class="css-square square5"></div>
                <div class="css-square square6"></div>
                <div class="css-square square7"></div>
                <div class="css-square square8"></div>
                </div>
            </section>
            <section>
                <div class="loader loader-12">
                <svg class="loader-star star1" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
                    </svg>
                <svg class="loader-star star2" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
                    </svg>
                <svg class="loader-star star3" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
                    </svg>
                <svg class="loader-star star4" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
                    </svg>
                <svg class="loader-star star5" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
                    </svg>
                <svg class="loader-star star6" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
                    </svg>
                </div>
            </section>
            <section>
                <div class="loader loader-6">
                <div class="loader-inner"></div>
                </div>
            </section>
            <section>
                <div class="loader loader-14">
                <svg class="loader-star star-small" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="23.172px" height="23.346px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon fill="#01579b" points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9  "></polygon>
                    </svg>
                <svg class="loader-star star-big" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="23.172px" height="23.346px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon fill="#40c4ff" points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9  "></polygon>
                    </svg>
                </div>
            </section>
            <section>
                <div class="loader loader-3">
                <div class="dot dot1"></div>
                <div class="dot dot2"></div>
                <div class="dot dot3"></div>
                </div>
            </section>
            <section>
                <div class="loader loader-9">
                <svg class="loader-star star1" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="23.172px" height="23.346px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon fill="#c6ff00" points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
                    </svg>
                <svg class="loader-star star2" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="23.172px" height="23.346px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon fill="#c6ff00" points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9  " />
                    </svg>
                <svg class="loader-star star3" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="23.172px" height="23.346px" viewBox="0 0 23.172 23.346" xml:space="preserve">
                        <polygon fill="#c6ff00" points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9  " />
                    </svg>
                </div>
            </section>
            <section>
                <div class="loader loader-20">
                <div class="css-diamond"></div>
                </div>
            </section>
            <section>
                <div class="loader loader-13">
                <div class="css-heart heart1"></div>
                <div class="css-heart heart2"></div>
                <div class="css-heart heart3"></div>
                <div class="css-heart heart4"></div>
                </div>
            </section>
            </div>
        </div>
    """

    element_style = SHOWCASE_GLOBAL_STYLES


    return element_code,element_style

def pretty_loaders(index=0):

    sub_loaders = [
"""
<div class="loader loader-1">
<div class="loader-outter"></div>
<div class="loader-inner"></div>
</div>
""","""
<div class="loader loader-2">
<svg class="loader-star" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
<polygon points="29.8 0.3 22.8 21.8 0 21.8 18.5 35.2 11.5 56.7 29.8 43.4 48.2 56.7 41.2 35.1 59.6 21.8 36.8 21.8 " fill="#18ffff" />
</svg>
<div class="loader-circles"></div>
</div>
""","""
<div class="loader loader-21">
<div class="css-times times1"></div>
<div class="css-times times2"></div>
<div class="css-times times3"></div>
</div>
""","""
<div class="loader loader-7">
<div class="line line1"></div>
<div class="line line2"></div>
<div class="line line3"></div>
</div>
""","""
<div class="loader loader-18">
<div class="css-star star1"></div>
<div class="css-star star2"></div>
<div class="css-star star3"></div>
<div class="css-star star4"></div>
<div class="css-star star5"></div>
<div class="css-star star6"></div>
<div class="css-star star7"></div>
<div class="css-star star8"></div>
</div>
""","""
<div class="loader loader-5">
<div class="loader-pacman"></div>
</div>
""","""
<div class="loader loader-4"></div>
""","""
<div class="loader loader-17">
<div class="css-square square1"></div>
<div class="css-square square2"></div>
<div class="css-square square3"></div>
<div class="css-square square4"></div>
<div class="css-square square5"></div>
<div class="css-square square6"></div>
<div class="css-square square7"></div>
<div class="css-square square8"></div>
</div>
""","""
<div class="loader loader-12">
<svg class="loader-star star1" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
</svg>
<svg class="loader-star star2" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
</svg>
<svg class="loader-star star3" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
</svg>
<svg class="loader-star star4" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
</svg>
<svg class="loader-star star5" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
</svg>
<svg class="loader-star star6" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="35px" height="35px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
</svg>
</div>
""","""
<div class="loader loader-6">
<div class="loader-inner"></div>
</div>
""","""
<div class="loader loader-14">
<svg class="loader-star star-small" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="23.172px" height="23.346px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon fill="#01579b" points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9  "></polygon>
</svg>
<svg class="loader-star star-big" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="23.172px" height="23.346px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon fill="#40c4ff" points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9  "></polygon>
</svg>
</div>
""","""
<div class="loader loader-3">
<div class="dot dot1"></div>
<div class="dot dot2"></div>
<div class="dot dot3"></div>
</div>
""","""
<div class="loader loader-9">
<svg class="loader-star star1" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="23.172px" height="23.346px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon fill="#c6ff00" points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9" />
</svg>
<svg class="loader-star star2" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="23.172px" height="23.346px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon fill="#c6ff00" points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9  " />
</svg>
<svg class="loader-star star3" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="23.172px" height="23.346px" viewBox="0 0 23.172 23.346" xml:space="preserve">
<polygon fill="#c6ff00" points="11.586,0 8.864,8.9 0,8.9 7.193,14.447 4.471,23.346 11.586,17.84 18.739,23.346 16.77,14.985 23.172,8.9 14.306,8.9  " />
</svg>
</div>
""","""
<div class="loader loader-20">
<div class="css-diamond"></div>
</div>
""","""
<div class="loader loader-13">
<div class="css-heart heart1"></div>
<div class="css-heart heart2"></div>
<div class="css-heart heart3"></div>
<div class="css-heart heart4"></div>
</div>
"""]

    l = len(sub_loaders)

    if hasattr(index,'__iter__'):
        group_loaders = "".join([f"""{sub_loaders[i%l]}""" for i in index])
    else:
        group_loaders = sub_loaders[index%l]

    element_code = f"""
        <div class="parent">
            <div class="container">
            <h1>||-label-||</h1><br>
            {group_loaders}
    """

    element_style = SHOWCASE_GLOBAL_STYLES

    return element_code,element_style

def standard_loaders(index=0):
    outer_style = """
        <style>
        .parent {
        display: flex;
        justify-content: center;
        text-align: center;
        width: 100%;
        z-index: 999;
        }          
        .container {
            text-align: center;
            z-index: 999;
        }
        section {
            width: 30%;
            display: inline-block;
            text-align: center;
        }
        </style>
    """

    sub_loaders = [           
"""
<div class="loader" id="loader-1"></div>
""","""
<div class="loader" id="loader-2">
<span></span>
<span></span>
<span></span>
</div>
""","""
<div class="loader" id="loader-3"></div>
""","""
<div class="loader" id="loader-4">
<span></span>
<span></span>
<span></span>
</div>
""","""
<div class="loader" id="loader-5">
<span></span>
<span></span>
<span></span>
<span></span>
</div>
""","""
<div class="loader" id="loader-6">
<span></span>
<span></span>
<span></span>
<span></span>
</div>
""","""
<div class="loader" id="loader-7"></div>
""","""
<div class="loader" id="loader-8"></div>
"""]

    l = len(sub_loaders)
    if hasattr(index,'__iter__'):
        group_loaders = "".join([f"""{sub_loaders[i%l]}""" for i in index])
    else:
        group_loaders = sub_loaders[index%l]

    element_code = f"""
    <div class="parent">
        <div class="container">
            <h1>||-label-||</h1><br>
            {group_loaders}
    """

    element_style = SHOWCASE2_GLOBAL_STYLES

    return element_code,outer_style+element_style


class Loaders(Enum):
    points_line = auto()
    grid_points = auto()
    pulse_bars = auto()
    pacman = auto()
    standard_loaders = auto()
    showcase_pretty = auto()
    pretty_loaders = auto()


def get_loader(loader_name, **kargs):

    if loader_name == Loaders.points_line:
        return point_line(**kargs)
    elif loader_name == Loaders.grid_points:
        return grid_points(**kargs)
    elif loader_name == Loaders.pulse_bars:
        return pulse_bars(**kargs)
    elif loader_name == Loaders.pacman:
        return pacman_loader(**kargs)
    elif loader_name == Loaders.standard_loaders:
        return standard_loaders(**kargs)
    elif loader_name == Loaders.pretty_loaders:
        return pretty_loaders(**kargs)
    elif loader_name == Loaders.showcase_pretty:
        return showcase(**kargs)
    else:
        return pulse_bars(**kargs)


class HyLoader:

    def __init__(self, text='', loader_name=None, height=256, index=0, primary_color=None):
       
        #primary_color = st.get_option('theme.primaryColor')
        if primary_color is None:
            if st.get_option('theme.primaryColor') is None:
                primary_color = '#F63366'
            else:
                primary_color = st.get_option('theme.primaryColor')

        height_str = '{}{}'.format(str(height),'px')

        loader_div, loader_style = get_loader(loader_name,index=index)
        self.element_code = loader_div.replace('||-label-||',text)
        self.element_style = loader_style.replace('||-height-||',height_str)
        self.element_style = self.element_style.replace('||-pcolor-||',primary_color)

    def __enter__(self):
        self.display_element_style = st.markdown(self.element_style, unsafe_allow_html=True)
        self.display_element = st.markdown(self.element_code, unsafe_allow_html=True)
        

    def __exit__(self, *args, **kwargs):
        self.display_element_style.empty()
        self.display_element.empty()