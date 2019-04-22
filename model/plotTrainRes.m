Tb = readtable('record.csv');
Tb(1:3,:)
epochs = 1:size(Tb,1);
mean_overlapping_bboxes = Tb{:,1};
class_acc = Tb{:,2};
loss_rpn_cls = Tb{:,3};
loss_rpn_regr = Tb{:,4};
loss_class_cls = Tb{:,5};
loss_class_rerg = Tb{:,6};
curr_loss = Tb{:,7};
elapsed_time = Tb{:,8};

f1 = figure(1);
plot(epochs, mean_overlapping_bboxes);
title('Evolution of the mean overlapping between boxes as a function of the epochs')
xlabel('Epochs')
ylabel('mean_overlapping_bboxes')
saveas(f1, 'mean_overlapping_bboxes.png')

f2 = figure(2);
plot(epochs, class_acc);
title('Evolution de la précision de la classification en fonction du nombre d''epochs')
xlabel('Epochs')
ylabel('Précision de la classification')
saveas(f2, 'class_acc.png')

f3 = figure(3);
plot(epochs, loss_rpn_cls);
title('Evolution du cout de la classification du RPN en fonction du nombre d''epochs')
xlabel('Epochs')
ylabel('Cout de la classification du RPN')
saveas(f3, 'loss_rpn_cls.png')

f4 = figure(4);
plot(epochs, loss_rpn_regr);
title('Evolution du cout de la régression du RPN en fonction du nombre d''epochs')
xlabel('Epochs')
ylabel('Cout de la régression du RPN')
saveas(f4, 'loss_rpn_regr.png')

f5 = figure(5);
plot(epochs, loss_class_cls);
title('Evolution du cout de la classification du classificateur en fonction du nombre d''epochs')
xlabel('Epochs')
ylabel('Cout de la classification du classificateur')
saveas(f5, 'loss_class_cls.png')

f6 = figure(6);
plot(epochs, loss_class_rerg);
title('Evolution du cout de la régression du classificateur en fonction du nombre d''epochs')
xlabel('Epochs')
ylabel('Cout de la régression du classificateur')
saveas(f6, 'loss_class_rerg.png')

f7 = figure(7);
plot(epochs, curr_loss);
title('Evolution du cout total en fonction du nombre d''epochs')
xlabel('Epochs')
ylabel('Cout total')
saveas(f7, 'curr_loss.png')

f8 = figure(8);
plot(epochs, elapsed_time);hold on;
Umean = mean(mean(elapsed_time));
line(xlim, [Umean,Umean],'Color','r');
legend('Valeurs réelles','Moyenne')
title('Evolution du temps d''exécution d''une epoch en fonction du nombre d''epochs')
xlabel('Epochs')
ylabel('Temps d''exécution de l''epoch')
saveas(f8, 'elapsed_time.png')