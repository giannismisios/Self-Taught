from .base import *


class GLDv2(BaseDataset):
    def __init__(self, root, mode, transform=None, k_fold_eval=False, fold_idx=0):
        self.root = root + '/gldv2/train'
        self.mode = mode
        self.transform = transform

        if k_fold_eval:
            num_class_per_fold = 311657 // 4
            val_class_split = range(num_class_per_fold * fold_idx, num_class_per_fold * (fold_idx + 1))
            if self.mode == 'train':
                self.classes = [x for x in range(0, 311657) if (x not in val_class_split)]
            elif self.mode == 'val':
                self.classes = val_class_split
            '''elif self.mode == 'eval':
                self.classes = range(11318, 22634)'''
        else:
            if self.mode == 'train':
                self.classes = range(0, 311657)
            '''elif self.mode == 'eval':
                self.classes = range(11318, 22634)'''

        BaseDataset.__init__(self, self.root, self.mode, self.transform, k_fold_eval, fold_idx)

        '''with open(os.path.join(self.root, 'partof_equalmin15_train_clean.csv'), "r") as fr: #localpartof_train_clean
            lines = (line.strip() for line in fr.readlines())'''

        with open(os.path.join(self.root, 'localpartof_train_clean.csv'), "r") as fr: #localpartof_train_clean
            lines = (line.strip() for line in fr.readlines())

        index = 0
        for idx, line in enumerate(lines):
            if idx == 0:
                # skip the first line
                continue
            landmark, imgs = line.split(",")
            landmark = int(landmark)
            imgs = imgs.split()

            for img in imgs:
                #self.im_paths.append(img) #no use
                #self.landmarks.append(landmark)
                self.ys += [landmark]
                self.im_paths.append(os.path.join(self.root, img[0], img[1], img[2], img + ".jpg"))
                #self.labels.append(index)
                self.I += [index]
            index += 1